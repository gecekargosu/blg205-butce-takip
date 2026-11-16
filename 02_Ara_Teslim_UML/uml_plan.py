# -*- coding: utf-8 -*-
"""
UML diyagraminin ikinci sayfasini uretir: finalde eklenecek siniflar.
Birinci sayfa uml.svg, ikinci sayfa bu sayfa. Ikisi tek PDF'te birlestirilir.
Bu sayfadaki siniflar ara teslim kodunda yoktur, plan olarak cizilmistir.
"""

SAYFA2 = """
<div class="bas">
  <div class="h1">Final sürümünde eklenecek sınıflar</div>
  <div class="h2">Plan sayfası. Aşağıdaki dört sınıf ara teslim kodunda yoktur, Aralık 2026'da eklenecek.
  Birinci sayfadaki diyagram bu sınıflar eklendiğinde güncellenecek.</div>
</div>

<div class="izgara">

  <div class="kart">
    <div class="kbas"><span class="stereo">&lt;&lt;interface&gt;&gt;</span><br>Raporlanabilir</div>
    <div class="yol">model/Raporlanabilir.java</div>
    <div class="govde">
      <div class="bolum">metotlar</div>
      <div class="uy">+ raporSatiri() : String</div>
      <div class="not"><b>Neden:</b> her işlem kendi özet satırını üretiyor. Liste ekranı tek metotla
      besleniyor, gelir ve gider için ayrı ayrı yazdırma kodu kalmıyor. Islem sınıfı bunu uygulayacak.</div>
      <div class="hafta">Hafta 9</div>
    </div>
  </div>

  <div class="kart">
    <div class="kbas"><span class="stereo">extends RuntimeException</span><br>GecersizTutarException</div>
    <div class="yol">exception/GecersizTutarException.java</div>
    <div class="govde">
      <div class="bolum">alanlar</div>
      <div class="uy">- hataliDeger : double</div>
      <div class="bolum">metotlar</div>
      <div class="uy">+ GecersizTutarException(mesaj, hataliDeger)</div>
      <div class="uy">+ getHataliDeger() : double</div>
      <div class="not"><b>Neden:</b> setTutar içinde sıfır veya eksi değer görülünce fırlatılacak.
      Menü yakalayıp "tutar sıfırdan büyük olmalı" mesajını basacak, program kapanmayacak.</div>
      <div class="hafta">Hafta 10</div>
    </div>
  </div>

  <div class="kart">
    <div class="kbas"><span class="stereo">&lt;&lt;generic&gt;&gt;</span><br>Repository&lt;T&gt;</div>
    <div class="yol">repository/Repository.java</div>
    <div class="govde">
      <div class="bolum">alanlar</div>
      <div class="uy">- kayitlar : ArrayList&lt;T&gt;</div>
      <div class="bolum">metotlar</div>
      <div class="uy">+ ekle(kayit : T) : void</div>
      <div class="uy">+ hepsiniGetir() : ArrayList&lt;T&gt;</div>
      <div class="uy">+ boyut() : int</div>
      <div class="not"><b>Neden:</b> işlem listesi ve kategori listesi aynı sınıfla tutuluyor.
      ArrayList kutunun içinde kalıyor, dışarıya sadece ekle ve listele görünüyor.
      Bu sınıf ek puan getiriyor, kodu büyütmüyor.</div>
      <div class="hafta">Hafta 11-12</div>
    </div>
  </div>

  <div class="kart">
    <div class="kbas"><br>DosyaIslemleri</div>
    <div class="yol">repository/DosyaIslemleri.java</div>
    <div class="govde">
      <div class="bolum">alanlar</div>
      <div class="uy">- dosyaAdi : String</div>
      <div class="bolum">metotlar</div>
      <div class="uy">+ kaydet(liste : ArrayList&lt;Islem&gt;) : void</div>
      <div class="uy">+ yukle() : ArrayList&lt;Islem&gt;</div>
      <div class="not"><b>Neden:</b> program kapanırken kayıtlar dosyaya yazılıyor, açılışta geri okunuyor.
      Dosya yoksa program çökmüyor, boş listeyle başlıyor.</div>
      <div class="hafta">Hafta 13</div>
    </div>
  </div>

</div>

<div class="tablo">
  <div class="h3">Hangi gereksinim nerede karşılanacak</div>
  <table>
    <tr><th style="width:52mm">Gereksinim</th><th>Nerede</th><th style="width:20mm">Hafta</th><th style="width:24mm">Durum</th></tr>
    <tr><td>Arayüz</td><td>model/Raporlanabilir.java, Islem implements</td><td>9</td><td>Planlandı</td></tr>
    <tr><td>Özel istisna</td><td>exception/GecersizTutarException.java</td><td>10</td><td>Planlandı</td></tr>
    <tr><td>ArrayList</td><td>repository/Repository.java</td><td>11</td><td>Planlandı</td></tr>
    <tr><td>HashMap</td><td>service/ButceService.java, kategoriler</td><td>11</td><td>Planlandı</td></tr>
    <tr><td>Generic sınıf (ek puan)</td><td>repository/Repository.java</td><td>12</td><td>Planlandı</td></tr>
    <tr><td>Dosya işlemleri</td><td>repository/DosyaIslemleri.java</td><td>13</td><td>Planlandı</td></tr>
    <tr><td>Lambda ve Stream</td><td>service/ButceService.java, rapor metotları</td><td>15</td><td>Planlandı</td></tr>
    <tr><td>Sıralama</td><td>model/Islem.java, Comparable</td><td>9</td><td>Planlandı</td></tr>
    <tr><td>JUnit, Git, Javadoc (ek puan)</td><td>test/ klasörü, GitHub deposu, doc/</td><td>11-17 Ara</td><td>Planlandı</td></tr>
  </table>
  <div class="dip">Bu sayfadaki hiçbir sınıf henüz yazılmadı. Takvimde tarihleri var, o tarihlerde yazılıp
  birinci sayfadaki diyagram güncellenecek.</div>
</div>
"""

STIL = """
@page { size: A3 landscape; margin: 0; }
html, body { margin: 0; padding: 0; }
body { width: 420mm; height: 297mm; font-family: "Segoe UI", Calibri, Arial, sans-serif;
       color: #1a1a1a; padding: 14mm 16mm; box-sizing: border-box; }
.bas { margin-bottom: 7mm; }
.h1 { font-family: Georgia, serif; font-size: 20pt; font-weight: bold; color: #16261c; }
.h2 { font-size: 10.5pt; color: #4a5a4f; margin-top: 2mm; max-width: 340mm; }
.izgara { display: grid; grid-template-columns: 1fr 1fr; gap: 7mm; }
.kart { border: 1.6px dashed #8a6d3b; background: #fdfbf3; padding: 4mm 5mm; }
.kbas { font-family: Georgia, serif; font-size: 13pt; font-weight: bold; color: #16261c;
        text-align: center; border-bottom: 1.2px solid #8a6d3b; padding-bottom: 2mm; }
.stereo { font-size: 9.5pt; font-style: italic; font-weight: normal; color: #7a5c2e; }
.yol { font-family: Consolas, monospace; font-size: 9.5pt; color: #7a5c2e; text-align: center; margin: 2mm 0; }
.govde { font-size: 10pt; }
.bolum { font-size: 8.5pt; text-transform: uppercase; letter-spacing: 0.6pt; color: #6b7a6e; margin: 2mm 0 1mm 0; }
.uy { font-family: Consolas, monospace; font-size: 10pt; color: #243b2b; margin-left: 2mm; }
.not { font-size: 9.5pt; color: #3d4a42; margin-top: 3mm; line-height: 1.45; text-align: justify; }
.hafta { display: inline-block; margin-top: 2.5mm; font-size: 9pt; background: #2c5d3f; color: #fff;
         padding: 1mm 3mm; }
.tablo { margin-top: 8mm; }
.h3 { font-family: Georgia, serif; font-size: 13pt; font-weight: bold; color: #2c5d3f;
      border-bottom: 1.2px solid #2c5d3f; padding-bottom: 1.5mm; margin-bottom: 3mm; }
table { width: 100%; border-collapse: collapse; font-size: 9.5pt; }
th { background: #2c5d3f; color: #fff; text-align: left; padding: 1.6mm 2.5mm; }
td { border-bottom: 0.6px solid #cfd6cf; padding: 1.4mm 2.5mm; }
tr:nth-child(even) td { background: #f6f7f5; }
.dip { font-size: 9pt; color: #555; margin-top: 3mm; font-style: italic; }
"""

html = ('<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8"><title>UML sayfa 2</title>'
        '<style>%s</style></head><body>%s</body></html>' % (STIL, SAYFA2))

with open("uml_plan.html", "w", encoding="utf-8") as f:
    f.write(html)

# ---------------------------------------------------- iki sayfayi tek PDF icin birlestir
with open("uml.svg", encoding="utf-8") as f:
    svg1 = f.read()

birlesik = """<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8"><style>
@page { size: A3 landscape; margin: 0; }
html, body { margin: 0; padding: 0; }
.sayfa { width: 420mm; height: 297mm; page-break-after: always; overflow: hidden; }
.sayfa:last-child { page-break-after: auto; }
svg { display: block; width: 420mm; height: 297mm; }
</style></head><body>
<div class="sayfa">%s</div>
<div class="sayfa">%s</div>
</body></html>""" % (svg1, SAYFA2)

# ikinci sayfanin stili birlesik dosyada da gecerli olsun diye stil blogunu tasi
birlesik = birlesik.replace("</style>", STIL + "\n</style>", 1)
# ikinci sayfa icin body olculerini sifirla, sayfa kutusu olcu versin
birlesik = birlesik.replace("body { width: 420mm; height: 297mm;",
                            "body { width: auto; height: auto;")

with open("uml_birlesik.html", "w", encoding="utf-8") as f:
    f.write(birlesik)

print("uml_plan.html ve uml_birlesik.html yazildi")
