# Yapılacaklar Listesi

Kişisel Gelir-Gider ve Bütçe Takip Sistemi · BLG205
Cengiz Kılıç 251205027
Son güncelleme: 16 Kasım 2026, saat 05.30

Bu dosya tek doğru kaynak. Eski konuşmalara bakmak yerine buraya bak.
Her madde işaretlenebilir, her maddenin tarihi ve çıktısı yazılı.

---

## ⚠️ UNUTMA: GitHub'a yüklenecek

Proje bitince ders projesi GitHub'a yüklenecek. Depo adı ve adresi şimdiden belli:

**Depo:** https://github.com/gecekargosu/blg205-butce-takip
**Görünürlük:** Herkese açık (hoca commit geçmişini görecek)
**Not:** Adres `05_Rapor_Plani/FINAL_RAPOR_PLANI.md` kaynakçasında ve kapakta yazılı.

Cengiz, bunu bana hatırlat. Yükleme yapılmadan ek puanın 1,5 puanı sayılmaz.

---

## 1. Bugün, 16 Kasım — ara teslim (17.00)

| # | İş | Çıktı | Durum |
|---|---|---|---|
| 1 | ZIP içindeki 7 gereksiz dosyayı çıkar | temiz ZIP | Bekliyor |
| 2 | ZIP'i yeniden paketle, adı yönergeye uysun | `Cengiz_Kilic_251205027_Yapay_Zeka_ve_Makine_Ogrenmesi.zip` | Ad düzeltildi, içerik bekliyor |
| 3 | ZIP'i aç, 8 java dosyası var mı gör, `.class` yok mu gör | kontrol notu | Bekliyor |
| 4 | UZEM'e yükle, yükleme ekranını görüntüle | ekran görüntüsü | Bekliyor |
| 5 | Javadoc üret (`javadoc -d javadoc ...`) | `javadoc/` klasörü | Bekliyor |
| 6 | Kodun son hâlini Git'e commit et | commit | Yapıldı, 3 commit var |

Çıkarılacak dosyalar: `uml_plan.zip`, `uml_uret.py`, `uml_plan.py`, `takvim_uret.py`, `uml_baski.html`, `uml_plan.html`.

---

## 2. 17–23 Kasım — kullanıcı girişli ekran

| # | İş | Çıktı | Durum |
|---|---|---|---|
| 7 | Gelir ve gider ekleme ekranı (menüye 2 yeni seçenek) | kullanıcıdan veri alan menü | Bekliyor |
| 8 | Kategori seçimi, tarih doğrulaması | doğrulanmış giriş | Bekliyor |
| 9 | Yeni ekranların konsol görüntüleri | 3-4 ekran | Bekliyor |

Not: Bu adım istisna yönetiminden önce geliyor çünkü kullanıcıdan sayı okumak zaten hata üretiyor. Hataları görüp bir sonraki hafta try-catch ile çözmek daha anlaşılır olur.

---

## 3. 24–30 Kasım — arayüz ve istisna

| # | İş | Çıktı | Durum |
|---|---|---|---|
| 10 | `model/Raporlanabilir.java` arayüzü, `ozetSatiri()` | arayüz | Bekliyor |
| 11 | `exception/GecersizTutarException.java` | özel istisna | Bekliyor |
| 12 | Menü girişlerini try-catch'e çevir | çökmeyen program | Bekliyor |
| 13 | Setter'ları istisna fırlatacak şekilde düzenle | doğrulama | Bekliyor |
| 14 | Rapor 4. ve 5. bölümü doldur | rapor taslağı | Bekliyor |

Bu hafta 8 zorunlu gereksinimden 2 tanesi kapanıyor: arayüz ve istisna.

---

## 4. 1–7 Aralık — koleksiyonlar ve dosya

| # | İş | Çıktı | Durum |
|---|---|---|---|
| 15 | `Islem[]` yerine `ArrayList<Islem>` | güncellenmiş servis | Bekliyor |
| 16 | Kategoriler için `HashMap<String, Kategori>` | hızlı arama | Bekliyor |
| 17 | `repository/Repository.java` generic sınıf | `Repository<T>` | Bekliyor |
| 18 | `repository/DosyaIslemleri.java`, TXT yazma ve okuma | `data/islemler.txt` | Bekliyor |
| 19 | Dosya yoksa programın çökmemesi | ilk açılış testi | Bekliyor |
| 20 | UML'i güncelle, yeni sınıfları diyagrama işle | UML v2 | Bekliyor |

Bu hafta 3 zorunlu gereksinim kapanıyor: koleksiyonlar, dosya işlemleri. Bir de ek puanın generic sınıfı.

---

## 5. 8–14 Aralık — sıralama, stream, testler

| # | İş | Çıktı | Durum |
|---|---|---|---|
| 21 | `Comparable` ile tarihe göre sıralama | sıralı liste | Bekliyor |
| 22 | Lambda ve Stream: `filter`, `sorted`, `collect`, `mapToDouble` | rapor ekranı | Bekliyor |
| 23 | JUnit 5 ile en az 10 birim testi | test sınıfları | Bekliyor |
| 24 | Hatalı giriş testleri, tutanak | test tutanağı | Bekliyor |
| 25 | Javadoc'u yenile | `javadoc/` | Bekliyor |

Bu hafta son zorunlu gereksinim kapanıyor: lambda ve Stream. Yani 8/8 tamam.

---

## 6. 15–18 Aralık — teslim

| # | İş | Çıktı | Durum |
|---|---|---|---|
| 26 | Final raporu (8-15 sayfa, 10 bölüm) | `Rapor.pdf` | Bekliyor |
| 27 | Sunum dosyası | `Sunum.pptx` | Bekliyor |
| 28 | Demo videosu (5-8 dakika) | video bağlantısı | Bekliyor |
| 29 | Final ZIP: src, data, README.txt, UML, Rapor.pdf, Sunum.pptx | teslim paketi | Bekliyor |
| 30 | GitHub'a yükle, bağlantıyı rapora yaz | public depo | **Bekliyor** |
| 31 | UZEM'e yükle (18 Aralık 17.00) | yükleme kanıtı | Bekliyor |

---

## 7. Ek puan — 10 puanın tamamı hedefte

Yönergede 7 kalem var, tavan 10 puan. Hepsi şart değil ama hedefimiz tavan.
Ucuzdan pahalıya sıraladım, önce garantili puanları alıyoruz.

| # | Kalem | Ne yapılacak | Ne zaman | Puan | Zorluk |
|---|---|---|---|---|---|
| E1 | Javadoc | `javadoc` komutu, `docs/` klasörü, raporda ekran görüntüsü | **Bugün** | ~1,5 | Kolay |
| E2 | Git ve GitHub | Depo herkese açık, haftalık commit, en az 15 commit | **Bugün başla** | ~1,5 | Kolay |
| E3 | Generic sınıf | `Repository<T>`, hem `Islem` hem `Kategori` için | 1-7 Aralık | ~1,5 | Orta |
| E4 | JUnit 5 | En az 10 test: tutar, limit, doğrulama, dosya | 8-13 Aralık | ~1,5 | Orta |
| E5 | Tasarım deseni | `Singleton` (Repository erişimi) veya `Observer` (limit uyarısı) | 8-14 Aralık | ~1,5 | Orta |
| E6 | Thread | Arka planda otomatik yedekleme, her 60 saniyede dosyaya yaz | 8-14 Aralık | ~1,5 | Zor |
| E7 | Swing arayüzü | Ayrı `gui/` paketi, konsol bozulmadan yanına | 8-14 Aralık | ~1,5 | Zor |

**Sıra mantığı:** E1 ve E2 bugün bedava. E3 ve E4 zaten zorunlu gereksinimlerin içinde geliyor, ayrı iş değil. E5 küçük bir sınıf. E6 ve E7 kodu büyütür, en sona bırakıldı.

**Risk notu:** E7 (Swing) kodu iki katına çıkarır ve sunumda "bunu sen mi yazdın" sorusu gelir. E6 (thread) tek kişilik projede zorlama durur. İkisini de Aralık'ta, zorunlu 8 gereksinim bittikten sonra yapıyoruz. Yetişmezse E1-E5 bize 7,5 puana kadar getirir.

---

## 8. Verilmiş kararlar — tekrar tartışmıyoruz

| Karar | Gerekçe |
|---|---|
| İskelet kod hafta 8 konularıyla sınırlı | Sunumda her satırı açıklayabilmek |
| `ArrayList` yerine dizi (şimdilik) | Hafta 11'de işlenecek, 1-7 Aralık'ta geçilecek |
| UML iki sayfa | Sayfa 1 mevcut kod, sayfa 2 finalde eklenecek dört sınıf |
| Metinlerde noktalı virgül yok | Hocaların en çok dikkat ettiği ayrıntı |
| 8 sınıf, fazlası yok | Sınıf sayısı değil sorumluluk netliği puan getiriyor |
| Para `double`, ekranda kuruşa yuvarlanıyor | Aralık'ta `long kurus`'a geçiş değerlendirilecek |
| Proje bireysel | İş bölümü tablosu tek satır, uydurma üye yok |

---

## 9. Benim sana hatırlatacaklarım

- [ ] Proje bitince GitHub'a yükle (30. madde)
- [ ] ZIP'i UZEM'e yükle, ekran görüntüsünü sakla
- [ ] Javadoc'u bugün üret, 15 dakika
- [ ] Her hafta en az bir commit at, hoca geçmişe bakacak
- [ ] 8 zorunlu gereksinim bitince UML'i güncelle
- [ ] Sunumdan önce kendi kodunu baştan sona bir kez yüksek sesle anlat

---

## 10. Nerede ne var

| Dosya | İçerik |
|---|---|
| `00_ARA_TESLIM_OKU.txt` | Teslim paketinin rehberi |
| `01_Kurgu_ve_Mimari_Tasarim.pdf` | 17 sayfalık tasarım dosyası |
| `02_Ara_Teslim_UML/` | UML iki sayfa, png, svg |
| `03_Iskelet_Kod/src/` | 8 java dosyası |
| `04_Kalan_Isler_ve_Takvim/` | 20 işlik takvim, xlsx |
| `05_Rapor_Plani/FINAL_RAPOR_PLANI.md` | Raporun 10 bölümü, sayfa bütçesi, yapay zekâ beyanı |
| `06_KONTROL_LISTESI.md` | Yönerge uyumu ve eksikler |
| `07_PROJE_BAGLANTILARI.md` | GitHub bağlantıları |
| `08_YAPILACAKLAR.md` | Bu dosya |
