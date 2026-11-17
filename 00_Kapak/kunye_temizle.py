"""Teslim PDF'lerinin kunyesini bosaltir.

Kullanim: python 00_Kapak/kunye_temizle.py [dosya ...]
Dosya verilmezse projedeki teslim PDF'leri temizlenir.
"""
import os
import sys

import pypdf


def temizle(yol):
    okuyucu = pypdf.PdfReader(yol)
    yazici = pypdf.PdfWriter()
    for sayfa in okuyucu.pages:
        yazici.add_page(sayfa)
    bilgi = yazici._info.get_object()
    for anahtar in list(bilgi.keys()):
        del bilgi[anahtar]
    gecici = yol + ".tmp"
    with open(gecici, "wb") as dosya:
        yazici.write(dosya)
    os.replace(gecici, yol)
    print("temizlendi:", yol, len(okuyucu.pages), "sayfa")


if __name__ == "__main__":
    hedefler = sys.argv[1:]
    if not hedefler:
        hedefler = ["Rapor.pdf", "UML/UML_Sinif_Diyagrami.pdf", "Kalan_Isler/Kalan_Isler_ve_Takvim.pdf"]
    for yol in hedefler:
        temizle(yol)
