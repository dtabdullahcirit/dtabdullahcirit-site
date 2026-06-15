const treatmentContent = {
  "Gülüş Tasarımı": {
    text: "Gülüş tasarımı; dişlerin rengi, formu, dizilimi, diş eti görünümü ve yüz hattı birlikte değerlendirilerek hazırlanan kişisel estetik planlamadır. Amaç tek tip bir görünüm oluşturmak değil, kişinin yüz ifadesiyle uyumlu, doğal ve sağlıklı bir gülüş elde etmektir.",
    suitable: ["Diş formundan veya renginden memnun olmayan hastalar", "Ön bölgede aralık, aşınma ya da şekil bozukluğu olan kişiler", "Daha doğal ve dengeli bir gülüş isteyen hastalar"],
    steps: ["Beklentileriniz, ağız yapınız ve yüz oranlarınız değerlendirilir.", "Fotoğraf, renk ve kapanış analizi ile tedavi seçenekleri belirlenir.", "Beyazlatma, dolgu, lamina, kaplama veya diş eti düzenleme ihtiyacı planlanır.", "Uygulamalar doğal görünüm hedefiyle seanslar halinde tamamlanır.", "Son kontrolde ağız bakımı, koruma ve takip önerileri paylaşılır."],
    note: "Gülüş tasarımında estetik beklenti kadar diş eti sağlığı ve kapanış ilişkisi de önemlidir."
  },
  "Estetik Diş Tedavisi": {
    text: "Estetik diş tedavisi; dişlerdeki renk, şekil, boyut ve yüzey problemlerini doğal görünüme en yakın şekilde düzenlemeyi hedefler. Tedavi planı hastanın ağız yapısına, beklentisine ve mevcut diş dokusuna göre kişiselleştirilir.",
    suitable: ["Kırık, aşınmış veya şekil bozukluğu olan dişler", "Renklenme ya da eski restorasyon problemi yaşayan hastalar", "Gülüşünde daha uyumlu bir görünüm isteyen kişiler"],
    steps: ["Diş dokusu, diş eti ve kapanış ilişkisi incelenir.", "Estetik beklentileriniz dinlenir ve uygulanabilir seçenekler anlatılır.", "Kompozit dolgu, porselen lamina, zirkonyum kaplama veya beyazlatma ihtiyacı belirlenir.", "Tedavi doğal renk ve form hedefiyle uygulanır.", "Sonrasında bakım önerileri ve kontrol aralığı belirlenir."],
    note: "Estetik uygulamalar planlanırken sağlam diş dokusunu korumak önceliklidir."
  },
  "Lazer Destekli Diş Hekimliği": {
    text: "Lazer destekli diş hekimliği, uygun vakalarda tedavi konforunu artırmak ve bazı işlemleri daha kontrollü yürütmek için kullanılan modern destek uygulamalarını kapsar. Her hasta için lazer kullanımına uygunluk muayene sonrası belirlenir.",
    suitable: ["Diş eti işlemlerinde destek gerektiren vakalar", "Hassasiyet ve konfor beklentisi yüksek hastalar", "Hekim değerlendirmesiyle lazer uygulamasına uygun bulunan kişiler"],
    steps: ["İşlem bölgesi ve tedavi ihtiyacı değerlendirilir.", "Lazer desteğinin gerekli olup olmadığı hastaya açıklanır.", "Uygun protokol ile işlem kontrollü şekilde uygulanır.", "İşlem sonrası bakım önerileri verilir.", "Gerekirse iyileşme kontrolü için randevu planlanır."],
    note: "Lazer her işlemde zorunlu değildir; doğru endikasyonla kullanıldığında tedaviye destek sağlar."
  },
  "Diş Beyazlatma": {
    text: "Diş beyazlatma, diş yüzeyindeki renklenmeleri azaltmak ve mevcut diş rengini daha açık tona taşımak için hekim kontrolünde uygulanan estetik bir işlemdir. İşlem öncesi diş ve diş eti sağlığının uygun olması gerekir.",
    suitable: ["Çay, kahve veya sigara kaynaklı renklenme yaşayan hastalar", "Diş renginden memnun olmayan kişiler", "Kaplama gerektirmeden daha aydınlık bir gülüş isteyen hastalar"],
    steps: ["Diş taşı, çürük ve diş eti durumu değerlendirilir.", "Mevcut diş rengi belirlenir ve beklenti gerçekçi şekilde konuşulur.", "Uygun beyazlatma yöntemi seçilir.", "İşlem hekim kontrolünde uygulanır.", "Renk korunumu için beslenme ve bakım önerileri paylaşılır."],
    note: "Beyazlatma dolguların veya kaplamaların rengini açmaz; bu nedenle tüm ağız estetiği birlikte değerlendirilmelidir."
  },
  "Porselen Laminalar": {
    text: "Porselen laminalar, özellikle ön bölge dişlerinde renk, form ve küçük dizilim problemlerini düzeltmek için kullanılan ince porselen yüzeylerdir. Doğal ışık geçirgenliği sayesinde estetik ve zarif sonuçlar hedeflenir.",
    suitable: ["Ön dişlerinde renk veya form problemi olan hastalar", "Diş aralıklarından rahatsız olan kişiler", "Minimal müdahale ile estetik iyileşme isteyen hastalar"],
    steps: ["Ön dişlerin formu, kapanışı ve diş eti görünümü değerlendirilir.", "Gülüş hattına uygun lamina planı hazırlanır.", "Gerekli ölçü ve prova aşamaları tamamlanır.", "Laminalar dişe uyumlu şekilde yapıştırılır.", "Bakım ve kontrol aralığı hastaya anlatılır."],
    note: "Lamina tedavisinde başarı için doğru vaka seçimi ve düzenli ağız bakımı çok önemlidir."
  },
  "Porselen Kaplama": {
    text: "Porselen kaplama, madde kaybı, renk değişikliği, form bozukluğu veya eski restorasyon problemi bulunan dişlerde hem estetik görünümü hem de çiğneme fonksiyonunu desteklemek için planlanan kaplama uygulamasıdır. Tedavide diş eti uyumu, kapanış ilişkisi, renk seçimi ve komşu dişlerle doğal görünüm birlikte değerlendirilir.",
    suitable: ["Renk, form veya eski kaplama problemi olan hastalar", "Madde kaybı nedeniyle desteklenmesi gereken dişler", "Estetik ve fonksiyon ihtiyacını birlikte çözmek isteyen kişiler"],
    steps: ["Muayenede diş dokusu, diş eti sağlığı ve kapanış ilişkisi incelenir.", "Kaplama yapılacak diş sayısı, renk ve form planı hastayla birlikte belirlenir.", "Gerekli diş hazırlığı ve ölçü aşaması tamamlanır.", "Prova aşamasında estetik görünüm, konuşma ve kapanış kontrol edilir.", "Kaplamalar uyumlandırılarak bakım ve kontrol önerileri paylaşılır."],
    note: "Porselen kaplamaların uzun ömürlü olması için diş eti sağlığı, düzenli ağız bakımı ve kontrol randevuları önemlidir."
  },
  "Porselen Lamina": {
    text: "Porselen lamina, özellikle ön dişlerin görünen yüzeyine uygulanan ince porselen yapraklarla renk, form, küçük aralık ve yüzey düzensizliklerini düzenlemeyi hedefleyen estetik bir tedavidir. Doğru vaka seçiminde doğal ışık geçirgenliğiyle zarif ve yüz hattıyla uyumlu sonuçlar elde edilebilir.",
    suitable: ["Ön dişlerinde renk, aralık veya form problemi olan hastalar", "Daha doğal ve parlak bir gülüş isteyen kişiler", "Uygun diş yapısına sahip ve minimal müdahale ile estetik iyileşme isteyen hastalar"],
    steps: ["Gülüş hattı, diş formu, renk beklentisi ve kapanış ilişkisi değerlendirilir.", "Hastaya uygun lamina planı ve alternatif tedavi seçenekleri anlatılır.", "Gerekli ölçü, renk seçimi ve prova aşamaları tamamlanır.", "Laminalar dişe uyumlu ve kontrollü şekilde yapıştırılır.", "Bakım, sert gıda kullanımı ve düzenli kontrol önerileri paylaşılır."],
    note: "Porselen lamina her diş yapısı için uygun olmayabilir; karar muayene ve kapanış değerlendirmesiyle verilir."
  },
  "Zirkonyum Diş Kaplama": {
    text: "Zirkonyum diş kaplama, estetik beklentisi yüksek bölgelerde doğal görünüme yakın ve dayanıklı sonuçlar elde etmek için kullanılan kaplama seçeneklerinden biridir. Diş rengi, diş eti uyumu, kapanış ilişkisi ve gülüş hattı birlikte değerlendirilerek planlanır.",
    suitable: ["Renk, form veya eski kaplama problemi olan hastalar", "Ön ve arka bölgede estetik ve dayanıklılığı birlikte isteyen kişiler", "Gülüş görünümünü daha dengeli hale getirmek isteyen hastalar"],
    steps: ["Muayenede diş dokusu, diş eti ve kapanış ilişkisi değerlendirilir.", "Renk, form ve kaplama sayısı hastayla birlikte planlanır.", "Gerekli hazırlık ve ölçü aşaması tamamlanır.", "Prova aşamasında estetik ve kapanış kontrol edilir.", "Zirkonyum kaplamalar uyumlandırılarak bakım önerileri paylaşılır."],
    note: "Zirkonyum kaplamalarda doğal görünüm için diş eti sağlığı, renk seçimi ve düzenli bakım önemlidir."
  },
  "İmplant Üstü Sabit Protezler": {
    text: "İmplant üstü sabit protezler, eksik dişlerin implantlardan destek alınarak sabit şekilde tamamlanmasını sağlayan protez uygulamalarıdır. Amaç çiğneme konforunu artırmak, estetik görünümü düzenlemek ve günlük kullanımı kolaylaştırmaktır.",
    suitable: ["Birden fazla diş eksikliği olan hastalar", "Hareketli protez yerine sabit çözüm isteyen kişiler", "İmplant tedavisi tamamlanmış ve üst yapı aşamasına gelen hastalar"],
    steps: ["İmplantların konumu ve çevre doku sağlığı değerlendirilir.", "Ölçü alınarak protez tasarımı planlanır.", "Prova aşamalarında estetik, konuşma ve kapanış kontrol edilir.", "Sabit protez ağız içinde uyumlandırılarak teslim edilir.", "Temizlik, bakım ve düzenli kontrol programı anlatılır."],
    note: "İmplant üstü protezlerin uzun ömürlü olması için ara yüz temizliği ve düzenli kontroller aksatılmamalıdır."
  },
  "İmplant": {
    text: "İmplant tedavisi, eksik dişlerin yerine çene kemiğine yerleştirilen yapay diş kökleri ile sabit ve konforlu bir çözüm sunmayı hedefler. Tedavi planı kemik yapısı, diş eti sağlığı, genel sağlık durumu ve protez ihtiyacına göre hazırlanır.",
    suitable: ["Tek veya çoklu diş eksikliği olan hastalar", "Hareketli protez kullanımında zorlanan kişiler", "Kemik yapısı ve genel sağlık durumu implant için uygun olan hastalar"],
    steps: ["Muayene ve görüntüleme ile kemik yapısı ayrıntılı değerlendirilir.", "İmplant sayısı, konumu ve üst protez planı belirlenir.", "Cerrahi işlem steril klinik koşullarında uygulanır.", "İyileşme süreci düzenli kontrollerle takip edilir.", "Üst yapı protezi tamamlanarak kullanım ve bakım önerileri verilir."],
    note: "İmplant tedavisinde doğru planlama, hijyen ve kontrol randevuları tedavinin başarısını doğrudan etkiler."
  },
  "Çocuk Diş Hekimliği": {
    text: "Çocuk diş hekimliği, süt ve daimi dişlerin sağlıklı gelişimini takip etmeyi, çürükleri erken dönemde önlemeyi ve çocuğun diş hekimiyle güvenli bir ilişki kurmasını amaçlar. Tedaviler çocuğun yaşına, uyumuna ve ağız sağlığı ihtiyacına göre planlanır.",
    suitable: ["İlk diş hekimi kontrolüne gelecek çocuklar", "Çürük, ağrı veya diş hassasiyeti yaşayan çocuklar", "Koruyucu flor, fissür örtücü veya düzenli takip ihtiyacı olan hastalar"],
    steps: ["İlk görüşmede çocukla güven ilişkisi kurulmaya çalışılır.", "Dişler, çene gelişimi ve ağız bakım alışkanlıkları değerlendirilir.", "Koruyucu uygulamalar veya gerekli tedaviler aileye açıklanır.", "Tedavi çocuğun uyumuna göre sakin ve aşamalı şekilde yürütülür.", "Ev bakımı, beslenme ve kontrol aralıkları aileyle paylaşılır."],
    note: "Çocuklarda düzenli kontrol, çürük oluşmadan önlem almak için en güçlü adımdır."
  },
  "Kompozit Lamina": {
    text: "Kompozit lamina, ön dişlerdeki küçük şekil bozuklukları, aralıklar, renk uyumsuzlukları veya yüzey problemlerini kompozit materyalle düzenlemeyi hedefleyen estetik bir uygulamadır. Çoğu vakada daha konservatif ve hızlı bir seçenek olarak değerlendirilir.",
    suitable: ["Ön dişlerinde küçük aralık veya form problemi olan hastalar", "Minimal müdahale ile estetik iyileşme isteyen kişiler", "Kırık, aşınma veya yüzey düzensizliği bulunan dişler"],
    steps: ["Diş formu, renk ve kapanış ilişkisi değerlendirilir.", "Kompozit lamina ile elde edilebilecek sonuç hastaya anlatılır.", "Uygun renk seçimi yapılarak diş yüzeyi hazırlanır.", "Kompozit materyal katmanlar halinde şekillendirilir ve cilalanır.", "Bakım, renklenmeden korunma ve kontrol önerileri paylaşılır."],
    note: "Kompozit lamina sonrası çay, kahve ve sigara kaynaklı renklenmelere karşı düzenli bakım önerilir."
  },
  "Çene Cerrahisi": {
    text: "Çene cerrahisi; cerrahi diş çekimi, implant uygulamaları, gömük dişler ve ileri cerrahi işlemleri kapsayan tedavi alanıdır. Her işlem öncesinde radyolojik değerlendirme yapılarak kişiye özel plan oluşturulur.",
    suitable: ["Gömük veya problemli dişi olan hastalar", "Cerrahi çekim ya da implant planlanan kişiler", "Çene kemiği veya çevre dokularda cerrahi işlem ihtiyacı olan hastalar"],
    steps: ["Şikayet, ağız içi muayene ve görüntüler birlikte değerlendirilir.", "İşlem planı, riskler ve iyileşme süreci açıkça anlatılır.", "Cerrahi uygulama lokal anestezi altında kontrollü şekilde yapılır.", "İşlem sonrası ilaç, beslenme ve bakım önerileri verilir.", "Kontrol randevusunda iyileşme takip edilir."],
    note: "Cerrahi işlemlerden sonra verilen bakım talimatlarına uymak iyileşme sürecini rahatlatır."
  },
  "Sinüs Kaldırma": {
    text: "Sinüs kaldırma, üst çene arka bölgede implant için yeterli kemik yüksekliği bulunmadığında uygulanan destekleyici cerrahi işlemdir. Amaç implant yerleşimi için uygun kemik hacmini oluşturmaktır.",
    suitable: ["Üst arka bölgede kemik hacmi yetersiz olan hastalar", "İmplant planlanan ancak sinüs mesafesi uygun olmayan kişiler", "Radyolojik değerlendirmede ek kemik desteği gereken vakalar"],
    steps: ["Üst çene kemik hacmi görüntüleme ile incelenir.", "İmplant için sinüs kaldırma gerekip gerekmediği belirlenir.", "Cerrahi işlem kişiye özel plana göre uygulanır.", "İyileşme süreci ve dikkat edilecekler anlatılır.", "Uygun zamanda implant veya üst yapı aşamasına geçilir."],
    note: "Sinüs kaldırma işlemi her implant hastasında gerekmez; karar muayene ve görüntüleme sonrası verilir."
  },
  "Cerrahi Diş Çekimi": {
    text: "Cerrahi diş çekimi, normal çekimle alınması zor olan dişlerde kontrollü cerrahi yaklaşımla uygulanan işlemdir. Dişin konumu, kök yapısı ve çevre dokular işlem öncesi değerlendirilir.",
    suitable: ["Kırık veya kök yapısı problemli dişler", "Standart çekimle alınamayan dişler", "Çevre dokulara zarar vermeden planlı çekim gereken vakalar"],
    steps: ["Dişin pozisyonu ve çevre dokular görüntüleme ile incelenir.", "Çekim yöntemi ve işlem sonrası süreç hastaya anlatılır.", "Cerrahi çekim steril koşullarda uygulanır.", "Kanama kontrolü ve yara bakımı önerileri verilir.", "Gerekli durumda kontrol randevusu planlanır."],
    note: "Cerrahi çekim sonrası ilk gün beslenme, ağız çalkalama ve sigara kullanımı konusunda dikkatli olunmalıdır."
  },
  "Gömük Yirmi Yaş Diş Çekimi": {
    text: "Gömük yirmi yaş dişleri ağrı, şişlik, enfeksiyon, komşu dişe baskı veya temizlik zorluğu gibi sorunlara yol açabilir. Çekim kararı dişin pozisyonu ve hastanın şikayetleri değerlendirilerek verilir.",
    suitable: ["Gömük veya yarı gömük yirmi yaş dişi olan hastalar", "Tekrarlayan ağrı, şişlik veya enfeksiyon yaşayan kişiler", "Komşu dişe baskı riski bulunan vakalar"],
    steps: ["Yirmi yaş dişinin pozisyonu panoramik görüntüyle incelenir.", "Sinir ve komşu diş ilişkileri değerlendirilir.", "Cerrahi işlem planı ve iyileşme süreci açıklanır.", "Çekim kontrollü şekilde tamamlanır.", "İyileşme kontrolleri ve bakım önerileri paylaşılır."],
    note: "Gömük diş çekimlerinde kişisel iyileşme süreci değişebilir; kontrol randevuları önemlidir."
  },
  "Ortodontik Tedavi": {
    text: "Ortodontik tedavi, çapraşık, aralıklı veya yanlış konumlanmış dişlerin ve kapanış problemlerinin düzeltilmesini hedefler. Tedavi seçeneği yaş, diş dizilimi, çene ilişkisi ve beklentiye göre belirlenir.",
    suitable: ["Dişlerinde çapraşıklık veya aralık olan hastalar", "Kapanış problemi yaşayan kişiler", "Estetik ve fonksiyonel olarak daha düzenli diş dizilimi isteyen hastalar"],
    steps: ["Diş dizilimi, kapanış ve çene ilişkisi değerlendirilir.", "Gerekli ölçü, fotoğraf ve radyolojik kayıtlar alınır.", "Tel veya şeffaf plak gibi uygun seçenekler anlatılır.", "Düzenli kontrollerle diş hareketleri takip edilir.", "Tedavi sonrası pekiştirme ve bakım aşaması planlanır."],
    note: "Ortodontik tedavide başarı, düzenli kontroller ve hastanın kullanım talimatlarına uyumuyla artar."
  }
};

const title = document.querySelector("h1")?.textContent.trim();
const data = treatmentContent[title];
const detail = document.querySelector(".treatment-detail > div");

if (data && detail) {
  detail.innerHTML = `
    <span class="detail-kicker">Tedavi Sürecimiz</span>
    <h2>${title}</h2>
    <p class="detail-intro">${data.text}</p>
    <div class="detail-panels">
      <article>
        <h3>Kimler için uygundur?</h3>
        <ul>${data.suitable.map((item) => `<li>${item}</li>`).join("")}</ul>
      </article>
      <article>
        <h3>Tedavi sürecimiz nasıl ilerler?</h3>
        <ol>${data.steps.map((item) => `<li>${item}</li>`).join("")}</ol>
      </article>
    </div>
    <p class="detail-note">${data.note}</p>
    <a class="button" href="online-randevu.html">Randevu Oluştur</a>
  `;
}
