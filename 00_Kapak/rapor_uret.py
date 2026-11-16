"""Ara rapor PDF ureteci.

Kapak + govde HTML uretir, Chrome ile A4 PDF basar, sonra reportlab ile
her sayfaya altbilgi (ders adi, proje adi, sayfa numarasi) ekler.
Govde metni 11 punto, satir araligi 1,15.
"""
import os, subprocess, sys, html
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
LOGO = KOK / "00_Kapak/assets/image1.png"
UML = KOK / "02_Ara_Teslim_UML/UML_Sinif_Diyagrami.png"
KAYIT = KOK / "03_Iskelet_Kod/konsol-kayitlari"
CIKTI = KOK / "01_Ara_Rapor.pdf"


def konsol(ad, bas=0, son=99):
    """Konsol kaydini okur, satir araligini secer, HTML icin kacar."""
    yol = KAYIT / ad
    if not yol.exists():
        return "(kayit bulunamadi)"
    satirlar = yol.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n").split("\n")
    secili = satirlar[bas:son]
    return html.escape("\n".join(secili).rstrip())


CSS = """
@page { size: A4; margin: 22mm 18mm 26mm 18mm; }
* { box-sizing: border-box; }
body { font-family: 'Calibri', 'Segoe UI', Arial, sans-serif; font-size: 11pt;
       line-height: 1.15; color: #111; margin: 0; }
h1 { font-size: 15pt; margin: 0 0 8pt 0; padding-bottom: 4pt; border-bottom: 1.5pt solid #8b1a1a; }
h2 { font-size: 12.5pt; margin: 14pt 0 5pt 0; color: #8b1a1a; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 10pt 0 4pt 0; }
p { margin: 0 0 6pt 0; text-align: justify; }
ul, ol { margin: 0 0 6pt 0; padding-left: 16pt; }
li { margin-bottom: 2pt; }
table { border-collapse: collapse; width: 100%; font-size: 10pt; margin: 5pt 0 8pt 0; }
th, td { border: 0.75pt solid #888; padding: 3.5pt 5pt; vertical-align: top; }
th { background: #f0e6e6; font-weight: bold; text-align: left; }
code { font-family: Consolas, monospace; font-size: 9.5pt; background: #f4f4f4; padding: 0 2pt; }
pre { font-family: Consolas, monospace; font-size: 8.2pt; line-height: 1.25; background: #1e1e1e;
      color: #e8e8e8; padding: 6pt 8pt; border-radius: 3pt; white-space: pre-wrap;
      margin: 4pt 0 9pt 0; page-break-inside: avoid; }
pre .y { color: #7ec699; }
.ekran { border: 0.75pt solid #bbb; background: #fafafa; padding: 6pt 8pt; margin: 4pt 0 10pt 0;
         font-family: Consolas, monospace; font-size: 8.2pt; line-height: 1.28; white-space: pre-wrap;
         page-break-inside: avoid; }
.girdi { font-size: 8.8pt; font-weight: normal; color: #555; font-family: Consolas, monospace; }
.altbilgi-not { font-size: 9pt; color: #555; font-style: italic; margin-top: -4pt; margin-bottom: 10pt; }
.sayfa { page-break-after: always; }
.kapak { text-align: center; height: 245mm; position: relative; }
.kapak img.logo { width: 50mm; margin-top: 2mm; }
.kapak .ust { font-size: 13.5pt; font-weight: bold; letter-spacing: 0.3pt; margin-top: 4mm; }
.kapak .uni { font-size: 15pt; font-weight: bold; margin-top: 6mm; }
.kapak .fak { font-size: 13.5pt; font-weight: bold; margin-top: 2mm; }
.kapak .ders { font-size: 13.5pt; font-weight: bold; margin-top: 6mm; }
.kapak .proje { font-size: 16pt; font-weight: bold; margin-top: 10mm; line-height: 1.25; }
.kapak .alt { font-size: 11pt; margin-top: 4mm; font-style: italic; }
.kapak table { width: 148mm; margin: 12mm auto 0 auto; font-size: 11pt; }
.kapak td { border: none; padding: 1.6pt 3pt; text-align: left; }
.kapak td.b { font-weight: bold; width: 34mm; }
.kapak td.i { width: 4mm; }
.muhur { position: absolute; bottom: 0; left: 0; right: 0; }
.muhur .kutu { width: 46mm; height: 26mm; border: 0.75pt dashed #999; margin: 0 auto;
               display: flex; align-items: center; justify-content: center; color: #999;
               font-size: 8.5pt; }
"""


def konsol_blok(ad, bas, son):
    """Konsol kaydindan isaretlere gore blok cikarir, HTML icin kacislar."""
    satirlar = (KAYIT / ad).read_text(encoding="utf-8", errors="replace").splitlines()
    i = None
    for k, satir in enumerate(satirlar):
        if bas in satir:
            i = k
            break
    if i is None:
        raise SystemExit("blok baslangici yok: %s / %s" % (ad, bas))
    j = i
    while j > 0 and not satirlar[j].startswith("Seciminiz:"):
        j -= 1
    k = len(satirlar) - 1
    for m in range(i, len(satirlar)):
        if son in satirlar[m]:
            k = m
            break
    return html.escape("\n".join(satirlar[j:k + 1]).strip())


def kapak():
    return f"""
<div class="kapak">
  <img class="logo" src="file:///{LOGO.as_posix()}">
  <div class="uni">İSTANBUL RUMELİ ÜNİVERSİTESİ</div>
  <div class="fak">MÜHENDİSLİK VE DOĞA BİLİMLERİ FAKÜLTESİ</div>
  <div class="fak">YAPAY ZEKÂ VE MAKİNE ÖĞRENMESİ BÖLÜMÜ</div>
  <div class="ders">BLG205 NESNE TABANLI PROGRAMLAMAYA GİRİŞ</div>
  <div class="proje">Kişisel Gelir Gider ve<br>Bütçe Takip Sistemi</div>
  <div class="alt">Dönem Projesi · Ara Teslim Raporu</div>
  <table>
    <tr><td class="b">Adı Soyadı</td><td class="i">:</td><td>Cengiz KILIÇ</td></tr>
    <tr><td class="b">Öğrenci No</td><td class="i">:</td><td>251205027</td></tr>
    <tr><td class="b">Bölümü</td><td class="i">:</td><td>Yapay Zekâ ve Makine Öğrenmesi</td></tr>
    <tr><td class="b">Ders</td><td class="i">:</td><td>BLG205 Nesne Tabanlı Programlamaya Giriş</td></tr>
    <tr><td class="b">Öğretim Üyesi</td><td class="i">:</td><td>Doç. Dr. Aykut Diker</td></tr>
    <tr><td class="b">Grup No</td><td class="i">:</td><td>— (bireysel proje)</td></tr>
    <tr><td class="b">Proje Türü</td><td class="i">:</td><td>Bireysel proje</td></tr>
    <tr><td class="b">Teslim Tarihi</td><td class="i">:</td><td>16.11.2026</td></tr>
  </table>
  <div class="muhur"><div class="kutu">mühür / kaşe</div></div>
</div>
<div class="sayfa"></div>
"""


def govde():
    e_menu = konsol_blok("e.txt", "1) Tum islemleri listele", "0) Cikis")
    e_liste = konsol_blok("e.txt", "------- KAYITLI ISLEMLER", "Toplam kayit:")
    e_ozet = konsol_blok("e.txt", "BUTCE OZETI", "Limit durumu")
    e_analiz = konsol_blok("e.txt", "ISLEM TURU ANALIZI", "Toplam")
    a_ekle = konsol_blok("a.txt", "YENI GELIR", "Kayit eklendi")
    d_ekle = konsol_blok("d.txt", "YENI GIDER", "Kayit eklendi")
    b_hata = konsol_blok("b.txt", "YENI GELIR", "Hata: tutar")
    c_hata = konsol_blok("c.txt", "YENI GIDER", "Hata: boyle bir kategori")

    return f"""
<h1>1. Problem Tanımı ve Kullanım Senaryoları</h1>
<p>Bir öğrencinin ya da maaşlı çalışanın ay içinde parasının nereden geldiğini ve nereye gittiğini
takip etmesi, çoğu zaman dağınık notlar ve banka uygulamaları arasında kaybolur. Bu proje, tek bir
konsol uygulaması üzerinden gelir ve giderleri kaydetmeyi, ay sonunda toplam geliri, toplam gideri ve
net bakiyeyi tek ekranda görmeyi, ayrıca belirlenen aylık limitin aşılıp aşılmadığını anında öğrenmeyi
amaçlar.</p>
<p>Uygulama üç kişi grubu için tasarlandı. Birincisi burs ve aile desteğiyle geçinen öğrenci, ikincisi
maaş ve ek gelirle geçinen çalışan, üçüncüsü kira ve fatura gibi her ay tekrarlayan giderleri takip
etmek isteyen kişi. Veritabanı kullanılmaz, kayıtlar metin dosyasında tutulacaktır. Harici kütüphane
kullanılmamıştır, program yalnızca standart Java sınıflarıyla çalışır.</p>

<h2>1.1 Kullanım senaryoları</h2>
<p><b>Senaryo 1, kayıt ekleme.</b> Kullanıcı menüden 4 numarayı seçer. Ekrana kategori listesi gelir,
ardından açıklama, tutar, tarih, kategori ve kaynak sorulur. Tutar sayı değilse ya da kategori listede
yoksa kayıt eklenmez ve kullanıcı menüye döner. Geçerli girişte kayıt listeye eklenir ve numarası
bildirilir.</p>
<p><b>Senaryo 2, bütçe kontrolü.</b> Kullanıcı 2 numarayı seçer. Başlangıç bakiyesi, toplam gelir,
toplam gider, net bakiye ve aylık limit alt alta yazılır. Toplam gider limiti geçtiyse ekranda
"Sinir asildi" uyarısı çıkar.</p>
<p><b>Senaryo 3, dönem sonu.</b> Program kapatılırken kayıtlar dosyaya yazılacak, sonraki açılışta geri
yüklenecektir. Bu adım hafta 13 konusu olduğu için ara teslimde henüz yoktur, örnek kayıtlar program
açılırken belleğe yüklenmektedir.</p>

<h2>1.2 Temel işlevler</h2>
<p>Program yedi temel işlevi yerine getirir. Gelir kaydı ekleme, gider kaydı ekleme, kayıtları
listeleme, bütçe özeti çıkarma, işlem türüne göre sayım, aylık limit kontrolü ve kayıtların kalıcı
olarak saklanması. Bu yedi işlevden ilk altısı ara teslimde çalışır durumdadır. Limit kontrolü bütçe
özetinin içinde yapılır. Kalıcı saklama hafta 13 konusu olduğu için sonraki sürümde eklenecektir.</p>

<h2>1.3 Kapsam ve sınırlar</h2>
<p>Program tek kullanıcı içindir, çok kullanıcılı bir yapı hedeflenmemiştir. Veritabanı ve harici
kütüphane kullanılmaz. Arayüz konsol tabanlıdır, grafik arayüz yönergede zorunlu tutulmadığı için
tercih edilmemiştir. Para birimi Türk lirasıdır, tutarlar kuruş duyarlılığında gösterilir. Tarih alanı
metin olarak tutulur ve gg.aa.yyyy biçimindedir, tarih aritmetiği bu sürümde yapılmaz.</p>

<h1>2. Sınıf Tasarımı</h1>
<p>Sekiz sınıf üç pakete ayrıldı. Model paketi veriyi, servis paketi iş mantığını, uygulama paketi
yalnızca menüyü tutar. İş mantığının tamamı tek sınıfta toplandığı için ana sınıfta hesap kodu yoktur.</p>
<table>
<tr><th style="width:34mm">Sınıf</th><th>Sorumluluk</th></tr>
<tr><td>Islem</td><td>Gelir ve giderin ortak alanlarını tutan soyut üst sınıf. Bütçeye etkiyi hesaplayan
<code>butceEtkisi()</code> ve ekranda görünen etiketi veren <code>tip()</code> soyuttur, gövdesi alt
sınıflarda. Otomatik numara için <code>static sayac</code> alanı vardır.</td></tr>
<tr><td>Gelir</td><td>Islem'den türer. Kaynak alanı gelir türüne özgüdür. Bütçeye artı yönde etki eder.</td></tr>
<tr><td>Gider</td><td>Islem'den türer. Ödeme yöntemi ve zorunlu olup olmadığı bilgisini tutar. Bütçeye eksi
yönde etki eder.</td></tr>
<tr><td>SabitGider</td><td>Gider'den türer, yani kalıtım üç seviyedir. Her ay tekrarlayan giderlerde
ödeme gününü tutar, ekranda "Sabit Gider" etiketiyle görünür.</td></tr>
<tr><td>Kategori</td><td>İşlemin başlığını ve gelir mi gider mi olduğunu tutar. Kendi numarasını static
sayaçla üretir.</td></tr>
<tr><td>ButceHesabi</td><td>Hesap sahibi, öğrenci numarası, aylık limit ve başlangıç bakiyesi. Limit
aşımını <code>limitAsildiMi()</code> metodu bildirir.</td></tr>
<tr><td>ButceService</td><td>İş mantığının tamamı. Kayıt ekleme, kategori arama, listeleme, toplam gelir,
toplam gider, net bakiye, limit kontrolü ve tür analizi burada.</td></tr>
<tr><td>Main</td><td>Menü, kullanıcıdan veri okuma ve program döngüsü. Hesaplama yapmaz.</td></tr>
</table>
<p class="altbilgi-not">UML sınıf diyagramı, alanların ve metotların erişim belirleyicileriyle birlikte
ekte ve ayrı dosyada verilmiştir.</p>
<h2>2.1 Tasarım gerekçeleri</h2>
<p><b>Neden soyut üst sınıf.</b> Gelir ve gider aynı alanların çoğunu paylaşır, ama tek başına bir
"işlem" nesnesi anlam taşımaz. Bir kaydın bütçeye artı mı eksi mi etki ettiğini ancak alt sınıf bilir.
Bu yüzden <code>Islem</code> soyuttur ve <code>butceEtkisi()</code> gövdesiz bırakılmıştır.</p>
<p><b>Neden ayrı servis sınıfı.</b> Yönerge, iş mantığını tek sınıfta toplayan projelere tasarım puanı
vermiyor. Bu nedenle toplama, sayma ve limit kontrolü <code>ButceService</code> içinde, menü ve veri
okuma <code>Main</code> içinde tutuldu. Ana sınıfta tek satır hesap yoktur.</p>
<p><b>Neden static sayaç.</b> Her kaydın numarası kendi kendine oluşsun istedim. Numarayı dışarıda
tutan ikinci bir liste yerine sınıfın kendi sayacı kullanıldı. Böylece kayıt nereden eklenirse eklensin
numara çakışmaz.</p>
<p><b>Neden SabitGider ayrı sınıf.</b> Kira ve fatura her ay tekrarlar, market harcaması tekrarlamaz.
Tekrarlayan giderin ödeme günü vardır. Bu ayrımı alan olarak tutmak yerine kalıtımla yapmak, ileride
otomatik tahakkuk özelliği eklendiğinde işi kolaylaştıracak.</p>

<h2>2.2 Paket yapısı</h2>
<table>
<tr><th style="width:30mm">Paket</th><th style="width:52mm">Sınıflar</th><th>Görevi</th></tr>
<tr><td>model</td><td>Islem, Gelir, Gider, SabitGider, Kategori, ButceHesabi</td><td>Veriyi ve doğrulamayı
tutar. Ekrana yazma biçimi toString içinde.</td></tr>
<tr><td>service</td><td>ButceService</td><td>İş mantığının tamamı. Toplama, sayma, arama, limit
kontrolü.</td></tr>
<tr><td>app</td><td>Main</td><td>Menü, kullanıcıdan veri okuma, program döngüsü.</td></tr>
</table>

<img src="file:///{UML.as_posix()}" style="width:100%; border:0.75pt solid #ccc">

<h1>3. NYP İlkelerinin Uygulanması</h1>
<p>Aşağıdaki tablo, yönergenin üçüncü bölümündeki sekiz gereksinimi kodda hangi sınıfın karşıladığıyla
birlikte gösterir. Ara teslimde sekiz gereksinimden üçü karşılanmış, biri kısmen karşılanmış
durumdadır. Kalan dördü, derste ilgili konu işlendikten sonra eklenecektir. Bu tablo, yönergenin
beşinci bölümünde istenen <b>gereksinim eşleştirme tablosudur</b>.</p>
<table>
<tr><th style="width:40mm">Gereksinim</th><th style="width:40mm">Sınıf / Dosya</th><th>Açıklama</th><th style="width:16mm">Durum</th></tr>
<tr><td>Sınıflar ve kapsülleme</td><td>model/*.java</td><td>Sekiz sınıfın bütün alanları private. Erişim
getter ve setter ile. İki sınıfta static sayaç alanı, üç static metot var.</td><td>Karşılandı</td></tr>
<tr><td>Kalıtım</td><td>model/Gelir.java, Gider.java, SabitGider.java</td><td>Islem üst sınıf, Gelir ve
Gider ondan türer, SabitGider Gider'den türer. Üç seviye hiyerarşi. super(...) ile ortak alanlar üst
sınıftan doldurulur, toString ve tip metotları ezilir.</td><td>Karşılandı</td></tr>
<tr><td>Soyut sınıf ve çok biçimlilik</td><td>model/Islem.java, service/ButceService.java</td><td>Islem
soyut, butceEtkisi() ve tip() soyut metot. Service içindeki Islem[] dizisinde Gelir, Gider ve SabitGider
birlikte tutulur, çağrı nesnenin gerçek türüne gider.</td><td>Karşılandı</td></tr>
<tr><td>Koleksiyonlar</td><td>service/ButceService.java</td><td>Şu an sabit boyutlu dizi kullanılıyor.
ArrayList ve HashMap geçişi planlandı.</td><td>Kısmen</td></tr>
<tr><td>Arayüz ve sıralama</td><td>—</td><td>Raporlanabilir arayüzü ve Comparable, hafta 9 konusu
olduğu için sonraki sürümde.</td><td>Bekliyor</td></tr>
<tr><td>İstisna yönetimi</td><td>—</td><td>Özel istisna sınıfı hafta 10 konusu. Şu an doğrulama kontrol
ile yapılıyor, program hatalı girişte çökmüyor.</td><td>Bekliyor</td></tr>
<tr><td>Dosya işlemleri</td><td>—</td><td>Hafta 13 konusu.</td><td>Bekliyor</td></tr>
<tr><td>Lambda ve Stream</td><td>—</td><td>Hafta 15 konusu.</td><td>Bekliyor</td></tr>
</table>

<h2>3.1 Çok biçimliliğin kodda görünüşü</h2>
<p>Üst sınıf türünden dizi kullanıldığı için aynı metot çağrısı üç farklı davranış üretir. Gelir sınıfı
tutarı olduğu gibi döndürür, gider sınıfı eksi işaretle döndürür. Böylece toplam hesaplayan metot hangi
kaydın gelir hangisinin gider olduğunu bilmek zorunda kalmaz.</p>
<pre>public abstract class Islem {{          // model/Islem.java
    private static int sayac = 0;
    private int id;
    private double tutar;
    ...
    public abstract double butceEtkisi();   // gövdesi yok
    public abstract String tip();
}}

public class Gelir extends Islem {{      // model/Gelir.java
    @Override
    public double butceEtkisi() {{ return getTutar(); }}   // artı
}}

public class Gider extends Islem {{      // model/Gider.java
    @Override
    public double butceEtkisi() {{ return -getTutar(); }}  // eksi
}}</pre>
<p>Servis sınıfı bu çağrıyı tek satırda yapar. Nesnenin gerçek türü çalışma anında belirlenir, kod
değişmez.</p>
<pre>for (int i = 0; i &lt; islemSayisi; i++) {{
    toplam = toplam + islemler[i].butceEtkisi();   // hangi alt sınıfsa o çalışır
}}</pre>

<h2>3.2 Kapsülleme ve doğrulama</h2>
<p>Bütün alanlar private. Geçersiz değer setter içinde reddediliyor ve eski değer korunuyor. Böylece
nesne hiçbir zaman tutarsız duruma geçmiyor. Aşağıdaki örnekte sıfır ve eksi tutar kabul edilmiyor.</p>
<pre>public void setTutar(double tutar) {{
    if (tutar &lt;= 0) {{
        System.out.println("Uyari: tutar sifir veya eksi olamaz, eski deger korundu.");
        return;
    }}
    this.tutar = tutar;
}}</pre>
<p>Kurucu da aynı setter'ı çağırıyor. Böylece doğrulama tek yerde kalıyor, kurucuya ayrıca kontrol
yazmak gerekmiyor. Bunun bedeli, Java'nın "this-escape" bilgi uyarısıdır. Uyarı derlemeyi durdurmuyor,
bilinçli olarak kabul edildi.</p>

<h2>3.3 Kalıtım zinciri ve super çağrısı</h2>
<p>Kalıtım üç seviyedir. SabitGider, Gider'in bütün alanlarını devralır, üzerine ödeme gününü ekler.
Üst sınıfın kurucusu super ile çağrılır, ortak alanlar tek yerde doldurulur.</p>
<pre>public class SabitGider extends Gider {{
    private int odemeGunu;

    public SabitGider(String aciklama, double tutar, String tarih, Kategori kategori,
                      String odemeYontemi, int odemeGunu) {{
        super(aciklama, tutar, tarih, kategori, odemeYontemi, true);
        setOdemeGunu(odemeGunu);
    }}

    @Override
    public String tip() {{ return "Sabit Gider"; }}   // ust sinifin etiketi degisiyor
}}</pre>

<h2>3.4 Tür analizinde instanceof sırası</h2>
<p>Tür analizi <code>instanceof</code> ile yapılıyor. SabitGider aynı zamanda bir Gider olduğu için en
alt sınıf önce kontrol ediliyor. Sıra tersine çevrilirse bütün sabit giderler gider sayılır ve sayım
yanlış çıkar. Bu hata geliştirme sırasında yaşandı ve düzeltildi.</p>

<h1>4. İstisna Yönetimi Stratejisi</h1>
<p>Özel istisna sınıfı hafta 10 konusu olduğu için bu sürümde henüz kullanılmıyor. Buna karşın program
hatalı girişte çökmüyor. Doğrulama iki katmanda yapılıyor. Birinci katman setter metotları, ikinci
katman kullanıcıdan veri okuyan menü metotları.</p>
<table>
<tr><th style="width:46mm">Öngörülen hata</th><th style="width:34mm">Nerede yakalanıyor</th><th>Kullanıcıya mesaj</th></tr>
<tr><td>Tutar alanına harf yazılması</td><td>Main.metindenSayi</td><td>"Hata: tutar sifirdan buyuk bir sayi olmali. Kayit eklenmedi."</td></tr>
<tr><td>Sıfır veya eksi tutar</td><td>Islem.setTutar</td><td>"Uyari: tutar sifir veya eksi olamaz, eski deger korundu."</td></tr>
<tr><td>Listede olmayan kategori</td><td>ButceService.kategoriBul</td><td>"Hata: boyle bir kategori yok. Kayit eklenmedi."</td></tr>
<tr><td>Boş açıklama</td><td>Main.gelirEkle, Main.giderEkle ve Islem.setAciklama</td><td>"Hata: aciklama bos olamaz. Kayit eklenmedi."</td></tr>
<tr><td>1 ile 31 dışında ödeme günü</td><td>SabitGider.setOdemeGunu</td><td>"Uyari: odeme gunu 1 ile 31 arasinda olmali, eski deger korundu."</td></tr>
<tr><td>Menüde olmayan seçim</td><td>Main döngüsü</td><td>"Gecersiz secim. Menudeki bir numarayi girin."</td></tr>
</table>
<p>Hafta 10'dan sonra bu kontroller <code>GecersizTutarException</code> sınıfıyla birlikte try-catch
bloklarına taşınacak. Amaç kontrolü kaybetmek değil, hatayı çağıran katmana taşıyabilmek.</p>

<h2>4.1 Hatanın kullanıcıya ulaşma biçimi</h2>
<p>Doğrulama iki katmanda olduğu için kullanıcı hatayı her zaman görüyor. Menü katmanı, kullanıcıdan
aldığı metni sayıya çeviremediğinde kaydı hiç oluşturmuyor ve tek satır açıklama yazıp menüye dönüyor.
Model katmanı ise nesne kurulurken geçersiz değeri reddediyor. İki katmanın mesaj dili aynı, kısa ve
anlaşılır tutuldu, teknik terim kullanılmadı.</p>
<p>Bu yaklaşımın sınırı şudur. Hata mesajı ekrana yazılıyor ama çağıran koda bildirilmiyor, yani
program akışı kesilmiyor. Örneğin kurucuya geçersiz tutar verilirse nesne oluşur ama tutarı sıfır
kalır. Hafta 10'da bu davranış istisna ile değişecek, nesne hiç oluşmayacak. Bu, mevcut sürümün
bilinen ve belgelenmiş eksiğidir.</p>

<h1>5. Dosya Yapısı</h1>
<p>Verilerin kalıcılığı hafta 13'te dosya işlemleriyle sağlanacak. Biçim şimdiden sabitlendi, satır
başına bir kayıt, alanlar noktalı virgülle ayrılıyor. İlk alan kaydın türünü söyler, okurken bu alana
bakılıp doğru sınıf üretilir. Böylece çok biçimlilik dosyadan okuma sırasında da kullanılır.</p>
<pre>GELIR;1;32000.00;01.11.2026;Maas;Proje geliri;Serbest
SABIT;3;12500.00;05.11.2026;Kira;Ev kirasi;Havale;5
GIDER;5;2450.00;12.11.2026;Market;Market alisverisi;Kredi karti</pre>

<h2>5.1 Dosya biçiminin alanları</h2>
<table>
<tr><th style="width:20mm">Sıra</th><th style="width:30mm">Alan</th><th>Örnek ve açıklama</th></tr>
<tr><td>1</td><td>Tür</td><td>GELIR, GIDER veya SABIT. Okurken hangi sınıfın üretileceğini belirler.</td></tr>
<tr><td>2</td><td>Numara</td><td>Kaydın kimliği, listede görünen numara.</td></tr>
<tr><td>3</td><td>Tutar</td><td>Nokta ayırıcılı, iki ondalık basamak.</td></tr>
<tr><td>4</td><td>Tarih</td><td>gg.aa.yyyy biçiminde metin.</td></tr>
<tr><td>5</td><td>Kategori</td><td>Kategori adı. Açılışta kategori listesi önce okunur.</td></tr>
<tr><td>6</td><td>Açıklama</td><td>Serbest metin.</td></tr>
<tr><td>7</td><td>Türe özgü alan</td><td>Gelirde kaynak, giderde ödeme yöntemi, sabit giderde ayrıca
ödeme günü.</td></tr>
</table>
<p>Okuma sırasında satır noktalı virgülle ayrılıp tür alanına bakılacak. Tür GELIR ise Gelir
nesnesi, SABIT ise SabitGider nesnesi üretilecek. Böylece çok biçimlilik yalnızca bellekte değil,
dosyadan geri yüklemede de kullanılmış olacak.</p>

<h1>6. Ekran Görüntüleri</h1>
<p>Aşağıdaki görüntüler programın gerçek çıktısıdır. Menü, kayıt listesi, bütçe özeti ve tür analizi
normal akışı, son iki görüntü hatalı giriş senaryolarını gösterir.</p>

<h2>6.1 Ana menü</h2>
<div class="ekran">{e_menu}</div>

<h2>6.2 Kayıt listesi</h2>
<div class="ekran">{e_liste}</div>

<h2>6.3 Bütçe özeti</h2>
<div class="ekran">{e_ozet}</div>

<h2>6.4 Tür analizi</h2>
<div class="ekran">{e_analiz}</div>

<h2>6.5 Gelir ekleme <span class="girdi">girdi: Kitap telifi / 1500,50 / 15.11.2026 / Maas / Telif</span></h2>
<div class="ekran">{a_ekle}</div>

<h2>6.6 Gider ekleme <span class="girdi">girdi: Kirtasiye / 350 / 13.11.2026 / Market / Nakit</span></h2>
<div class="ekran">{d_ekle}</div>

<h2>6.7 Hatalı giriş, tutar sayı değil <span class="girdi">girdi: tutar abc</span></h2>
<div class="ekran">{b_hata}</div>

<h2>6.8 Hatalı giriş, olmayan kategori <span class="girdi">girdi: kategori Yok</span></h2>
<div class="ekran">{c_hata}</div>
<p>Her iki hatada da program kapanmıyor, kayıt eklemiyor ve menüye geri dönüyor.</p>

<h1>7. Karşılaşılan Sorunlar ve Çözümler</h1>
<table>
<tr><th style="width:44mm">Sorun</th><th>Çözüm</th></tr>
<tr><td>Tutar alanında virgül sorunu</td><td>Konsolda ondalık ayırıcı virgül olduğunda değer bölünüyordu.
Yazdırma işini <code>paraYaz()</code> metodu üstlendi, metin girişinde virgül noktaya çevriliyor.</td></tr>
<tr><td>Sabit gideri gider sayma hatası</td><td><code>instanceof Gider</code> kontrolü önce yapıldığında
sabit giderler de gider sayılıyordu. En alt sınıf önce kontrol edilecek şekilde sıra değiştirildi.</td></tr>
<tr><td>Kurucuda doğrulama uyarısı</td><td>Setter kurucudan çağrıldığında Java "this-escape" bilgi
uyarısı veriyor. Uyarı kabul edildi, çünkü geçersiz değerin nesneye hiç girmemesi daha önemli.</td></tr>
<tr><td>Menüde harf girilmesi</td><td><code>nextInt()</code> doğrudan istisna fırlatıyordu.
<code>nextLine()</code> ile metin okunup <code>equals()</code> ile karşılaştırıldı.</td></tr>
<tr><td>Türkçe karakter bozulması</td><td>Kaynak dosyalar ve konsol çıktısı ASCII tutuldu, derleme
<code>-encoding UTF-8</code> ile yapılıyor. Bu yüzden bozulma oluşmadı.</td></tr>
<tr><td>Girdi akışı bitince çökme</td><td>Boru hattıyla beslenen denemede <code>NoSuchElementException</code>
alındı. Okumalar <code>satirOku()</code> metodundan geçirildi, akış bitince program uyarı verip kapanıyor.</td></tr>
<tr><td>Ondalık sayı okuma</td><td>Kullanıcı "1500,50" yazdığında sayı olarak algılanmıyordu. Giriş
metni önce virgülden noktaya çevriliyor, sonra desen kontrolünden geçiyor.</td></tr>
</table>

<h1>8. Grup İçi İş Bölümü</h1>
<p>Proje bireyseldir, yönergenin izin verdiği ölçüde tek kişi tarafından yürütülmüştür. Aşağıdaki tablo
hangi sınıfın kim tarafından yazıldığını gösterir.</p>
<table>
<tr><th style="width:38mm">Üye</th><th style="width:26mm">Numara</th><th>Sorumlu olduğu sınıflar ve işler</th></tr>
<tr><td>Cengiz Kılıç</td><td>251205027</td><td>Islem, Gelir, Gider, SabitGider, Kategori, ButceHesabi,
ButceService, Main. UML diyagramı, rapor, takvim, testler.</td></tr>
</table>
<p>Tasarım kararlarını kendim aldım. Sınıf sayısını sekizde tuttum, taslakta önerilen vergi kesintisi ve
kategori hedef limiti gibi işlevsiz özellikleri projeden çıkardım. Bütün metotları satır satır okuyup
kendi cümlelerimle açıklayabiliyorum. Kodun tamamının sorumluluğu bana aittir.</p>

<h2>8.1 Sorumluluk dağılımı</h2>
<table>
<tr><th style="width:44mm">İş</th><th>Kapsam</th></tr>
<tr><td>Model katmanı</td><td>Altı sınıf, alan doğrulamaları, toString ve soyut metotların alt sınıflarda
uygulanması.</td></tr>
<tr><td>Servis katmanı</td><td>Kayıt ekleme, kategori arama, listeleme, toplam gelir ve gider, net
bakiye, limit kontrolü, tür analizi.</td></tr>
<tr><td>Menü katmanı</td><td>Altı seçenekli menü, gelir ve gider ekleme akışı, hatalı girişte menüye
dönüş.</td></tr>
<tr><td>Belgeler</td><td>UML diyagramı iki sayfa, ara rapor, yirmi işlik takvim, Javadoc belgeleri.</td></tr>
</table>

<h1>9. Yapay Zekâ Kullanım Beyanı ve Kaynakça</h1>
<h2>9.1 Beyan</h2>
<p>Bu projede yapay zekâ araçlarından aşağıdaki işlerde destek aldım. Kullanım alanlarını tek tek
yazıyorum.</p>
<table>
<tr><th style="width:52mm">Kullanım alanı</th><th>Ne yapıldı</th></tr>
<tr><td>Sınıf yapısının ilk taslağı</td><td>Sekiz sınıfın sorumluluk dağılımı ve paket yerleşimi için
öneri alındı. Taslakta on bir sınıf vardı, işlevsiz olanlar çıkarılıp sekize indirildi.</td></tr>
<tr><td>Kod yazımı ve sadeleştirme</td><td>Metot gövdeleri yazıldı, ardından her metot satır satır
okunup anlaşılmayan kısımlar sadeleştirildi.</td></tr>
<tr><td>Derleme ve hata ayıklama</td><td>Kodun derlenmesi, JDK 17 uyumunun denenmesi ve hatalı giriş
senaryolarının çalıştırılması.</td></tr>
<tr><td>Belge düzeni</td><td>Rapor metninin başlık yapısı, sayfa düzeni, 11 punto yazı boyutu, 1,15
satır aralığı, sayfa altı bilgi satırı ve sayfa numarası ayarları.</td></tr>
<tr><td>Kapak sayfası</td><td>Kapak yerleşimi, üniversite logosunun yerleştirilmesi ve bilgi tablosunun
hizalanması.</td></tr>
<tr><td>PDF üretimi</td><td>Belgelerin PDF çıktısının alınması ve sayfa numaralarının eklenmesi.</td></tr>
<tr><td>Javadoc belgeleri</td><td>Sınıf ve metot açıklamalarının yazılması, Javadoc çıktısının
üretilmesi.</td></tr>
</table>
<p>Tasarım kararları, sınıf sayısı, hangi özelliğin projeye girip girmeyeceği ve kodun savunulabilir
sadeliği bana aittir. Sunumda sorulan sorulara kendi kodum üzerinden cevap vereceğim.</p>

<h2>9.2 Kaynakça</h2>
<ol>
<li>BLG205 Nesne Tabanlı Programlamaya Giriş ders slaytları, hafta 1-15, İstanbul Rumeli Üniversitesi, 2026.</li>
<li>BLG205 Dönem Projesi Yönergesi, 2026.</li>
<li>Oracle. <i>Java SE Documentation</i>, docs.oracle.com/javase.</li>
<li>Oracle. <i>Java Language Specification</i>, bölüm 8 (sınıflar) ve bölüm 11 (istisnalar).</li>
<li>Gamma, E. ve ark. <i>Design Patterns</i>, Addison-Wesley, 1994. Yalnızca kavram için başvuruldu,
kodda tasarım deseni kullanılmadı.</li>
<li>Proje deposu, github.com/gecekargosu/blg205-butce-takip (herkese açık, ara teslimde sekiz işlem gönderildi).</li>
</ol>
"""


def uret():
    icerik = "<html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>" + kapak() + govde() + "</body></html>"
    gecici = KOK / "00_Kapak/_rapor.html"
    gecici.write_text(icerik, encoding="utf-8")
    ham = KOK / "00_Kapak/_rapor_ham.pdf"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--user-data-dir=" + os.environ.get("TEMP", ".") + "/chr_rapor",
                    "--no-pdf-header-footer", "--print-to-pdf=" + str(ham),
                    "file:///" + gecici.as_posix()], capture_output=True, timeout=180)
    if not ham.exists():
        print("HATA: PDF uretilemedi"); return
    altbilgi_ekle(ham, CIKTI)
    ham.unlink(missing_ok=True)
    gecici.unlink(missing_ok=True)
    print("uretildi:", CIKTI, os.path.getsize(CIKTI), "bayt")


def altbilgi_ekle(kaynak, hedef):
    """Her sayfaya altbilgi yazar. Kapak sayfasi atlanir."""
    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.pagesizes import A4
    import io
    try:
        pdfmetrics.registerFont(TTFont("ArialTR", "C:/Windows/Fonts/arial.ttf"))
        font = "ArialTR"
    except Exception:
        font = "Helvetica"

    okuyucu = PdfReader(str(kaynak))
    toplam = len(okuyucu.pages)
    yazici = PdfWriter()
    sol = "BLG205 Nesne Tabanlı Programlamaya Giriş"
    orta = "Kişisel Gelir Gider ve Bütçe Takip Sistemi"
    for i, sayfa in enumerate(okuyucu.pages):
        if i > 0:
            tampon = io.BytesIO()
            c = canvas.Canvas(tampon, pagesize=A4)
            c.setFont(font, 7.5)
            c.setStrokeColorRGB(0.7, 0.7, 0.7)
            c.line(51, 40, A4[0] - 51, 40)
            c.setFillColorRGB(0.35, 0.35, 0.35)
            c.drawString(51, 29, f"{sol}  |  {orta}")
            c.drawRightString(A4[0] - 51, 29, f"Cengiz Kılıç 251205027  ·  Sayfa {i} / {toplam - 1}")
            c.save()
            tampon.seek(0)
            sayfa.merge_page(PdfReader(tampon).pages[0])
        yazici.add_page(sayfa)
    with open(hedef, "wb") as f:
        yazici.write(f)


if __name__ == "__main__":
    uret()
