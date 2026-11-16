# İskelet Kod — Ne Var, Ne Yok

Kişisel Gelir-Gider ve Bütçe Takip Sistemi, ara teslim sürümü.
Cengiz Kılıç, 251205027, BLG205.

## Derleme ve çalıştırma

```
cd 03_Iskelet_Kod
javac -encoding UTF-8 -d build src/model/*.java src/service/*.java src/app/*.java
java -cp build app.Main
```

JDK 25 ile derlendi ve çalıştırıldı. Kod Java 17 ve üzeri her sürümde derlenir,
çünkü dilin temel özelliklerinden başka bir şey kullanılmadı.

## Dosyalar

```
src/model/Islem.java        soyut üst sınıf, ortak alanlar, static id sayacı
src/model/Gelir.java        Islem'den türer, bütçeye artı etki eder
src/model/Gider.java        Islem'den türer, bütçeye eksi etki eder
src/model/SabitGider.java   Gider'den türer, ödeme günü tutar
src/model/Kategori.java     kategori adı ve tipi, static id sayacı
src/model/ButceHesabi.java  sahip, öğrenci no, aylık limit, başlangıç bakiyesi
src/service/ButceService.java  iş mantığı, Islem[] dizisi, toplamlar, analiz
src/app/Main.java           menü, örnek veriler, program döngüsü
```

## Bu sürümde çalışanlar

- Menü açılıyor ve kapanana kadar dönüyor.
- Altı örnek kayıt açılışta yükleniyor.
- İşlemleri listeleme, bütçe özeti ve işlem türü analizi çalışıyor.
- Yeni gelir ve yeni gider ekleme ekranları çalışıyor (menü 4 ve 5), hatalı girişte
  kayıt eklenmiyor ve menüye dönülüyor.
- Kalıtım zinciri kurulu, `butceEtkisi()` ve `tip()` alt sınıflarda ezilmiş durumda.
- `Islem[]` dizisi üzerinden gelir, gider ve sabit gider birlikte tutuluyor,
  yani çok biçimlilik gerçekten kullanılıyor.
- Setter'larda geçerlilik kontrolü var, geçersiz değer eskisini koruyor.
- Menüde harf girilirse program çökmüyor, uyarı verip menüye dönüyor.

## Bu sürümde bilerek olmayanlar

| Konu | Neden yok | Ne zaman gelecek |
|---|---|---|
| Arayüz | Hafta 9 konusu, henüz işlenmedi | 24-30 Kasım |
| Özel istisna, try-catch | Hafta 10 konusu | 24-30 Kasım |
| ArrayList, HashMap | Hafta 11 konusu | 1-7 Aralık |
| Dosya işlemleri | Hafta 13 konusu | 1-7 Aralık |
| Lambda, Stream | Hafta 15 konusu | 8-14 Aralık |

Bu konular derste işlendikten sonra eklenecek. Sıra bu şekilde çünkü sunumda
her satırı anlatabilmem gerekiyor.

## Ekran görüntüsü

```
=======================================================
     KISISEL GELIR GIDER VE BUTCE TAKIP SISTEMI
=======================================================
1) Tum islemleri listele
2) Butce ozeti
3) Islem turu analizi
4) Yeni gelir ekle
5) Yeni gider ekle
0) Cikis
Seciminiz: 2
------------------- BUTCE OZETI -------------------
Hesap            : Cengiz Kilic 251205027
Baslangic bakiye :   +5000.00 TL
Toplam gelir     :  +38000.00 TL
Toplam gider     :  -16180.00 TL
Net bakiye       :  +26820.00 TL
Aylik limit      :   25000.00 TL
Limit durumu     : Sinir asilmadi
```
