BLG205 NESNE TABANLI PROGRAMLAMAYA GIRIS
Kisisel Gelir-Gider ve Butce Takip Sistemi - Ara Teslim
Cengiz Kilic - 251205027 - Yapay Zeka ve Makine Ogrenmesi

1) ORTAM
   JDK    : 25 ile derlendi ve calistirildi. Kod 17 ve uzeri tum surumlerde derlenir
            (javac --release 17 ile de denendi, hata yok).
   IDE    : Zorunlu degil. Komut satiri yeterli. IntelliJ IDEA veya Eclipse ile
            proje kok dizini acilip src klasoru kaynak olarak gosterilebilir.

2) DERLEME
   cd 03_Iskelet_Kod
   javac -encoding UTF-8 -d build src/model/*.java src/service/*.java src/app/*.java

3) CALISTIRMA
   cd 03_Iskelet_Kod
   java -cp build app.Main

4) MENU
   1) Tum islemleri listele
   2) Butce ozeti
   3) Islem turu analizi
   4) Yeni gelir ekle
   5) Yeni gider ekle
   0) Cikis

5) ORNEK VERI
   Program acilirken Main.ornekVerileriYukle metodu alti kayit yukler, menu
   hemen denenebilir. Dosyadan okuma ve yazma hafta 13 konusu oldugu icin bu
   surumde yok, final surumunde data/islemler.txt eklenecek.

6) GITHUB DEPOSU (herkese acik)
   https://github.com/gecekargosu/blg205-butce-takip
   Depoda kaynak kodun commit gecmisi, UML ve rapor bulunur.
   Hoca kontrol icin dogrudan bu baglantidan inceleyebilir.

7) DEMO VIDEOSU
   Final tesliminde eklenecek 5-8 dakikalik ekran kaydi baglantisi buraya yazilacak.

8) PAKET ICERIGI
   00_ARA_TESLIM_OKU.txt    paket rehberi, yonerge maddelerinin karsiligi
   01_Ara_Rapor.pdf         ara rapor, on sayfa
   02_Ara_Teslim_UML/       UML sinif diyagrami (pdf, png, svg) + final plan sayfasi
   03_Iskelet_Kod/src/      sekiz java dosyasi, uc paket
   03_Iskelet_Kod/konsol-kayitlari/  programin gercek calisma ciktilari
   04_Kalan_Isler_ve_Takvim/ kalan isler, takvim, riskler
