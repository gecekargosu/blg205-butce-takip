# -*- coding: utf-8 -*-
"""
UML sinif diyagramini SVG olarak uretir.
Kutulardaki alan ve metotlar kod dosyalariyla birebir ayni.
Uzun kurucu satirlari iki satira bolunuyor ki kutu disina tasmasin.
"""

W = 1620
H = 1180
LH = 15.0
FS = 11.0

parcalar = []


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def kutu(x, y, w, ad, stereo, alanlar, metotlar):
    m_satir = 0
    for m in metotlar:
        m_satir = m_satir + (len(m) if isinstance(m, (list, tuple)) else 1)
    ust = 8 + (13 if stereo else 0) + 21
    h = ust + 7 + len(alanlar) * LH + 7 + m_satir * LH + 10

    parcalar.append('<rect x="%g" y="%g" width="%g" height="%g" fill="#ffffff" '
                    'stroke="#243b2b" stroke-width="1.8"/>' % (x, y, w, h))

    imlec = y + 6
    if stereo:
        imlec += 13
        parcalar.append('<text x="%g" y="%g" font-family="Georgia,serif" font-size="10.5" '
                        'font-style="italic" fill="#4a5a4f" text-anchor="middle">&lt;&lt;%s&gt;&gt;</text>'
                        % (x + w / 2, imlec, esc(stereo)))
    imlec += 16
    stil = 'font-style="italic"' if stereo == "abstract" else 'font-weight="bold"'
    parcalar.append('<text x="%g" y="%g" font-family="Georgia,serif" font-size="13.5" %s '
                    'fill="#16261c" text-anchor="middle">%s</text>'
                    % (x + w / 2, imlec, stil, esc(ad)))

    cy = y + ust
    parcalar.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="#243b2b" stroke-width="1.2"/>'
                    % (x, cy, x + w, cy))
    cy += 7 + 11
    for a in alanlar:
        parcalar.append('<text x="%g" y="%g" font-family="Consolas,Menlo,monospace" font-size="%g" '
                        'fill="#243b2b">%s</text>' % (x + 9, cy, FS, esc(a)))
        cy += LH

    cy = y + ust + 7 + len(alanlar) * LH + 7
    parcalar.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="#243b2b" stroke-width="1.2"/>'
                    % (x, cy, x + w, cy))
    cy += 11
    for m in metotlar:
        satirlar = m if isinstance(m, (list, tuple)) else [m]
        for s in satirlar:
            parcalar.append('<text x="%g" y="%g" font-family="Consolas,Menlo,monospace" font-size="%g" '
                            'fill="#243b2b">%s</text>' % (x + 9, cy, FS, esc(s)))
            cy += LH
    return {"x": x, "y": y, "w": w, "h": h}


def baslik(x, y, metin, boyut=13):
    parcalar.append('<text x="%g" y="%g" font-family="Georgia,serif" font-size="%g" '
                    'font-weight="bold" fill="#16261c">%s</text>'
                    % (x, y, boyut, esc(metin)))


def yazi(x, y, metin, boyut=10.5, stil=""):
    parcalar.append('<text x="%g" y="%g" font-family="Georgia,serif" font-size="%g" %s '
                    'fill="#3d4a42">%s</text>' % (x, y, boyut, stil, esc(metin)))


def paket(x, y, w, h, ad):
    parcalar.append('<rect x="%g" y="%g" width="%g" height="%g" fill="#f4f6f3" '
                    'stroke="#7d8d80" stroke-width="1.3" stroke-dasharray="6 4"/>' % (x, y, w, h))
    parcalar.append('<text x="%g" y="%g" font-family="Georgia,serif" font-size="12" '
                    'font-style="italic" fill="#54604f">package %s</text>' % (x + 10, y + 17, esc(ad)))


def _yon(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    uzun = (dx * dx + dy * dy) ** 0.5
    if uzun == 0:
        return 0, -1
    return dx / uzun, dy / uzun


def ok(noktalar, tur="kalinim", kesikli=False):
    d = " ".join("%g,%g" % (p[0], p[1]) for p in noktalar)
    dash = ' stroke-dasharray="7 5"' if kesikli else ''
    parcalar.append('<polyline points="%s" fill="none" stroke="#243b2b" stroke-width="1.7"%s/>'
                    % (d, dash))
    son = noktalar[-1]
    dx, dy = _yon(noktalar[-2], son)
    px, py = -dy, dx

    if tur == "kalinim":
        b = (son[0] - dx * 13, son[1] - dy * 13)
        a1 = (b[0] + px * 6, b[1] + py * 6)
        a2 = (b[0] - px * 6, b[1] - py * 6)
        parcalar.append('<polygon points="%g,%g %g,%g %g,%g" fill="#ffffff" '
                        'stroke="#243b2b" stroke-width="1.7"/>'
                        % (son[0], son[1], a1[0], a1[1], a2[0], a2[1]))
        parcalar.append('<polygon points="%g,%g %g,%g %g,%g" fill="#ffffff" stroke="none"/>'
                        % (son[0] + dx * 1.5, son[1] + dy * 1.5,
                           b[0] + px * 5.2, b[1] + py * 5.2,
                           b[0] - px * 5.2, b[1] - py * 5.2))
        parcalar.append('<polygon points="%g,%g %g,%g %g,%g" fill="none" '
                        'stroke="#243b2b" stroke-width="1.7"/>'
                        % (son[0], son[1], a1[0], a1[1], a2[0], a2[1]))
    else:
        a1 = (son[0] - dx * 11 + px * 5, son[1] - dy * 11 + py * 5)
        a2 = (son[0] - dx * 11 - px * 5, son[1] - dy * 11 - py * 5)
        parcalar.append('<polyline points="%g,%g %g,%g %g,%g" fill="none" '
                        'stroke="#243b2b" stroke-width="1.7"/>'
                        % (a1[0], a1[1], son[0], son[1], a2[0], a2[1]))


# ------------------------------------------------------------------ baslik
baslik(32, 36, "Kişisel Gelir-Gider ve Bütçe Takip Sistemi", 17)
yazi(32, 56, "UML sınıf diyagramı  |  BLG205 Nesne Tabanlı Programlamaya Giriş  |  "
             "Cengiz Kılıç 251205027  |  Ara teslim", 10.5)

paket(30, 72, 770, 1060, "model")
paket(830, 72, 760, 515, "service")
paket(830, 610, 760, 250, "app")

# ------------------------------------------------------------------ model
isle = kutu(100, 122, 330, "Islem", "abstract",
            ["- sayac : int   {static}",
             "- id : int",
             "- aciklama : String",
             "- tutar : double",
             "- tarih : String",
             "- kategori : Kategori"],
            ["+ Islem(aciklama, tutar, tarih, kategori)",
             "+ getId() : int",
             "+ getAciklama() : String",
             "+ getTutar() : double",
             "+ getTarih() : String",
             "+ getKategori() : Kategori",
             "+ setAciklama(aciklama) : void",
             "+ setTutar(tutar) : void",
             "+ setTarih(tarih) : void",
             "+ setKategori(kategori) : void",
             "+ gecerliTarih(tarih) : boolean   {static}",
             "+ ayYil() : String",
             "+ ay() : YearMonth",
             "+ getSayac() : int   {static}",
             "+ butceEtkisi() : double   {abstract}",
             "+ tip() : String   {abstract}",
             "+ paraYaz(deger) : String   {static}",
             "+ toString() : String"])

kat = kutu(470, 122, 300, "Kategori", None,
           ["- sayac : int   {static}",
            "- id : int",
            "- ad : String",
            "- tip : String"],
           ["+ Kategori(ad, tip)",
            "+ getId() : int",
            "+ getAd() : String",
            "+ getTip() : String",
            "+ setAd(ad) : void",
            "+ setTip(tip) : void",
            "+ getSayac() : int   {static}",
            "+ toString() : String"])

gel = kutu(70, 580, 300, "Gelir", None,
           ["- kaynak : String"],
           ["+ Gelir(aciklama, tutar, tarih,",
            "        kategori, kaynak)",
            "+ getKaynak() : String",
            "+ setKaynak(kaynak) : void",
            "+ butceEtkisi() : double",
            "+ tip() : String",
            "+ toString() : String"])

gid = kutu(400, 580, 300, "Gider", None,
           ["- odemeYontemi : String",
            "- zorunluMu : boolean"],
           ["+ Gider(aciklama, tutar, tarih, kategori,",
            "        odemeYontemi, zorunluMu)",
            "+ getOdemeYontemi() : String",
            "+ isZorunluMu() : boolean",
            "+ setOdemeYontemi(odemeYontemi) : void",
            "+ setZorunluMu(zorunluMu) : void",
            "+ butceEtkisi() : double",
            "+ tip() : String",
            "+ toString() : String"])

sab = kutu(400, 860, 300, "SabitGider", None,
           ["- odemeGunu : int"],
           ["+ SabitGider(aciklama, tutar, tarih, kategori,",
            "             odemeYontemi, odemeGunu)",
            "+ getOdemeGunu() : int",
            "+ setOdemeGunu(gun) : void",
            "+ tip() : String",
            "+ toString() : String"])

hes = kutu(70, 860, 300, "ButceHesabi", None,
           ["- sahip : String",
            "- ogrenciNo : String",
            "- aylikLimit : double",
            "- baslangicBakiye : double"],
           ["+ ButceHesabi(sahip, ogrenciNo,",
            "              aylikLimit, baslangicBakiye)",
            "+ getSahip() : String",
            "+ getOgrenciNo() : String",
            "+ getAylikLimit() : double",
            "+ getBaslangicBakiye() : double",
            "+ setSahip(sahip) : void",
            "+ setOgrenciNo(no) : void",
            "+ setBaslangicBakiye(bakiye) : void",
            "+ setAylikLimit(limit) : void",
            "+ limitAsildiMi(toplamGider) : boolean",
            "+ toString() : String"])

# ------------------------------------------------------------------ service + app
serv = kutu(860, 116, 680, "ButceService", None,
            ["- hesap : ButceHesabi",
             "- islemler : Islem[]",
             "- islemSayisi : int",
             "- kategoriler : Kategori[]",
             "- kategoriSayisi : int"],
            ["+ ButceService(hesap : ButceHesabi, kapasite : int)",
             "+ getHesap() : ButceHesabi",
             "+ getIslemSayisi() : int",
             "+ kategoriEkle(kategori : Kategori) : void",
             "+ islemEkle(islem : Islem) : boolean",
             "+ sonEklenenId() : int",
             "+ kategorileriListele() : void",
             "+ kategoriBul(ad : String) : Kategori",
             "+ getKategoriSayisi() : int",
             "+ tumIslemleriListele() : void",
             "+ toplamGelir() : double",
             "+ toplamGider() : double",
             "+ toplamGider(ay : YearMonth) : double",
             "+ netBakiye() : double",
             "+ tipAnalizi() : void",
             "+ butceOzeti() : void",
             "+ getSeciliAy() : YearMonth",
             "+ seciliAyAyarla(metin : String) : boolean",
             "+ enSonAyiSec() : void"])

mai = kutu(860, 656, 680, "Main", None,
           [],
           ["+ main(args : String[]) : void   {static}",
            "- ornekVerileriYukle(servis) : void   {static}",
            "- gelirEkle(servis, giris) : void   {static}",
            "- giderEkle(servis, giris) : void   {static}",
            "- satirOku(giris) : String   {static}",
            "- metindenSayi(metin) : double   {static}",
            "- aySec(servis, giris) : void   {static}",
            "- menuYazdir() : void   {static}"])

# ------------------------------------------------------------------ oklar
ok([(220, 580), (220, 562), (265, 562), (265, isle["y"] + isle["h"])], "kalinim")
ok([(550, 580), (550, 546), (330, 546), (330, isle["y"] + isle["h"])], "kalinim")
ok([(550, 860), (550, gid["y"] + gid["h"])], "kalinim")

ok([(470, 220), (430, 220)], "iliski")
yazi(459, 213, "1")
yazi(433, 213, "*")

ok([(860, 160), (770, 160)], "iliski")
yazi(775, 153, "1")
yazi(838, 153, "*")

ok([(860, 400), (430, 400)], "iliski")
yazi(760, 393, "*")

ok([(1540, 500), (1600, 500), (1600, 1155), (220, 1155), (220, hes["y"] + hes["h"])], "iliski")
yazi(200, 1149, "*")

ok([(1210, 656), (1210, serv["y"] + serv["h"])], "bagimlilik", kesikli=True)

# ------------------------------------------------------------------ aciklama
parcalar.append('<rect x="830" y="890" width="620" height="205" fill="#fdfbf3" '
                'stroke="#8a6d3b" stroke-width="1.2" stroke-dasharray="5 4"/>')
baslik(850, 916, "Okuma anahtarı", 12)
yazi(850, 940, "- private      + public      {static} sınıfa ait")
yazi(850, 962, "italik ad ve <<abstract>> : soyut sınıf ve soyut metot")
yazi(850, 984, "içi boş üçgen ok : kalıtım (extends)")
yazi(850, 1006, "kesikli ok : bağımlılık, bir sınıf diğerini kullanıyor")
yazi(850, 1028, "düz çizgi : ilişkilendirme, uçlardaki sayılar çokluk")
yazi(850, 1056, "Islem soyut olduğu için doğrudan nesnesi üretilemez.", 10, 'font-style="italic"')
yazi(850, 1076, "Islem[] dizisi Gelir, Gider ve SabitGider nesnelerini birlikte tutar.", 10, 'font-style="italic"')

svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">\n'
       '<rect width="%d" height="%d" fill="#ffffff"/>\n%s\n</svg>'
       % (W, H, W, H, W, H, "\n".join(parcalar)))

import os
KLASOR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(KLASOR, "uml.svg"), "w", encoding="utf-8") as f:
    f.write(svg)

html = ('<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8"><style>'
        '@page{size:A3 landscape;margin:0}html,body{margin:0;padding:0}'
        'svg{display:block;width:420mm;height:297mm}</style></head><body>%s</body></html>' % svg)
with open(os.path.join(KLASOR, "uml_baski.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("uml.svg ve uml_baski.html yazildi")
