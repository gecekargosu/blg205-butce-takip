# BLG205 — Hoca Ne İstedi, Bizde Var mı (Ara Teslim Denetimi)

Denetim tarihi: 16 Kasım 2026
Kaynak: `BLG205_NTP_Donem_Projesi_Yonergesi.docx` (192 satır, tamamı okundu)
Proje: Kişisel Gelir-Gider ve Bütçe Takip Sistemi · Cengiz Kılıç 251205027

Bu belge, yönergedeki her maddeyi tek tek kontrol eder. Her satırda "hoca ne istedi / bizde ne var / kanıt nerede" yazar.

---

## 1. Ara teslimin tanımı (Yönerge 4.2)

Hoca ara teslimde **üç** şey istiyor:

| # | İstenen | Durum | Kanıt |
|---|---------|-------|-------|
| 1 | UML sınıf diyagramı (sınıflar, alanlar, metotlar, erişim belirleyicileri, ilişkiler) | **VAR** | `02_Ara_Teslim_UML/` pdf + png. 8 sınıf, 3 paket, kalıtım okları işaretli |
| 2 | İskelet kod: sınıflar, kurucular, kalıtım hiyerarşisi, derlenebilir ilk sürüm | **VAR** | `03_Iskelet_Kod/src/` 8 `.java`. Bu denetimde `javac --release 17` ile yeniden derlendi: **0 hata** |
| 3 | Kalan işler ve iş bölümü planı | **VAR** | `04_Kalan_Isler_ve_Takvim/` (20 işlik takvim) + `08_YAPILACAKLAR.md` |

Ek olarak teslim tablosunda "ara raporu" da isteniyor: `01_Ara_Rapor.pdf` (10 sayfa, 9 gövde) ve `01_Kurgu_ve_Mimari_Tasarim.pdf` (17 sayfa) hazır.

**Ara teslim sonucu: 3/3 madde karşılandı.**

---

## 2. Zorunlu 8 teknik gereksinim (Yönerge Bölüm 3)

Hocanın tablosu, asgari beklenti ve bugünkü durum:

| # | Gereksinim | Asgari beklenti | Durum | Kanıt / eksik |
|---|-----------|-----------------|-------|----------------|
| 1 | Sınıflar, kapsülleme | ≥6 sınıf, private alanlar, setter doğrulaması, ≥1 static alan/metot | **TAM** | 8 sınıf. `Islem.sayac` static alan (satır 14), `Islem.getSayac` ve `Islem.paraYaz` static metot. Bütün alanlar `private` |
| 2 | Kalıtım | super çağrısı, override, `toString` | **TAM** | `Islem` → `Gelir`, `Islem` → `Gider` → `SabitGider` (üç seviye). `toString` üç sınıfta ezildi, `super.toString()` kullanılıyor |
| 3 | Soyut sınıf + çok biçimlilik | ≥1 abstract sınıf ve metot, üst türden liste üzerinde çağrı | **TAM** | `Islem` abstract (satır 12). `butceEtkisi()` ve `tip()` soyut. `ButceService` içinde `Islem[]` dizisi üzerinden çok biçimli çağrı |
| 4 | Arayüz + Comparable/Comparator | ≥1 interface, sıralama için Comparable/Comparator | **YOK** | Hafta 12 planında: `model/Raporlanabilir.java` + tarihe göre `Comparable` |
| 5 | İstisna yönetimi | ≥1 özel istisna sınıfı, try-catch, çökmeme | **KISMEN** | Çökmeme var (menüde hatalı giriş test edildi), ancak **özel istisna sınıfı ve try-catch yok**. Hafta 10 planında `exception/GecersizTutarException.java` |
| 6 | Koleksiyonlar | ArrayList ve HashMap temel yapı | **YOK** | Şu an `Islem[]` ve `Kategori[]` sabit diziler. Hafta 11 planında `ArrayList<Islem>` + `HashMap<String,Kategori>` |
| 7 | Dosya işlemleri | Açılışta okuma, kapanışta yazma, dosya yoksa çökmeme | **YOK** | Hafta 13 planında `repository/DosyaIslemleri.java`, `data/islemler.txt` |
| 8 | Lambda ve Stream | ≥2 farklı Stream işlemi | **YOK** | Hafta 15 planında `filter` + `sorted` + `collect` |

**Skor: 3 tam, 1 kısmen, 4 yok.**

Bu, ara teslim için normaldir: hoca "derlenebilen ilk sürüm" istiyor, 8 gereksinimin tamamını bugün istemiyor. Ancak 4–8 numaralı maddeler finalde toplam **40 puanlık** kod puanını taşıyor. Takvimde tarihleri var, risk burada.

---

## 3. Rapor yapısı (Yönerge Bölüm 5)

| Hocanın istediği başlık | Ara raporda | Not |
|---|---|---|
| Kapak: ders kodu/adı, proje adı, grup numarası, üye, tarih | **VAR** | Logo + mühür alanı + "Bireysel proje" satırı |
| Problem tanımı ve kullanım senaryoları | **VAR** | 1. bölüm |
| Sınıf tasarımı (UML + sorumluluklar) | **VAR** | 2. bölüm |
| NYP ilkelerinin uygulanması + eşleştirme tablosu | **VAR** | 3. bölüm, tablo hâlinde |
| İstisna yönetimi stratejisi | **KISMEN** | İstisna sınıfı hafta 10'da geleceği için strateji anlatıldı, kod yok |
| Dosya yapısı | **KISMEN** | Biçim planlandı, kod hafta 13 |
| Ekran görüntüleri (hatalı giriş dahil) | **VAR** | Hatalı giriş ekranları eklendi |
| Karşılaşılan sorunlar ve çözümler | **VAR** | 6. bölüm |
| İş bölümü tablosu | **VAR** | Bireysel, tek satır |
| Yapay zekâ beyanı ve kaynakça | **VAR** | 9. bölüm |
| 8–15 sayfa, 11–12 punto, 1,15 satır aralığı | **VAR** | 9 gövde sayfa, Times 11 punto, 1,15 |

---

## 4. Ek puan (Yönerge Bölüm 7, tavan +10)

| # | Kalem | Durum | Kanıt |
|---|-------|-------|-------|
| 1 | Swing/JavaFX arayüz | YOK | Planlanmadı (kodu iki katına çıkarır) |
| 2 | Generic sınıf (`Repository<T>`) | FINAL | Hafta 11 |
| 3 | Thread | YOK | Planlanmadı |
| 4 | JUnit ile ≥10 test | FINAL | Hafta 14 |
| 5 | Tasarım deseni | FINAL | Hafta 12 |
| 6 | Git/GitHub, düzenli commit | **TAM** | https://github.com/gecekargosu/blg205-butce-takip — PUBLIC, **8 commit** (bu denetimde doğrulandı) |
| 7 | Javadoc | **TAM** | `03_Iskelet_Kod/javadoc/`, 22 sayfa, 56 metot |

Bugün kesinleşen: Javadoc (≈1,5) + Git (≈1,5) = **~3 puan**.
Finalde hedeflenen: generic sınıf, JUnit, tasarım deseni → toplam ~7,5 puan.

---

## 5. Doğrulanan teknik kontroller (bu denetimde yeniden çalıştırıldı)

| Kontrol | Komut | Sonuç |
|---|---|---|
| Derleme | `javac -encoding UTF-8 --release 17 -d ...` | **0 hata**, 8 `.class` |
| ZIP içeriği | `unzip -l ...` | **8 `.java`**, **0 `.class`** (yönergeye uygun) |
| ZIP adı | — | `Cengiz_Kilic_251205027_Yapay_Zeka_ve_Makine_Ogrenmesi.zip`, yönerge formatına uygun |
| GitHub | `gh repo view` | PUBLIC, son push 16.11.2026, 8 commit |

---

## 6. Düzeltilmesi gerekenler (öncelik sırası)

| # | Sorun | Neden önemli | Yapılacak |
|---|-------|--------------|-----------|
| 1 | 4 zorunlu gereksinim (arayüz, istisna, koleksiyon, dosya, stream) finalde | Kod puanının %40'ı | Takvime bağlı kal, hafta 10–15 arası her hafta bir madde |
| 2 | `06_KONTROL_LISTESI.md` içinde "Git deposu gönderilmedi" satırı eski | Kendi denetim dosyamız yanlış bilgi veriyor | Düzeltildi (bu denetimle) |
| 3 | Para `double` | Toplamada 0,01 kayması | Hafta 13'te `long kurus` alanına geçiş |
| 4 | İstisna stratejisi raporu kod olmadan anlatılıyor | Hoca "nerede" diye soracak | Hafta 10'da kod + rapor birlikte güncellenecek |
| 5 | `Rapor.pdf`, `Sunum.pptx`, demo videosu | Final ZIP zorunluluğu | 15–18 Aralık |

---

## 7. Tek cümlelik sonuç

Ara teslim üç maddesinin **üçü de tamam**, kod `--release 17` ile hatasız derleniyor, ZIP ve GitHub kanıtları yerinde; eksik olan tek şey finalde kapatılacak 4 zorunlu gereksinim ve 3 ek puan kalemi, ikisinin de tarihi takvimde yazılı.
