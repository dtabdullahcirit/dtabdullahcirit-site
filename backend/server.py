from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from http import cookies
from pathlib import Path
from urllib.parse import urlparse
import hashlib
import hmac
import json
import os
import re
import secrets
import smtplib
import sys
import threading
import time
from email.message import EmailMessage
from shutil import copy2


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
ROOT = PACKAGE_ROOT / "site"
if not ROOT.exists():
    ROOT = PACKAGE_ROOT / "outputs"
BACKEND_ROOT = Path(__file__).resolve().parent
APPOINTMENTS_FILE = BACKEND_ROOT / "appointments.json"
COMPLAINTS_FILE = BACKEND_ROOT / "complaints.json"
BACKUP_ROOT = BACKEND_ROOT / "backups"
ENV_FILES = [PACKAGE_ROOT / ".env", BACKEND_ROOT / ".env"]

MAX_BODY_BYTES = 12_000
SESSION_TTL_SECONDS = 60 * 60 * 8
SESSIONS = {}
RATE_BUCKETS = {}
DATA_LOCK = threading.Lock()
ALLOWED_TREATMENTS = {
    "Gülüş Tasarımı",
    "Estetik Diş Tedavisi",
    "Diş Beyazlatma",
    "Zirkonyum Diş Kaplama",
    "Porselen Kaplama",
    "Porselen Lamina",
    "İmplant",
    "İmplant Üstü Sabit Protezler",
    "Çocuk Diş Hekimliği",
    "Kompozit Lamina",
    "Ortodontik Tedavi",
    "Cerrahi Diş Çekimi",
    "Gömük Yirmi Yaş Diş Çekimi",
    "Sinüs Kaldırma",
}


def load_dotenv():
    for env_file in ENV_FILES:
        if not env_file.exists():
            continue
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


class SiteHandler(SimpleHTTPRequestHandler):
    server_version = "AbdullahCiritClinic/1.0"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        path = urlparse(self.path).path
        if path.startswith("/api/") or path.endswith("/admin.html"):
            cache_control = "no-store"
        elif path.endswith((".webp", ".jpg", ".jpeg", ".png", ".svg", ".ico")):
            cache_control = "public, max-age=31536000, immutable"
        elif path.endswith((".css", ".js")):
            cache_control = "public, max-age=3600, must-revalidate"
        elif path.endswith((".xml", ".txt")):
            cache_control = "public, max-age=3600"
        else:
            cache_control = "public, max-age=300, must-revalidate"
        self.send_header("Cache-Control", cache_control)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; "
            "img-src 'self' https://www.google.com https://maps.gstatic.com data:; "
            "style-src 'self' 'unsafe-inline'; "
            "font-src 'self'; "
            "script-src 'self' 'unsafe-inline'; "
            "connect-src 'self'; "
            "frame-src https://www.google.com; "
            "base-uri 'self'; form-action 'self'; object-src 'none'",
        )
        super().end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/session":
            return self.handle_session()
        if path == "/api/export":
            if not self.require_admin():
                return
            return self.handle_export()
        if path == "/api/appointments":
            if not self.require_admin():
                return
            return self.send_json(load_appointments())
        if path == "/api/complaints":
            if not self.require_admin():
                return
            return self.send_json(load_complaints())
        return super().do_GET()

    def do_POST(self):
        path = urlparse(self.path).path
        if path == "/api/login":
            return self.handle_login()
        if path == "/api/logout":
            return self.handle_logout()
        if path == "/api/appointments":
            return self.handle_appointment_post()
        if path == "/api/complaints":
            return self.handle_complaint_post()
        self.send_error(404)

    def send_error(self, code, message=None, explain=None):
        path = urlparse(self.path).path
        if path.startswith("/api/"):
            return self.send_json({"ok": False, "error": "İstek işlenemedi."}, status=code)

        public_messages = {
            400: ("Geçersiz istek", "İstek beklenen biçimde değil."),
            401: ("Oturum gerekli", "Bu sayfayı görüntülemek için giriş yapmanız gerekir."),
            403: ("Erişim reddedildi", "Bu işlem için yetkiniz bulunmuyor."),
            404: ("Sayfa bulunamadı", "Aradığınız sayfa taşınmış veya silinmiş olabilir."),
            413: ("İstek çok büyük", "Gönderilen veri izin verilen sınırı aşıyor."),
            429: ("Çok fazla istek", "Lütfen kısa bir süre sonra tekrar deneyin."),
        }
        title, detail = public_messages.get(code, ("Bir sorun oluştu", "İşlem şu anda tamamlanamadı."))
        body = f"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <title>{code} | Diş Hekimi Abdullah Cirit</title>
  <link rel="stylesheet" href="/page.css">
</head>
<body>
  <main class="content">
    <section class="card">
      <h1>{title}</h1>
      <p>{detail}</p>
      <a class="button" href="/index.html">Ana Sayfaya Dön</a>
    </section>
  </main>
</body>
</html>""".encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_DELETE(self):
        path = urlparse(self.path).path
        if path == "/api/appointments":
            if not self.require_admin(require_csrf=True):
                return
            save_appointments([])
            return self.send_json({"ok": True})
        if path == "/api/complaints":
            if not self.require_admin(require_csrf=True):
                return
            save_complaints([])
            return self.send_json({"ok": True})
        self.send_error(404)

    def handle_session(self):
        session = self.current_session()
        if not session:
            return self.send_json({"authenticated": False}, status=401)
        return self.send_json(
            {
                "authenticated": True,
                "csrfToken": session["csrf"],
                "expiresAt": session["expires_at"],
            }
        )

    def handle_login(self):
        if not self.check_rate_limit("login", limit=8, window_seconds=10 * 60):
            return self.send_json({"ok": False, "error": "Çok fazla deneme. Lütfen sonra tekrar deneyin."}, status=429)

        payload = self.read_json_payload()
        if payload is None:
            return

        password = str(payload.get("password", ""))
        if not verify_admin_password(password):
            time.sleep(0.4)
            return self.send_json({"ok": False, "error": "Şifre hatalı."}, status=401)

        session_id = secrets.token_urlsafe(32)
        csrf = secrets.token_urlsafe(32)
        expires_at = int(time.time() + SESSION_TTL_SECONDS)
        SESSIONS[session_id] = {"csrf": csrf, "expires_at": expires_at}

        self.send_response(200)
        self.send_cookie("clinic_admin_session", session_id, max_age=SESSION_TTL_SECONDS)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps({"ok": True, "csrfToken": csrf}).encode("utf-8"))

    def handle_logout(self):
        session_id = self.cookie_value("clinic_admin_session")
        if session_id:
            SESSIONS.pop(session_id, None)
        self.send_response(200)
        self.send_cookie("clinic_admin_session", "", max_age=0)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(b'{"ok": true}')

    def handle_export(self):
        query = urlparse(self.path).query
        export_type = "all"
        for part in query.split("&"):
            key, _, value = part.partition("=")
            if key == "type" and value in {"appointments", "complaints", "all"}:
                export_type = value

        payload = {
            "exportedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "type": export_type,
        }
        if export_type in {"appointments", "all"}:
            payload["appointments"] = load_appointments()
        if export_type in {"complaints", "all"}:
            payload["complaints"] = load_complaints()

        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        filename = f"abdullah-cirit-{export_type}-export.json"
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def handle_appointment_post(self):
        if not self.check_rate_limit("appointment", limit=6, window_seconds=10 * 60):
            return self.send_json({"ok": False, "error": "Çok fazla istek. Lütfen sonra tekrar deneyin."}, status=429)

        payload = self.read_json_payload()
        if payload is None:
            return

        cleaned, errors = validate_appointment(payload)
        if errors:
            return self.send_json({"ok": False, "errors": errors}, status=400)

        prepend_json_item(APPOINTMENTS_FILE, cleaned)

        email_sent = send_appointment_email(cleaned)
        self.send_json({"ok": True, "emailSent": email_sent})

    def handle_complaint_post(self):
        if not self.check_rate_limit("complaint", limit=5, window_seconds=10 * 60):
            return self.send_json({"ok": False, "error": "Çok fazla istek. Lütfen sonra tekrar deneyin."}, status=429)

        payload = self.read_json_payload()
        if payload is None:
            return

        cleaned, errors = validate_complaint(payload)
        if errors:
            return self.send_json({"ok": False, "errors": errors}, status=400)

        prepend_json_item(COMPLAINTS_FILE, cleaned)

        email_sent = send_complaint_email(cleaned)
        self.send_json({"ok": True, "emailSent": email_sent})

    def require_admin(self, require_csrf=False):
        session = self.current_session()
        if not session:
            self.send_json({"ok": False, "error": "Oturum gerekli."}, status=401)
            return False
        if require_csrf and self.headers.get("X-CSRF-Token") != session["csrf"]:
            self.send_json({"ok": False, "error": "CSRF doğrulaması başarısız."}, status=403)
            return False
        return True

    def current_session(self):
        session_id = self.cookie_value("clinic_admin_session")
        if not session_id:
            return None
        session = SESSIONS.get(session_id)
        if not session:
            return None
        if session["expires_at"] < time.time():
            SESSIONS.pop(session_id, None)
            return None
        return session

    def check_rate_limit(self, action, limit, window_seconds):
        key = (self.client_address[0], action)
        now = time.time()
        bucket = [ts for ts in RATE_BUCKETS.get(key, []) if now - ts < window_seconds]
        if len(bucket) >= limit:
            RATE_BUCKETS[key] = bucket
            return False
        bucket.append(now)
        RATE_BUCKETS[key] = bucket
        return True

    def read_json_payload(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_json({"ok": False, "error": "Geçersiz istek boyutu."}, status=400)
            return None
        if length < 0:
            self.send_json({"ok": False, "error": "Geçersiz istek boyutu."}, status=400)
            return None
        if length > MAX_BODY_BYTES:
            self.send_json({"ok": False, "error": "İstek çok büyük."}, status=413)
            return None
        raw = self.rfile.read(length).decode("utf-8", errors="replace")
        try:
            payload = json.loads(raw or "{}")
        except json.JSONDecodeError:
            self.send_json({"ok": False, "error": "Geçersiz JSON."}, status=400)
            return None
        if not isinstance(payload, dict):
            self.send_json({"ok": False, "error": "Geçersiz veri."}, status=400)
            return None
        return payload

    def send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_cookie(self, name, value, max_age):
        secure = os.environ.get("COOKIE_SECURE", "false").lower() == "true"
        cookie = f"{name}={value}; Max-Age={max_age}; Path=/; HttpOnly; SameSite=Lax"
        if secure:
            cookie += "; Secure"
        self.send_header("Set-Cookie", cookie)

    def cookie_value(self, name):
        raw = self.headers.get("Cookie", "")
        jar = cookies.SimpleCookie()
        try:
            jar.load(raw)
        except cookies.CookieError:
            return None
        morsel = jar.get(name)
        return morsel.value if morsel else None


def clean_text(value, max_len):
    text = str(value or "").replace("\x00", "").strip()
    return " ".join(text.split())[:max_len]


def clean_message(value, max_len=1200):
    text = str(value or "").replace("\x00", "").strip()
    return text[:max_len]


def validate_appointment(payload):
    treatment = clean_text(payload.get("treatment"), 120)
    if treatment not in ALLOWED_TREATMENTS:
        treatment = "Belirtilmedi"
    cleaned = {
        "id": clean_text(payload.get("id") or secrets.token_urlsafe(12), 80),
        "createdAt": clean_text(payload.get("createdAt") or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), 80),
        "name": clean_text(payload.get("name"), 100),
        "phone": clean_text(payload.get("phone"), 40),
        "treatment": treatment,
        "date": clean_text(payload.get("date"), 40),
        "message": clean_message(payload.get("message"), 1200),
        "status": "Yeni",
    }
    errors = []
    if not cleaned["name"]:
        errors.append("Ad soyad zorunludur.")
    if len(re.sub(r"\D", "", cleaned["phone"])) < 10:
        errors.append("Geçerli bir telefon numarası zorunludur.")
    return cleaned, errors


def validate_complaint(payload):
    cleaned = {
        "id": clean_text(payload.get("id") or secrets.token_urlsafe(12), 80),
        "createdAt": clean_text(payload.get("createdAt") or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), 80),
        "name": clean_text(payload.get("name"), 100),
        "phone": clean_text(payload.get("phone"), 40),
        "topic": clean_text(payload.get("topic"), 120),
        "message": clean_message(payload.get("message"), 1500),
        "status": "Yeni",
    }
    errors = []
    if not cleaned["name"]:
        errors.append("Ad soyad zorunludur.")
    if len(re.sub(r"\D", "", cleaned["phone"])) < 10:
        errors.append("Geçerli bir telefon numarası zorunludur.")
    if not cleaned["message"]:
        errors.append("Mesaj alanı zorunludur.")
    return cleaned, errors


def load_appointments():
    return load_json_list(APPOINTMENTS_FILE)


def save_appointments(appointments):
    save_json_list(APPOINTMENTS_FILE, appointments)


def load_complaints():
    return load_json_list(COMPLAINTS_FILE)


def save_complaints(complaints):
    save_json_list(COMPLAINTS_FILE, complaints)


def load_json_list(path):
    with DATA_LOCK:
        if not path.exists():
            return []
        try:
            items = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
        return items if isinstance(items, list) else []


def save_json_list(path, items):
    with DATA_LOCK:
        write_json_list_unlocked(path, items)


def prepend_json_item(path, item):
    with DATA_LOCK:
        if path.exists():
            try:
                items = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                items = []
        else:
            items = []
        if not isinstance(items, list):
            items = []
        items.insert(0, item)
        write_json_list_unlocked(path, items)


def write_json_list_unlocked(path, items):
    backup_json_file(path)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    temp_path.write_text(json.dumps(items[:500], ensure_ascii=False, indent=2), encoding="utf-8")
    temp_path.replace(path)


def backup_json_file(path):
    if not path.exists():
        return
    BACKUP_ROOT.mkdir(parents=True, exist_ok=True)
    label = path.stem
    day = time.strftime("%Y-%m-%d", time.localtime())
    week = time.strftime("%Y-W%U", time.localtime())
    for backup_name in (f"{day}-{label}.json", f"{week}-{label}.json"):
        backup_path = BACKUP_ROOT / backup_name
        if not backup_path.exists():
            copy2(path, backup_path)


def verify_admin_password(password):
    configured_hash = os.environ.get("ADMIN_PASSWORD_HASH", "").strip()
    configured_password = os.environ.get("ADMIN_PASSWORD", "").strip()
    if configured_hash:
        digest = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return hmac.compare_digest(digest, configured_hash)
    if configured_password:
        return hmac.compare_digest(password, configured_password)
    return False


def send_appointment_email(request):
    return send_email(
        "Yeni randevu talebi",
        [
            "Yeni randevu talebi geldi.",
            "",
            f"Ad Soyad: {request.get('name', '-')}",
            f"Telefon: {request.get('phone', '-')}",
            f"Tedavi: {request.get('treatment', '-')}",
            f"Tercih Tarihi: {request.get('date', '-')}",
            f"Mesaj: {request.get('message', '-')}",
            f"Kayıt Zamanı: {request.get('createdAt', '-')}",
        ],
    )


def send_complaint_email(request):
    return send_email(
        "Yeni görüş ve öneri",
        [
            "Yeni görüş / öneri bildirimi geldi.",
            "",
            f"Ad Soyad: {request.get('name', '-')}",
            f"Telefon: {request.get('phone', '-')}",
            f"Konu: {request.get('topic', '-')}",
            f"Mesaj: {request.get('message', '-')}",
            f"Kayıt Zamanı: {request.get('createdAt', '-')}",
        ],
    )


def send_email(subject, lines):
    user = os.environ.get("APPOINTMENT_EMAIL_USER", "dtabdullahcirit@gmail.com").strip()
    password = (
        os.environ.get("APPOINTMENT_EMAIL_PASS")
        or os.environ.get("GMAIL_APP_PASSWORD")
        or os.environ.get("EMAIL_PASSWORD")
        or os.environ.get("SMTP_PASSWORD")
        or ""
    )
    to_address = os.environ.get("APPOINTMENT_EMAIL_TO", user)
    if not user or not password or not to_address:
        missing = []
        if not user:
            missing.append("APPOINTMENT_EMAIL_USER")
        if not password:
            missing.append("APPOINTMENT_EMAIL_PASS")
        if not to_address:
            missing.append("APPOINTMENT_EMAIL_TO")
        print(f"Email send skipped: missing environment value(s): {', '.join(missing)}", file=sys.stderr)
        return False
    to_address = to_address.strip()
    password = "".join(password.split())

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = to_address
    msg.set_content("\n".join(lines))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as smtp:
            smtp.login(user, password)
            smtp.send_message(msg)
        print(f"Email sent successfully to {to_address}", file=sys.stderr)
        return True
    except Exception as exc:
        print(f"Email send failed for {user} -> {to_address}: {type(exc).__name__}: {exc}", file=sys.stderr)
        return False


if __name__ == "__main__":
    load_dotenv()
    if not os.environ.get("ADMIN_PASSWORD") and not os.environ.get("ADMIN_PASSWORD_HASH"):
        print("WARNING: ADMIN_PASSWORD or ADMIN_PASSWORD_HASH is not set. Admin login is disabled.")
    port = int(os.environ.get("PORT", 10000))
    host = "0.0.0.0"
    server = ThreadingHTTPServer((host, port), SiteHandler)
    print(f"Serving {ROOT} on http://{host}:{port}")
    server.serve_forever()
