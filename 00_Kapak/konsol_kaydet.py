"""Konsol kayitlarini yeniden uretir.

Programi boru hattiyla calistirir, kullanicinin yazdigi degerleri istemlerin
yanina yerlestirir. Boylece rapora giren ekran goruntuleri gercek oturumdur.
Kullanim: python 00_Kapak/konsol_kaydet.py
"""
import subprocess
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
KAYIT = KOK / "Kod" / "konsol-kayitlari"
JAVA = r"C:/Program Files/Java/jdk-25/bin/java.exe"
SINIF = KOK / "Kod" / "build"


def oturum(ad, komutlar):
    """Tek bir oturumu calistirip istem ve cevaplarla birlikte kaydeder."""
    surec = subprocess.run(
        [JAVA, "-Dfile.encoding=UTF-8", "-cp", str(SINIF), "app.Main"],
        input="\n".join(deger for _, deger in komutlar) + "\n",
        capture_output=True, text=True, encoding="utf-8",
    )
    metin = surec.stdout.replace("\r\n", "\n")
    konum = 0
    parcalar = []
    for istem, deger in komutlar:
        bulundu = metin.find(istem, konum)
        if bulundu < 0:
            raise SystemExit("%s: istem bulunamadi %r" % (ad, istem))
        bulundu += len(istem)
        parcalar.append(metin[konum:bulundu])
        parcalar.append(deger + "\n")
        konum = bulundu
    parcalar.append(metin[konum:])
    sonuc = "".join(parcalar)
    (KAYIT / ad).write_text(sonuc, encoding="utf-8", newline="\r\n")
    print(ad, "->", len(sonuc.splitlines()), "satir")


SEC = "Seciminiz: "

oturum("e.txt", [
    (SEC, "1"), (SEC, "2"), (SEC, "3"), (SEC, "0"),
])

oturum("a.txt", [
    (SEC, "4"),
    ("Aciklama       : ", "Kitap telifi"),
    ("Tutar (TL)     : ", "1500,50"),
    ("Tarih          : ", "15.11.2026"),
    ("Kategori adi   : ", "Maas"),
    ("Kaynak         : ", "Telif"),
    (SEC, "0"),
])

oturum("d.txt", [
    (SEC, "5"),
    ("Aciklama       : ", "Kirtasiye"),
    ("Tutar (TL)     : ", "350"),
    ("Tarih          : ", "13.11.2026"),
    ("Kategori adi   : ", "Market"),
    ("Odeme yontemi  : ", "Nakit"),
    (SEC, "0"),
])

oturum("b.txt", [
    (SEC, "4"),
    ("Aciklama       : ", "Deneme kaydi"),
    ("Tutar (TL)     : ", "abc"),
    ("Tarih          : ", "13.11.2026"),
    ("Kategori adi   : ", "Maas"),
    ("Kaynak         : ", "Serbest"),
    (SEC, "0"),
])

oturum("c.txt", [
    (SEC, "5"),
    ("Aciklama       : ", "Deneme kaydi"),
    ("Tutar (TL)     : ", "350"),
    ("Tarih          : ", "13.11.2026"),
    ("Kategori adi   : ", "Yok"),
    ("Odeme yontemi  : ", "Nakit"),
    (SEC, "0"),
])
