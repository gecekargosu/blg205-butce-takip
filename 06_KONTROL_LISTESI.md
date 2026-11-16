# BLG205 Ara Teslim — Kontrol Listesi

Cengiz Kılıç · 251205027 · 16 Kasım 2026 · sürüm 1

Bu liste üç soruya cevap verir. Hoca ne istedi, bizde var mı, kanıtı nerede.
Durum işaretleri: **TAM** hazır · **KISMEN** var ama eksik · **YOK** henüz yok · **FİNAL** yönerge gereği finalde

---

## 1. Hocanın teslim öncesi kontrol listesi (yönerge bölüm 9)

Yönergenin sonundaki dokuz maddenin birebir karşılığı.

| # | Hocanın maddesi | Durum | Kanıt / not |
|---|---|---|---|
| 1 | Bölüm 3'teki 8 zorunlu gereksinim tamamı | **KISMEN** | 3'ü kodda var, 5'i hafta 11–15 planında tarihli. Ara teslim tanımı "derlenebilen ilk sürüm" olduğu için bu normal, ama finalde pazarlık yok |
| 2 | Tüm alanlar private, kod paketlere ayrıldı | **TAM** | 8 sınıf, 3 paket: `model`, `service`, `app`. Bütün alanlar `private` |
| 3 | Hatalı girişlerde program çökmüyor | **TAM** | Menüde sayı yerine harf, olmayan seçim ve boş giriş denendi. Hepsi "Gecersiz secim" mesajıyla menüye döndü. Setter'larda da doğrulama var |
| 4 | Veriler dosyaya kaydediliyor ve açılışta yükleniyor | **FİNAL** | Hafta 13. Şu an örnek veriler `Main.ornekVerileriYukle` içinde |
| 5 | UML diyagramı final koduyla uyumlu | **TAM** | Betikle karşılaştırıldı: kodda olup UML'de olmayan sınıf veya metot sayısı 0 |
| 6 | README ile başka bilgisayarda çalışıyor | **TAM** | Bu oturumda yeniden derlendi. `javac` 0 hata, `javac --release 17` de 0 hata |
| 7 | Raporda eşleştirme tablosu, iş bölümü, yapay zekâ beyanı | **KISMEN** | Üçünün iskeleti `05_Rapor_Plani/FINAL_RAPOR_PLANI.md` içinde. Rapora taşınacak |
| 8 | Demo videosu bağlantısı erişime açık | **FİNAL** | Final teslimi, 18 Aralık |
| 9 | ZIP doğru isimlendirildi ve zamanında yüklendi | **KISMEN** | Yönerge `Ogrenci_isim_soyisim_bölüm_.zip` istiyor. Mevcut adda bölüm adı yok, düzeltilecek |

---

## 2. Sekiz zorunlu teknik gereksinim

Yönergenin bölüm 3 tablosu. Bu tablo rapora da girecek.

| # | Gereksinim | Şu an | Nerede | Finalde eklenecek | Tarih |
|---|---|---|---|---|---|
| 1 | Sınıflar ve kapsülleme, en az 6 sınıf, static alan/metot | **TAM** | 8 sınıf. `Islem.sayac` ve `Kategori.sayac` static alan, `Islem.paraYaz` static metot | — | — |
| 2 | Kalıtım, super çağrısı, override, toString | **TAM** | `Islem` → `Gelir`, `Islem` → `Gider` → `SabitGider`. Üç seviye hiyerarşi. `butceEtkisi`, `tip`, `toString` ezildi | — | — |
| 3 | Soyut sınıf ve çok biçimlilik | **TAM** | `Islem` soyut, `butceEtkisi()` ve `tip()` soyut. `ButceService` içinde `Islem[]` dizisi üzerinden çağrı | — | — |
| 4 | Arayüz ve Comparable/Comparator ile sıralama | **YOK** | — | `Raporlanabilir` arayüzü, tarihe göre `Comparable` | Hafta 12 |
| 5 | Özel istisna ve try-catch | **YOK** | — | `GecersizTutarException`, girişlerde try-catch | Hafta 10 |
| 6 | ArrayList ve HashMap temel veri yapısı | **KISMEN** | `Islem[]` ve `Kategori[]` sabit boyutlu dizi. Hafta 8'e kadar dizi bilinçli tercih | `ArrayList<Islem>`, kategori özetinde `HashMap` | Hafta 11 |
| 7 | Dosya işlemleri, açılışta okuma, dosya yoksa çökmeme | **YOK** | — | `DosyaIslemleri` sınıfı, TXT biçimi | Hafta 13 |
| 8 | Lambda ve Stream, en az 2 farklı işlem | **YOK** | — | Filtreleme ve sıralamada `filter` + `sorted` + `collect` | Hafta 15 |

**Kritik oran.** Sekiz gereksinimden beşi finalde. Yönergeye göre kod puanı 100 üzerinden 60 ve bu beşi toplam 40 puan. Yetişmezse kod puanı yarıya iner.

---

## 3. Kodun çalıştığının kanıtı

Bu oturumda sıfırdan derlenip çalıştırıldı, sonuçlar aşağıda.

| Kontrol | Komut | Sonuç |
|---|---|---|
| Derleme | `javac -encoding UTF-8 -d build $(find src -name "*.java")` | 0 hata, 8 `.class` üretildi |
| JDK 17 uyumu | `javac --release 17 ...` | 0 hata. Yönerge "JDK 17 veya üzeri" diyor, kod 17'de de derleniyor |
| Çalışma | `java -cp build app.Main` | Menü açıldı, dört seçenek çalıştı |
| Listeleme | seçim 1 | Altı kayıt, tarih, tutar, kategori ile geldi |
| Bütçe özeti | seçim 2 | Gelir 38000, gider 16180, net 26820. Tasarım dosyasındaki ekranla aynı |
| Tür analizi | seçim 3 | Gelir 2, gider 2, sabit gider 2 |
| Hatalı giriş | sayı yerine harf | Çökme yok, uyarı verip menüye döndü |
| Geçersiz tutar | setter üzerinden | Uyarı verdi, eski değeri korudu |

Ortam: javac 25.0.1, Windows, UTF-8. Kod 17 ile de derlendiği için hoca kendi makinesinde sorun yaşamaz.

---

## 4. Ek 10 puan kontrolü

Yönergede yedi kalem var, her biri yaklaşık 1,5 puan. Biz dördünü seçtik. Fazlasını denemek kodu büyütür ve sözlüde savunmayı zorlaştırır.

| Kalem | Hedef | Şu an | Eksik olan | Beklenen puan |
|---|---|---|---|---|
| Generic `Repository<T>` | Evet | Planlandı | Sınıf yok, hafta 11 | 1,5 |
| JUnit 5, en az 10 test | Evet | Planlandı | Test yok, hafta 14 | 1,5 |
| Git ve GitHub | Evet | **Yerel depo var, 2 commit** | Uzak depoya gönderilmedi, hoca göremez | 1,5 → risk altında |
| Javadoc | Evet | **KISMEN** | Sınıf ve metot yorumları yazıldı ama `javadoc` çıktısı üretilmedi | 1,5 → yarım |
| Swing/JavaFX arayüz | Hayır | — | Kodu iki katına çıkarır | 0 |
| Thread | Hayır | — | Anlamsız kalır | 0 |
| Tasarım deseni | Hayır | — | Tek kişilik projede zorlama olur | 0 |

**En ucuz iki puan.** Javadoc bugün 15 dakikada üretilir, Git deposu bugün gönderilirse kanıtlanır. İkisi birlikte 3 puan, kod yazmadan.

**Kalan 3 puan** hafta 11 ve 14'te geliyor. İkisi de finalden önce.

---

## 5. Benim eklediğim kontroller

Yönergede yazmayan ama teslimde işe yarayan maddeler.

| Kontrol | Neden | Durum |
|---|---|---|
| UML ile kodu betikle karşılaştırma | Hoca "UML final kodla uyumlu" diye bakacak | TAM, fark 0 |
| `--release 17` ile derleme | Hoca JDK 17 kullanıyor olabilir | TAM |
| `.class` dosyası sızıntısı | Yönerge `.class` istemiyor | TAM, klasörde yok |
| Sır ve anahtar taraması | Yanlışlıkla anahtar yüklemek | TAM, temiz |
| ZIP içerik denetimi | Eksik dosya ile teslim | Yapılacak |
| Dosya adlarında Türkçe karakter | Bazı sistemlerde bozuluyor | TAM, adlar ASCII |
| UTF-8 kodlama | Türkçe karakterlerin bozulmaması | TAM, `-encoding UTF-8` yazılı |
| Rapor sayfa bütçesi | Yönerge 8–15 sayfa | Planda 12 sayfa ayrıldı |
| Para hesabında yuvarlama | `double` ile kuruş hatası | **AÇIK** aşağıda |
| Menüde 0 ile çıkış | Alışkanlık, hoca bekliyor | TAM |
| İsimlendirme tutarlılığı | Türkçe metot adları, tek biçim | TAM |

### Açık teknik konu: para `double`

Tutarlar `double` tutuluyor. `paraYaz` metodu kuruşa yuvarlıyor, ekranda sorun görünmüyor. Ama toplama işlemlerinde 0,01 kayması olabilir. Finalde iki seçenek var. Birincisi `long kurus` alanına geçmek, ikincisi `BigDecimal` kullanmak. İkincisi derste işlenmedi, birincisi daha savunulabilir. Karar hafta 13'te dosya yazımına geçerken verilmeli.

---

## 6. Açık riskler

| Risk | Etki | Önlem |
|---|---|---|
| Beş zorunlu gereksinimin finalde yetişmemesi | Kod puanı 60'tan 25'e düşer | Hafta 10–15 takvimi `04_Kalan_Isler_ve_Takvim` içinde, her hafta tek konu |
| ArrayList'e geçiş hafta 11, vize haftasına denk geliyor | Gecikme zinciri başlatır | Geçiş metot imzalarını değiştirmiyor, `ButceService` içi kapalı |
| Git deposu gönderilmedi | 1,5 puan kanıtsız kalır | Bugün gönderilecek |
| ZIP adında bölüm adı yok | Hoca dosyayı eşleştiremeyebilir | Bugün yeniden adlandırılacak |
| Sunumda "neden dizi kullandın" sorusu | Savunma zayıf görünür | Cevap hazır: hafta 8'de ArrayList işlenmedi, dizi bilinçli ve geçici |
| `instanceof` ile tür analizi | Hoca "kalıtım varken neden" diye sorabilir | Cevap: sayım için gerçek alt tip gerekiyor, `tip()` etiket için kullanılıyor |

---

## 7. Teslimden önce yapılacaklar

1. ZIP'i yönerge formatında yeniden adlandır: `Cengiz_Kilic_251205027_Yapay_Zeka_ve_Makine_Ogrenmesi.zip`
2. ZIP içeriğini aç ve kontrol et: `src` altında 8 `.java`, `.class` yok, PDF'ler açılıyor
3. Git deposunu uzak sunucuya gönder (ek puan kanıtı)
4. `javadoc -d javadoc src/model/*.java src/service/*.java src/app/*.java` çalıştır ve çıktıyı paketle
5. UZEM'e yükle, yükleme ekran görüntüsünü sakla
6. 17.00'den önce yüklendiğini teyit et, geç teslim her gün 10 puan

---

## 8. Sunum için hazır cevaplar

Sözlüde en çok sorulacak beş soru ve kısa cevabı.

| Soru | Cevap |
|---|---|
| Neden `Islem` soyut | Tek başına bir işlem anlamı taşımıyor. Gelir mi gider mi olduğunu alt sınıf biliyor, `butceEtkisi` bu yüzden soyut |
| Çok biçimlilik nerede | `ButceService` içindeki `Islem[]` dizisi. Diziye `Gelir` de `SabitGider` de giriyor, `butceEtkisi()` çağrısı doğru sınıfa gidiyor |
| Neden `ArrayList` değil dizi | Hafta 11'de işlendi, iskelet hafta 8 bilgisiyle yazıldı. Metot imzaları aynı kaldığı için geçiş tek sınıfı etkiliyor |
| `static sayac` neden | Her kaydın numarası kendi kendine oluşsun diye. Numara tutan ikinci bir liste gerekmiyor |
| Setter'da neden uyarı var, istisna yok | İstisna hafta 10'da geliyor. Şu an geçersiz değer eski değeri bozmuyor, program da çökmüyor |
