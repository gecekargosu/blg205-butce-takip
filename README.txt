BLG205 NESNE TABANLI PROGRAMLAMAYA GİRİŞ
Kişisel Gelir Gider ve Bütçe Takip Sistemi, Ara Teslim
Cengiz Kılıç, 251205027, Yapay Zekâ ve Makine Öğrenmesi

1) ORTAM
   JDK    : 25 ile derlendi ve çalıştırıldı. Kod 17 ve üzeri tüm sürümlerde
            derlenir (javac --release 17 ile de denendi, hata yok).
   IDE    : Zorunlu değil, komut satırı yeterli. IntelliJ IDEA veya Eclipse
            ile proje kök dizini açılıp src klasörü kaynak olarak gösterilebilir.

2) DERLEME
   cd Kod
   javac -encoding UTF-8 -d build src/model/*.java src/service/*.java src/app/*.java

3) ÇALIŞTIRMA
   cd Kod
   java -cp build app.Main

4) MENÜ
   1) Tüm işlemleri listele
   2) Bütçe özeti
   3) İşlem türü analizi
   4) Yeni gelir ekle
   5) Yeni gider ekle
   6) Özet ayını seç (MM.yyyy)
   0) Çıkış

5) ÖRNEK VERİ
   Program açılırken Main.ornekVerileriYukle metodu altı kayıt yükler, menü
   hemen denenebilir. Dosyadan okuma ve yazma hafta 13 konusu olduğu için bu
   sürümde yoktur, final sürümünde data/islemler.txt eklenecektir.

6) KODLAMA
   Kaynak dosyalar ASCII tutulmuştur, böylece bölge ayarı ve konsol kodlaması
   farklı olan makinelerde derleme ve çıktı bozulmaz. Belgeler tam Türkçe
   karakter kullanır.

7) GITHUB DEPOSU
   https://github.com/gecekargosu/blg205-butce-takip
   Depoya herkes erişebilir. Depoda kaynak kodun commit geçmişi, UML ve
   rapor bulunur.

8) DEMO VİDEOSU
   Final tesliminde eklenecek 5-8 dakikalık ekran kaydı bağlantısı:
   (bağlantı final tesliminden önce buraya yazılacak)

9) PAKET İÇERİĞİ
   Rapor.pdf      ara rapor, 13 sayfa
   UML/           UML sınıf diyagramı, pdf (iki sayfa) ve png
   Kod/src/       sekiz java dosyası, üç paket
   Kod/javadoc/   sınıf ve metot belgeleri (index.html tarayıcıda açılır)
   Kalan_Isler/   kalan işler ve takvim, pdf
   README.txt     bu dosya
