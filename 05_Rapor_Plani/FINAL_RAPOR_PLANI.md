# Final Raporu Planı

Kişisel Gelir-Gider ve Bütçe Takip Sistemi
BLG205 Nesne Tabanlı Programlamaya Giriş
Cengiz Kılıç, 251205027
Final teslimi: 18 Aralık 2026 · Sunum: 23 Aralık 2026

Bu dosya raporun iskeleti. Her başlık için ne yazılacağı, hangi bilginin elimizde olduğu ve neyin Aralık'ta
doldurulacağı yazılı. Uydurma bölüm yok, henüz yapılmamış iş "ARALIK" olarak işaretli.

## Biçim kuralları (yönerge)

- 8-15 sayfa, kapak ve ekler hariç
- 11-12 punto, 1,15 satır aralığı
- Noktalı virgül kullanmıyoruz, cümleler nokta ile bitiyor
- Her bölümün başında bir paragraf giriş, sonra tablo veya kod parçası

## Sayfa bütçesi

| Bölüm | Sayfa | Durum |
|---|---|---|
| 1. Kapak | 1 | HAZIR (kapak düzeni elde var) |
| 2. Problem tanımı ve senaryolar | 2 | HAZIR (tasarım PDF'i bölüm 1) |
| 3. Sınıf tasarımı | 2,5 | HAZIR (UML + tasarım PDF'i bölüm 3-5) |
| 4. NYP ilkeleri | 3 | YARIM (ilkeler var, arayüz ve koleksiyon ARALIK) |
| 5. İstisna stratejisi | 1 | ARALIK (hafta 10'dan sonra) |
| 6. Dosya yapısı | 1 | ARALIK (hafta 13'ten sonra) |
| 7. Ekran görüntüleri | 2 | YARIM (3 ekran var, hatalı giriş ARALIK) |
| 8. Sorunlar ve çözümler | 1 | YARIM (5 madde hazır, yenileri eklenecek) |
| 9. İş bölümü | 0,5 | HAZIR (bireysel) |
| 10. Yapay zekâ beyanı ve kaynakça | 1 | HAZIR (taslak aşağıda) |
| **Toplam** | **15** | |

---

## 1. Kapak

Ders kodu ve adı, proje adı, grup numarası yerine "Bireysel proje", öğrenci bilgisi, teslim tarihi.
Fizik ödevi kapağındaki düzen kullanılacak, üniversite logosu aynı yerden alınacak.
Kapak altına proje deposu bağlantısı yazılacak, çünkü sürüm kontrolü ek puanında
hocanın commit geçmişini görmesi gerekiyor.

## 2. Problem Tanımı ve Kullanım Senaryoları

Kimler kullanır: öğrenci, maaşlı çalışan, burs alan kişi. Amaç: ay içinde para nereden geldi, nereye gitti,
aylık limit aşıldı mı sorularını tek ekranda cevaplamak.

Üç senaryo yazılacak, her biri numaralı adımlarla:

1. **Kayıt ekleme.** Kullanıcı menüden gelir seçer, tutarı ve tarihi girer, kategori seçer, kayıt listeye düşer.
2. **Bütçe kontrolü.** Kullanıcı bütçe özetini açar, toplam gider ile aylık limiti karşılaştırır, limit aşıldıysa uyarı görür.
3. **Dönem sonu.** Program kapanırken kayıtlar dosyaya yazılır, sonraki açılışta geri yüklenir.

Temel işlev listesi tasarım PDF'inin 1. bölümünden alınacak (yedi madde).

## 3. Sınıf Tasarımı

UML diyagramı tam sayfa olarak eklenecek. Sonra her sınıf için üç-dört satır:

| Sınıf | Sorumluluk |
|---|---|
| Islem | Gelir ve giderin ortak alanlarını tutar, bütçeye etkiyi soyut metotla alt sınıfa bırakır |
| Gelir | Gelire özgü kaynak alanı, bütçeye artı etki |
| Gider | Ödeme yöntemi ve zorunluluk, bütçeye eksi etki |
| SabitGider | Her ay tekrarlayan gider, ödeme günü |
| Kategori | İşlemin başlığı, kendi sıra numarasını üretir |
| ButceHesabi | Hesap sahibi, limit ve başlangıç bakiyesi |
| ButceService | İş mantığının tamamı, kayıt ekleme, toplamlar, analiz |
| Main | Sadece menü ve program döngüsü |

ARALIK: Repository\<T\>, Raporlanabilir, GecersizTutarException, DosyaIslemleri eklenecek.
UML'in ikinci sayfası bu dört sınıfı plan olarak gösteriyor.

## 4. NYP İlkelerinin Uygulanması

Her gereksinim için "nerede, neden" açıklaması ve beş-altı satırlık kod parçası.

### Gereksinim eşleştirme tablosu

| Gereksinim | Sınıf / Dosya | Açıklama | Durum |
|---|---|---|---|
| Sınıflar ve kapsülleme | model/Islem.java, Kategori.java | Sekiz sınıfın bütün alanları private, erişim getter ve setter ile | HAZIR |
| Doğrulamalı setter | model/Islem.java setTutar() | Sıfır ve eksi tutar reddediliyor, eski değer korunuyor | HAZIR (ARALIK: istisna fırlatacak) |
| Static alan/metot | model/Islem.java sayac, getSayac() | Her işleme otomatik sıra numarası | HAZIR |
| Kalıtım ve super | model/Gelir.java, Gider.java | super(...) ile ortak alanlar üst sınıftan dolduruluyor | HAZIR |
| Override | model/SabitGider.java tip() | Üst sınıfın etiketi değiştiriliyor | HAZIR |
| toString | model/Islem.java | Bütün model sınıflarında ezildi, liste tek satırla basılıyor | HAZIR |
| Soyut sınıf ve metot | model/Islem.java | butceEtkisi() ve tip() soyut, gövdesi alt sınıflarda | HAZIR |
| Çok biçimlilik | service/ButceService.java islemEkle() | Islem[] dizisi üzerinden Gelir, Gider, SabitGider birlikte | HAZIR |
| Arayüz | model/Raporlanabilir.java | İşlem kendi özet satırını üretiyor | ARALIK |
| Sıralama | model/Islem.java Comparable | Tarihe göre sıralama | ARALIK |
| Özel istisna | exception/GecersizTutarException.java | Eksi tutarda fırlatılıyor, menü yakalıyor | ARALIK |
| ArrayList | repository/Repository.java | Kayıtlar ArrayList içinde | ARALIK |
| HashMap | service/ButceService.java | Kategoriler ada göre HashMap'te | ARALIK |
| Dosya işlemleri | repository/DosyaIslemleri.java | TXT dosyasına yazma ve okuma | ARALIK |
| Lambda ve Stream | service/ButceService.java | Kategoriye göre filtre, tarihe göre sıralama, toplam | ARALIK |
| Generic sınıf (ek puan) | repository/Repository.java | Repository\<T\>, hem Islem hem Kategori için | ARALIK |

Kod parçaları: her satır için 5-8 satırlık gerçek kod, dosyadan birebir kopyalanacak.
Yorum satırları da rapora girecek, çünkü kodun neden yazıldığını onlar anlatıyor.

## 5. İstisna Yönetimi Stratejisi

ARALIK doldurulacak. Şimdiden öngörülen hatalar:

| Hata | Nerede yakalanacak | Kullanıcıya mesaj |
|---|---|---|
| Harf yerine sayı girilmesi | Main giriş metodu, try-catch | "Lütfen sayı girin" |
| Sıfır veya eksi tutar | setTutar, GecersizTutarException | "Tutar sıfırdan büyük olmalı" |
| Olmayan ödeme günü (40) | setOdemeGunu | "Gün 1 ile 31 arasında olmalı" |
| Menüde olmayan seçim | Main | "Menüdeki bir numarayı girin" |
| Boş açıklama | setAciklama | "Açıklama boş bırakılamaz" |
| Dosya bulunamadı | DosyaIslemleri | "Kayıt dosyası yok, boş listeyle başlandı" |

Şu an: ilk dördünün koruması var ama istisna ile değil, kontrol ile. Hafta 10'dan sonra try-catch'e çevrilecek.

## 6. Dosya Yapısı

ARALIK. Planlanan biçim, satır başına bir kayıt, ayırıcı noktalı virgül:

```
GELIR;1;32000.00;01.11.2026;Maas;Proje geliri;Serbest
SABIT;3;12500.00;05.11.2026;Kira;Ev kirasi;Havale;5
GIDER;5;2450.00;12.11.2026;Market;Market alisverisi;Kredi karti
```

Alanlar: tür, id, tutar, tarih, kategori, açıklama, son iki alan türe göre değişiyor.
Okurken tür alanına bakılıp doğru sınıf üretilecek, bu da çok biçimliliğin ikinci kullanım yeri.

## 7. Ekran Görüntüleri

HAZIR olanlar: ana menü, işlem listesi, bütçe özeti, işlem türü analizi (konsol çıktıları).
ARALIK: hatalı giriş ekranları, dosya yükleme mesajı, limit aşımı uyarısı.

Konsol çıktıları kutu içinde, Consolas yazı tipiyle, gri zemin üzerinde verilecek.

## 8. Karşılaşılan Sorunlar ve Çözümler

Hazır maddeler:

1. **Tutar alanında virgül sorunu.** Konsolda ondalık ayırıcı virgül olduğunda 12500,50 değeri bölünüyordu. Çözüm: para yazdırma işini `paraYaz()` metodu üstlendi, hesaplama double, gösterim metin.
2. **SabitGider'i gider sayma hatası.** `instanceof Gider` kontrolü önce yapıldığında sabit giderler de gider sayılıyordu. Çözüm: en alt sınıf önce kontrol ediliyor.
3. **Kurucuda doğrulama.** Setter kurucudan çağrıldığında Java "this-escape" uyarısı veriyor. Çözüm: uyarı kabul edildi, çünkü geçersiz değerin nesneye hiç girmemesi daha önemli.
4. **Menüde harf girilmesi.** `nextInt()` doğrudan istisna fırlatıyordu. Çözüm: `nextLine()` ile metin okunup `equals()` ile karşılaştırıldı.
5. **Türkçe karakter.** Konsol kodlaması UTF-8'e alınmadan çıktı bozuk görünüyordu. Çözüm: derleme `-encoding UTF-8`, çalıştırma `-Dfile.encoding=UTF-8`.

ARALIK: dosya ve koleksiyon aşamasında çıkacak sorunlar eklenecek.

## 9. Grup İçi İş Bölümü

Proje bireysel. Tablo tek satır olacak, uydurma üye yazılmayacak.

| Üye | Numara | Sorumlu olduğu sınıflar | Yaptığı işler |
|---|---|---|---|
| Cengiz Kılıç | 251205027 | Sekiz sınıfın tamamı | Tasarım, UML, kod, test, rapor, sunum |

Ayrıca iki-üç cümle: tasarım kararlarını kendim aldım, kodu satır satır açıklayabiliyorum, yapay zekâdan
taslak ve derleme kontrolü için destek aldım, nihai kodu kendim anlayıp düzenledim.

## 10. Yapay Zekâ Kullanım Beyanı ve Kaynakça

### Beyan taslağı

> Bu projede tasarım ve kod yazımı sırasında yapay zekâ araçlarından destek aldım. Desteği üç yerde kullandım.
> Birincisi sınıf yapısının ilk taslağını çıkarmak. İkincisi yazdığım kodun derlenip derlenmediğini kontrol etmek.
> Üçüncüsü rapor dili ve yazım düzeni. Taslakta yer alan vergi kesintisi, gecikme zammı ve kategori hedef limiti
> gibi işlevsiz özellikleri projeden çıkardım. Sınıf sayısını sekizde tuttum. Bütün metotları satır satır
> okuyup kendi cümlelerimle açıklayabildiğim biçimde sadeleştirdim. Kodun tamamının sorumluluğu bana aittir.

### Kaynakça

0. Proje deposu, https://github.com/gecekargosu/blg205-butce-takip (herkese açık)
1. BLG205 Nesne Tabanlı Programlamaya Giriş ders slaytları, hafta 1-15, İstanbul Rumeli Üniversitesi, 2026.
2. BLG205 dönem projesi yönergesi, 2026.
3. Oracle. *Java SE Documentation*, docs.oracle.com/javase.
4. Oracle. *Java Language Specification*, bölüm 8 (sınıflar) ve bölüm 11 (istisnalar).
5. Gamma, E. ve ark. *Design Patterns*, Addison-Wesley, 1994. (yalnızca kavram için başvuruldu, kodda desen kullanılmadı)

---

## Aralık'ta yapılacaklar listesi

- [ ] Arayüz ve Comparable eklenmesi, 4. bölümün tamamlanması
- [ ] İstisna sınıfı ve 5. bölüm
- [ ] ArrayList, HashMap, Repository\<T\>, 4. bölümün güncellenmesi
- [ ] Dosya işlemleri ve 6. bölüm
- [ ] Lambda ve Stream, rapor tabloları
- [ ] Ekran görüntülerinin yenilenmesi
- [ ] 8. bölüme yeni sorunların eklenmesi
- [ ] Kapak, sayfa numarası, içindekiler
- [ ] PDF çıktısı ve sayfa sayısı kontrolü (8-15 arası)
- [ ] GitHub deposunun herkese açık olduğunu kontrol et, bağlantıyı kapak ve kaynakçaya yaz
- [ ] Depoda düzenli commit geçmişi olduğunu doğrula (en az on beş commit, haftalık)
