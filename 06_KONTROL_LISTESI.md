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
| Git ve GitHub | Evet | **TAM** | Depo public, 8 commit: github.com/gecekargosu/blg205-butce-takip | 1,5 |
| Javadoc | Evet | **TAM** | `03_Iskelet_Kod/javadoc/` üretildi, 22 sayfa, 56 metoda açıklama yazıldı | 1,5 |
| Swing/JavaFX arayüz | Hayır | — | Kodu iki katına çıkarır | 0 |
| Thread | Hayır | — | Anlamsız kalır | 0 |
| Tasarım deseni | Hayır | — | Tek kişilik projede zorlama olur | 0 |

**En ucuz iki puan.** Javadoc üretildi ve Git deposu GitHub'a gönderildi, ikisi birlikte 3 puan, tek satır zorunlu kod yazmadan geldi.

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
| Git deposu gönderildi (16 Kasım, 8 commit) | Risk kapandı | Her hafta en az bir commit ile geçmiş canlı tutulacak |
| ZIP adında bölüm adı yok | Hoca dosyayı eşleştiremeyebilir | Bugün yeniden adlandırılacak |
| Sunumda "neden dizi kullandın" sorusu | Savunma zayıf görünür | Cevap hazır: hafta 8'de ArrayList işlenmedi, dizi bilinçli ve geçici |
| `instanceof` ile tür analizi | Hoca "kalıtım varken neden" diye sorabilir | Cevap: sayım için gerçek alt tip gerekiyor, `tip()` etiket için kullanılıyor |

---

## 7. Teslimden önce yapılacaklar

1. ZIP'i yönerge formatında yeniden adlandır: `Cengiz_Kilic_251205027_Yapay_Zeka_ve_Makine_Ogrenmesi.zip`
2. ZIP içeriğini aç ve kontrol et: `src` altında 8 `.java`, `.class` yok, PDF'ler açılıyor
3. Git deposunu uzak sunucuya gönder (16 Kasım'da yapıldı)
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

---

## 9. Teslim ZIP'i denetimi (16 Kasım, teslim öncesi)

Yönergenin 4.2 maddesi ara teslimde üç şey istiyor. 4.3 maddesi ise final ZIP'inin içeriğini
sayıyor. Bu iki madde karıştırılmamalı, çünkü ara teslimde `Rapor.pdf`, `Sunum.pptx` ve `data/`
klasörü istenmiyor.

| Yönerge maddesi | İstediği | ZIP'te var mı |
|---|---|---|
| 4.2 | UML sınıf diyagramı | Var, `02_Ara_Teslim_UML/` içinde pdf ve png |
| 4.2 | İskelet kod, derlenebilir ilk sürüm | Var, 8 java dosyası |
| 4.2 | Kalan işler ve iş bölümü planı | Var, `04_Kalan_Isler_ve_Takvim/` ve `00_ARA_TESLIM_OKU.txt` içinde iş bölümü |
| Teslim tablosu | Ara rapor | Var, `01_Kurgu_ve_Mimari_Tasarim.pdf` |

ZIP dışında bırakılanlar ve gerekçesi:

| Dosya | Neden dışarıda |
|---|---|
| `05_Rapor_Plani/` | Final raporunun iç planı, hocaya verilmez |
| `06_KONTROL_LISTESI` | Kendi denetim listemiz, eksikleri ve riskleri yazıyor |
| `07_PROJE_BAGLANTILARI` | Ders dışı projeler, teslimle ilgisi yok |
| `08_YAPILACAKLAR` | İç yol haritası, GitHub hatırlatması, strateji notları |
| `03_Iskelet_Kod/javadoc/` | Final aşamasının ek puanı, ara teslimde istenmiyor |
| `README.md` | `00_ARA_TESLIM_OKU.txt` aynı işi görüyor, tekrar olmasın |

Son hâl: 18 dosya, 1,17 MB. ZIP'in içinden çıkan kod ayrı bir klasöre açılıp `javac --release 17`
ile derlendi, hata yok ve program aynı çıktıyı verdi (net 26.820 TL).

## 10. Ek puan maddesindeki sayı

Yönergede "10+1" diye bir ifade yok. Belgede yazan iki satır şöyle:

- Değerlendirme tablosu, son satır: "Ek puan (bkz. Bölüm 7)" ve karşısında "+10'a kadar"
- 7. bölümün başlığı: "Ek Puan Getiren Çalışmalar", altında yedi kalem

Yani toplam puan 100, buna en fazla 10 ek puan ekleniyor. Üst sınır 110.
Belgede küçük bir numara hatası var, 2. bölümdeki bir cümle ek puan için "bkz. Bölüm 8" diyor,
oysa ek puan 7. bölümde. Bu bir yazım hatası, puanlamayı değiştirmiyor.

Yedi kalemin hepsi yapılsa bile tavan 10 puan olduğu için, en az kalemle tavana ulaşmak yeterli.
Biz dört kalemi hedefliyoruz, ikisi bugün tamamlandı.

---

## 11. Biçim denetimi (16 Kasım, ikinci tur)

| Kural | Önce | Sonra |
|---|---|---|
| Gövde 11-12 punto | 9,1 punto | **11 punto** |
| Satır aralığı 1,15 | karışık | **1,15** |
| Sayfa altı bilgi satırı | yok | **ders adı, proje adı, ad soyad, sayfa x / y** |
| Kapak | logolu, mühür alanı yok | **logo, tablo, mühür alanı var** |
| Grup numarası | yok | **"Bireysel proje" yazılı** |
| Sayfa sayısı 8-15 | 17 (sınır aşılıyordu) | **10 sayfa, 9 gövde** |
| Hatalı giriş ekranı | yok | **2 ekran eklendi** |

Rapor betiği `00_Kapak/rapor_uret.py` dosyasında. Yeniden üretmek için tek komut yeterli.
