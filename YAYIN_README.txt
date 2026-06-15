Diş Hekimi Abdullah Cirit Klinik Sitesi - Yayın Paketi

Bu paket yayın firmasına teslim edilmek üzere hazırlanmıştır.

Klasör yapısı:
- site/: Ziyaretçiye gösterilecek tüm HTML, CSS, JS ve görsel dosyaları.
- backend/server.py: Randevu ve şikayet formlarını kaydeden ve e-postaya gönderen Python sunucusu.
- backend/appointments.json: Randevu taleplerinin tutulduğu dosya.
- backend/complaints.json: Şikayet ve geri bildirim kayıtlarının tutulduğu dosya.
- .env.example: E-posta ayarlarının örnek dosyası.
- start_server.bat: Windows ortamında yerel test için başlatma dosyası.

Yerel test:
1. Zip dosyasını açın.
2. backend/.env.example dosyasını backend/.env olarak kopyalayın.
3. backend/.env içindeki e-posta ve admin bilgilerini doldurun.
4. start_server.bat dosyasını çalıştırın.
5. http://127.0.0.1:4190/index.html adresini açın.

Yayın notu:
Bu site statik HTML dosyalarıyla açılır; ancak randevu ve şikayet formlarının çalışması için backend/server.py dosyasının da sunucuda çalıştırılması gerekir. Yayın firması isterse bu Python backend yerine aynı /api/appointments ve /api/complaints uç noktalarını kendi hosting altyapısında yeniden kurabilir.

Önerilen canlı kurulum:
- Backend'i reverse proxy arkasında çalıştırın.
- HTTPS zorunlu olsun.
- Canlı ortamda COOKIE_SECURE=true yapın.
- Backend doğrudan internete açılacaksa HOST=0.0.0.0 kullanılabilir; aksi halde 127.0.0.1 reverse proxy için daha güvenlidir.
- sitemap.xml ve robots.txt içindeki domain gerçek yayın domainiyle aynı olmalıdır.
- Python komutu: python backend/server.py
- Render benzeri platformlarda start command: python backend/server.py
- Turhost/cPanel gibi ortamlarda Python app kurulumunda uygulama dosyası backend/server.py olarak seçilmeli; site klasörü statik kök olarak servis edilmelidir.

E-posta:
Randevu ve şikayet formları aynı e-posta ayarlarını kullanır:
APPOINTMENT_EMAIL_USER
APPOINTMENT_EMAIL_PASS
APPOINTMENT_EMAIL_TO

Admin güvenliği:
Admin paneli artık tarayıcı içinde sabit şifre tutmaz. Yayın ortamında .env dosyasında ADMIN_PASSWORD veya ADMIN_PASSWORD_HASH tanımlanmalıdır. HTTPS yayında COOKIE_SECURE=true yapılmalıdır.
Admin şifresi en az 12-16 karakter, tahmin edilemeyen ve sadece bu siteye özel olmalıdır. Mümkünse ADMIN_PASSWORD yerine ADMIN_PASSWORD_HASH kullanılmalıdır.

Yedekleme ve export:
- backend/server.py her kayıt yazımından önce backend/backups klasörüne günlük ve haftalık JSON yedeği oluşturur.
- Admin panelinde aktif listeyi veya tüm kayıtları JSON olarak indirmek için export butonları vardır.
- Yayın firması ayrıca sunucu seviyesinde günlük dosya yedeği planlamalıdır.

Güvenlik:
Gerçek e-posta şifresi veya Gmail uygulama şifresi .env.example içine yazılmamıştır. Bu bilgi yayın firmasına ayrı ve güvenli bir kanaldan verilmelidir.
