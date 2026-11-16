# -*- coding: utf-8 -*-
"""Kalan isler takvimini HTML (PDF icin) ve XLSX olarak uretir."""

ISLER = [
    ("1",  "UML sınıf diyagramı", "15.11.2026", "16.11.2026", "UML png + pdf", "Tamamlandı"),
    ("2",  "Derlenebilir iskelet kod", "15.11.2026", "16.11.2026", "sekiz sınıf, javac temiz", "Tamamlandı"),
    ("3",  "Ara teslim paketi ve UZEM yüklemesi", "16.11.2026", "16.11.2026", "ZIP", "Tamamlandı"),
    ("4",  "Git deposu ve düzenli commitler", "16.11.2026", "18.12.2026", "GitHub bağlantısı", "Sürüyor"),
    ("5",  "Gelir ve gider ekleme ekranları", "17.11.2026", "23.11.2026", "kullanıcı girişli menü", "Bekliyor"),
    ("6",  "Arayüz tanımı ve uygulanması", "24.11.2026", "30.11.2026", "Raporlanabilir arayüzü", "Bekliyor"),
    ("7",  "Doğrulama ve özel istisna sınıfı", "24.11.2026", "30.11.2026", "exception paketi, try-catch", "Bekliyor"),
    ("8",  "ArrayList ve HashMap'e geçiş", "01.12.2026", "07.12.2026", "koleksiyon tabanlı servis", "Bekliyor"),
    ("9",  "Repository<T> generic sınıfı", "01.12.2026", "07.12.2026", "repository paketi", "Bekliyor"),
    ("10", "Dosyaya kayıt ve dosyadan yükleme", "01.12.2026", "07.12.2026", "data/islemler.txt", "Bekliyor"),
    ("11", "Comparable ile sıralama", "08.12.2026", "11.12.2026", "tarihe göre sıralı liste", "Bekliyor"),
    ("12", "Lambda ve Stream ile raporlama", "08.12.2026", "14.12.2026", "filtre, sıralama, özet", "Bekliyor"),
    ("13", "JUnit 5 ile en az 10 birim testi", "08.12.2026", "13.12.2026", "test sınıfları", "Bekliyor"),
    ("14", "Hatalı giriş testleri ve düzeltmeler", "13.12.2026", "15.12.2026", "test tutanağı", "Bekliyor"),
    ("15", "Javadoc belgeleri", "10.12.2026", "17.12.2026", "doc klasörü", "Bekliyor"),
    ("16", "Final raporu", "14.12.2026", "17.12.2026", "PDF rapor", "Bekliyor"),
    ("17", "Sunum dosyası", "16.12.2026", "18.12.2026", "slayt dosyası", "Bekliyor"),
    ("18", "Demo videosu", "17.12.2026", "18.12.2026", "5-8 dakika mp4", "Bekliyor"),
    ("19", "Final ZIP ve UZEM yüklemesi", "18.12.2026", "18.12.2026", "teslim paketi", "Bekliyor"),
    ("20", "Sözlü sunum provası", "19.12.2026", "23.12.2026", "soru cevap hazırlığı", "Bekliyor"),
]

GEREKSINIM = """
<table>
<tr><th style="width:8mm">#</th><th style="width:52mm">Zorunlu gereksinim</th><th style="width:15mm">Hafta</th>
<th style="width:20mm">Şu an</th><th>Nerede karşılanacak</th></tr>
<tr><td>1</td><td>Sınıflar ve kapsülleme</td><td>4-6</td><td>Var</td><td>Sekiz sınıf, bütün alanlar private, doğrulamalı setter</td></tr>
<tr><td>2</td><td>Kalıtım ve override</td><td>7</td><td>Var</td><td>Islem, Gelir, Gider, SabitGider zinciri, super çağrıları</td></tr>
<tr><td>3</td><td>Soyut sınıf ve çok biçimlilik</td><td>8</td><td>Var</td><td>Islem soyut, Islem[] üzerinden çağrı</td></tr>
<tr><td>4</td><td>Arayüz ve sıralama</td><td>9</td><td>Yok</td><td>Raporlanabilir arayüzü, Comparable, 24 Kasım - 11 Aralık</td></tr>
<tr><td>5</td><td>Özel istisna ve try-catch</td><td>10</td><td>Yok</td><td>GecersizTutarException, 24-30 Kasım</td></tr>
<tr><td>6</td><td>ArrayList ve HashMap</td><td>11</td><td>Yok</td><td>Repository&lt;T&gt; ve ButceService, 1-7 Aralık</td></tr>
<tr><td>7</td><td>Dosya işlemleri</td><td>13</td><td>Yok</td><td>DosyaIslemleri, 1-7 Aralık</td></tr>
<tr><td>8</td><td>Lambda ve Stream</td><td>15</td><td>Yok</td><td>ButceService rapor metotları, 8-14 Aralık</td></tr>
</table>
<p class="kucuk">Dördüncüden sekizinciye kadar olan satırlar derste henüz işlenmediği için ara teslim kodunda
bilerek kullanılmadı. İlgili haftalar geçtikten sonra eklenecek, böylece sunumda her satırı anlatabiliyor olacağım.</p>
"""

EK_PUAN = """
<table>
<tr><th style="width:44mm">Ek puan seçeneği</th><th>Ne yapacağız</th><th style="width:28mm">Ne zaman</th>
<th style="width:34mm">Kodu büyütür mü</th></tr>
<tr class="tamam"><td>Generic sınıf</td><td>Repository&lt;T&gt;, hem işlem hem kategori listesi için</td><td>1-7 Aralık</td><td>Hayır, 20 satır</td></tr>
<tr class="tamam"><td>JUnit 5</td><td>En az 10 birim testi, ayrı test klasöründe</td><td>8-13 Aralık</td><td>Hayır, koda dokunmuyor</td></tr>
<tr class="tamam"><td>Git ve GitHub</td><td>Depo kurulumu, haftalık anlamlı commitler</td><td>16 Kasım - 18 Aralık</td><td>Hayır</td></tr>
<tr class="tamam"><td>Javadoc</td><td>Sınıf ve metot belgeleri, doc klasörüne çıktı</td><td>10-17 Aralık</td><td>Yorum ekler, mantık eklemez</td></tr>
<tr><td>Swing veya JavaFX</td><td>Yapmıyoruz, konsol uygulaması yeterli</td><td>—</td><td>Evet, çok büyütür</td></tr>
<tr><td>Thread</td><td>Yapmıyoruz, projede gerçek bir ihtiyaç yok</td><td>—</td><td>Evet</td></tr>
<tr><td>Tasarım deseni</td><td>Yapmıyoruz, zorlama olur</td><td>—</td><td>Orta, anlatması zor</td></tr>
</table>
<p class="kucuk">Seçtiğimiz dört çalışma kodun satır sayısını artırmıyor. Üçünü zaten yapmamız gerekiyordu
(sürüm kontrolü, test, belge), biri de on dokuz satırlık bir sınıf.</p>
"""

satirlar = ""
for no, is_ad, bas, bit, cikti, durum in ISLER:
    sinif = ' class="tamam"' if durum in ("Tamamlandı", "Sürüyor") else ""
    satirlar += ('<tr%s><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n'
                 % (sinif, no, is_ad, bas, bit, cikti, durum))

html = """<!DOCTYPE html>
<html lang="tr"><head><meta charset="utf-8"><style>
@page { size: A4; margin: 15mm 13mm 13mm 13mm; }
body { font-family: "Segoe UI", Calibri, Arial, sans-serif; font-size: 9.6pt; color: #1a1a1a; line-height: 1.4; }
h1 { font-size: 16pt; margin: 0 0 2mm 0; color: #17301f; }
h2 { font-size: 11.5pt; margin: 5mm 0 2mm 0; color: #2c5d3f; border-bottom: 1px solid #2c5d3f; padding-bottom: 1mm; }
.alt { font-size: 8.8pt; color: #555; margin: 0 0 3mm 0; }
table { width: 100%%; border-collapse: collapse; font-size: 8.5pt; margin-bottom: 3mm; }
th { background: #2c5d3f; color: #fff; text-align: left; padding: 1.3mm 1.7mm; }
td { border-bottom: 0.5px solid #cfd6cf; padding: 1.2mm 1.7mm; vertical-align: top; }
tr.tamam td { background: #eef3ee; }
.kucuk { font-size: 8.3pt; color: #444; margin: 0 0 3mm 0; }
.not { background: #fdfbf3; border-left: 3px solid #8a6d3b; padding: 2.2mm 2.8mm; font-size: 8.8pt; margin-top: 2mm; }
.sayfa { page-break-after: always; }
.sayfa:last-child { page-break-after: auto; }
</style></head><body>

<div class="sayfa">
<h1>Kalan İşler ve Çalışma Takvimi</h1>
<p class="alt">Kişisel Gelir-Gider ve Bütçe Takip Sistemi &nbsp;|&nbsp; BLG205 Nesne Tabanlı Programlamaya Giriş
&nbsp;|&nbsp; Cengiz Kılıç 251205027 &nbsp;|&nbsp; Ara teslim: 16 Kasım 2026, final: 18 Aralık 2026</p>

<h2>1. Takvim</h2>
<table>
<tr><th style="width:7mm">#</th><th style="width:50mm">Yapılacak iş</th><th style="width:19mm">Başlangıç</th>
<th style="width:19mm">Bitiş</th><th>Beklenen çıktı</th><th style="width:19mm">Durum</th></tr>
%s</table>

<div class="not"><b>Çalışma düzeni.</b> Haftada yaklaşık dört saat ayırıyorum. Her işin sonunda kod derleniyor ve
çalıştırılıyor, bozuk bir sürüm üzerine yeni özellik eklemiyorum. Ara teslim tarihine kadar olan üç iş bitti,
dördüncüsü sürüyor. Kalanlar derste ilgili konu işlendikten sonraki haftaya yazıldı.</div>
</div>

<div class="sayfa">
<h2>2. Zorunlu gereksinimlerin durumu</h2>
%s

<h2>3. Ek puan hedefleri</h2>
%s

<h2>4. Riskler ve önlem</h2>
<table>
<tr><th style="width:50mm">Risk</th><th>Önlem</th></tr>
<tr><td>Son haftaya iş yığılması</td><td>Dosya işlemleri ve koleksiyonlar Aralık başında bitecek, son hafta sadece rapor ve video kalacak</td></tr>
<tr><td>Sunumda soruya cevap verememek</td><td>Her sınıfın neden var olduğunu bu dosyada ve UML üzerinde not ettim, haftada bir kendi kodumu baştan okuyacağım</td></tr>
<tr><td>Kodun tasarımdan kopması</td><td>Yeni metot eklerken önce UML'i güncelleyip sonra kodu yazacağım</td></tr>
<tr><td>Dosya bozulması</td><td>Her hafta sonu proje klasörünün kopyasını ayrı bir yere alacağım, ayrıca Git geçmişi var</td></tr>
</table>

<div class="not"><b>Ölçü.</b> Bu takvimde bir iş ancak kodu derlenip çalıştığında tamamlandı sayılıyor.
Kâğıt üzerinde kalan iş, teslim edilmiş iş değil.</div>
</div>

</body></html>
""" % (satirlar, GEREKSINIM, EK_PUAN)

with open("Kalan_Isler_ve_Takvim.html", "w", encoding="utf-8") as f:
    f.write(html)

# ------------------------------------------------------------------ xlsx
try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment

    wb = Workbook()
    ws = wb.active
    ws.title = "Takvim"
    ws.append(["No", "Yapılacak iş", "Başlangıç", "Bitiş", "Beklenen çıktı", "Durum"])
    for c in range(1, 7):
        h = ws.cell(row=1, column=c)
        h.font = Font(bold=True, color="FFFFFF")
        h.fill = PatternFill("solid", fgColor="2C5D3F")

    for no, is_ad, bas, bit, cikti, durum in ISLER:
        ws.append([no, is_ad, bas, bit, cikti, durum])

    for satir in ws.iter_rows(min_row=2, max_row=len(ISLER) + 1):
        if satir[5].value in ("Tamamlandı", "Sürüyor"):
            for c in satir:
                c.fill = PatternFill("solid", fgColor="EEF3EE")

    for kolon, genislik in (("A", 6), ("B", 44), ("C", 14), ("D", 14), ("E", 30), ("F", 14)):
        ws.column_dimensions[kolon].width = genislik
    for satir in ws.iter_rows(min_row=1, max_row=len(ISLER) + 1):
        for c in satir:
            c.alignment = Alignment(vertical="top", wrap_text=True)

    ws2 = wb.create_sheet("Gereksinim Durumu")
    ws2.append(["#", "Zorunlu gereksinim", "Hafta", "Şu an", "Nerede karşılanacak"])
    for c in range(1, 6):
        h = ws2.cell(row=1, column=c)
        h.font = Font(bold=True, color="FFFFFF")
        h.fill = PatternFill("solid", fgColor="2C5D3F")
    veri = [
        (1, "Sınıflar ve kapsülleme", "4-6", "Var", "Sekiz sınıf, private alanlar, doğrulamalı setter"),
        (2, "Kalıtım ve override", "7", "Var", "Islem, Gelir, Gider, SabitGider"),
        (3, "Soyut sınıf ve çok biçimlilik", "8", "Var", "Islem soyut, Islem[] üzerinden çağrı"),
        (4, "Arayüz ve sıralama", "9", "Yok", "Raporlanabilir ve Comparable, 24 Kasım - 11 Aralık"),
        (5, "Özel istisna ve try-catch", "10", "Yok", "GecersizTutarException, 24-30 Kasım"),
        (6, "ArrayList ve HashMap", "11", "Yok", "Repository<T> ve ButceService, 1-7 Aralık"),
        (7, "Dosya işlemleri", "13", "Yok", "DosyaIslemleri, 1-7 Aralık"),
        (8, "Lambda ve Stream", "15", "Yok", "ButceService rapor metotları, 8-14 Aralık"),
    ]
    for v in veri:
        ws2.append(list(v))
    for kolon, genislik in (("A", 6), ("B", 34), ("C", 10), ("D", 10), ("E", 52)):
        ws2.column_dimensions[kolon].width = genislik

    ws3 = wb.create_sheet("Ek Puan")
    ws3.append(["Ek puan seçeneği", "Ne yapacağız", "Ne zaman", "Kodu büyütür mü"])
    for c in range(1, 5):
        h = ws3.cell(row=1, column=c)
        h.font = Font(bold=True, color="FFFFFF")
        h.fill = PatternFill("solid", fgColor="2C5D3F")
    ekler = [
        ("Generic sınıf", "Repository<T>, işlem ve kategori listesi için", "1-7 Aralık", "Hayır"),
        ("JUnit 5", "En az 10 birim testi", "8-13 Aralık", "Hayır"),
        ("Git ve GitHub", "Depo ve düzenli commitler", "16 Kasım - 18 Aralık", "Hayır"),
        ("Javadoc", "Sınıf ve metot belgeleri", "10-17 Aralık", "Yorum ekler"),
        ("Swing veya JavaFX", "Yapmıyoruz", "—", "Evet, çok"),
        ("Thread", "Yapmıyoruz", "—", "Evet"),
        ("Tasarım deseni", "Yapmıyoruz", "—", "Orta"),
    ]
    for e in ekler:
        ws3.append(list(e))
    for kolon, genislik in (("A", 24), ("B", 52), ("C", 26), ("D", 20)):
        ws3.column_dimensions[kolon].width = genislik

    wb.save("Kalan_Isler_ve_Takvim.xlsx")
    print("xlsx yazildi")
except Exception as hata:
    print("xlsx atlandi:", hata)

print("Kalan_Isler_ve_Takvim.html yazildi")
