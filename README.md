# Kişisel Gelir-Gider ve Bütçe Takip Sistemi

BLG205 Nesne Tabanlı Programlamaya Giriş — dönem projesi
Cengiz Kılıç, 251205027
İstanbul Rumeli Üniversitesi, Yapay Zekâ ve Makine Öğrenmesi

Konsol tabanlı, veritabanı kullanmayan, verisini metin dosyasında tutan bir bütçe takip uygulaması.
Saf Java, harici kütüphane yok.

**Depo:** https://github.com/gecekargosu/blg205-butce-takip

## Durum

| Aşama | Tarih | Durum |
|---|---|---|
| Ara teslim (UML + iskelet kod + takvim) | 16 Kasım 2026 | Tamamlandı |
| Final teslimi | 18 Aralık 2026 | Devam ediyor |
| Sunum | 23 Aralık 2026 | Bekliyor |

## Klasör yapısı

```
01_Kurgu_ve_Mimari_Tasarim.pdf   tasarım dosyası, 17 sayfa
02_Ara_Teslim_UML/               UML sınıf diyagramı, 2 sayfa
03_Iskelet_Kod/src/              java kaynak kodları
04_Kalan_Isler_ve_Takvim/        çalışma takvimi
05_Rapor_Plani/                  final raporunun iskeleti
```

## Derleme ve çalıştırma

```
cd 03_Iskelet_Kod
javac -encoding UTF-8 -d build src/model/*.java src/service/*.java src/app/*.java
java -cp build app.Main
```

## Sınıflar

`model` paketi: Islem (soyut), Gelir, Gider, SabitGider, Kategori, ButceHesabi
`service` paketi: ButceService
`app` paketi: Main

Kalıtım zinciri üç seviyeli: Islem → Gider → SabitGider.

## Tamamlanan özellikler

- Sekiz sınıf, üç paket, bütün alanlar private
- Doğrulamalı setter metotları, geçersiz değer eski değeri koruyor
- Otomatik sıra numarası için static sayaç
- Soyut sınıf ve iki soyut metot, alt sınıflarda ezilmiş
- Üst sınıf türünden dizi ile çok biçimlilik
- Menü, işlem listesi, bütçe özeti, işlem türü analizi
- Hatalı menü girişinde çökmeme

## Sıradaki özellikler

| Özellik | Hafta | Planlanan tarih |
|---|---|---|
| Gelir ve gider ekleme ekranları | 9-10 | 17-30 Kasım |
| Arayüz ve Comparable | 9 | 24-30 Kasım |
| Özel istisna ve try-catch | 10 | 24-30 Kasım |
| ArrayList, HashMap, Repository\<T\> | 11-12 | 1-7 Aralık |
| Dosya işlemleri | 13 | 1-7 Aralık |
| Lambda ve Stream raporları | 15 | 8-14 Aralık |
| JUnit testleri, Javadoc | 12 | 8-17 Aralık |

## Notlar

- Kod, dersin ilk sekiz haftasında işlenen konularla sınırlı tutuldu. Sonraki konular
  işlendikçe eklenecek, böylece sunumda her satır açıklanabiliyor.
- Yapay zekâdan taslak ve derleme kontrolü için destek alındı. Ayrıntı final raporunun
  10. bölümünde.
