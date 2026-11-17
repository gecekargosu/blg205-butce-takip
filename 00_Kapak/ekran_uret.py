"""
Konsol ciktisini terminal gorunumlu PNG dosyasina cevirir.
Rapordaki ekran goruntusu sekilleri bu betikle uretilir.
Kullanim: python ekran_uret.py <cikti.txt> <hedef.png> <baslik> [satir_sayisi]
"""
import html
import os
import subprocess
import sys
import tempfile

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

SABLON = """<!doctype html>
<html lang="tr"><head><meta charset="utf-8">
<style>
  html, body {{ margin:0; padding:0; background:#1b1b1b; }}
  .pencere {{ margin:18px; border-radius:8px; overflow:hidden;
              box-shadow:0 6px 18px rgba(0,0,0,.45); background:#0c0c0c; }}
  .cubuk {{ background:#2b2b2b; padding:7px 12px; font:13px "Segoe UI",Arial;
            color:#c9c9c9; }}
  .nokta {{ display:inline-block; width:9px; height:9px; border-radius:50%;
            background:#ff5f56; margin-right:5px; }}
  .nokta.s {{ background:#ffbd2e; }} .nokta.y {{ background:#27c93f; }}
  .baslik {{ margin-left:10px; }}
  pre {{ margin:0; padding:14px 16px 18px; color:#d6d6d6; background:#0c0c0c;
         font:13.2px/1.42 Consolas,"Courier New",monospace; white-space:pre-wrap; }}
</style></head><body>
<div class="pencere">
  <div class="cubuk"><span class="nokta"></span><span class="nokta s"></span><span class="nokta y"></span>
    <span class="baslik">{baslik}</span></div>
  <pre>{metin}</pre>
</div>
</body></html>
"""


def uret(kaynak, hedef, baslik, satir_sayisi=30):
    with open(kaynak, encoding="utf-8", errors="replace") as dosya:
        satirlar = dosya.read().replace("\r", "").split("\n")
    satirlar = [s.rstrip() for s in satirlar if s.strip() != ""]
    satirlar = satirlar[:satir_sayisi]
    satir_sayisi = len(satirlar)
    metin = html.escape("\n".join(satirlar))

    gecici = os.path.join(tempfile.gettempdir(), "ekran_gecici.html")
    with open(gecici, "w", encoding="utf-8") as dosya:
        dosya.write(SABLON.format(baslik=html.escape(baslik), metin=metin))

    yukseklik = 104 + satir_sayisi * 19
    subprocess.run([
        CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
        "--hide-scrollbars", "--force-device-scale-factor=2",
        "--window-size=1180,%d" % yukseklik,
        "--screenshot=" + os.path.abspath(hedef),
        "file:///" + gecici.replace("\\", "/"),
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("yazildi:", hedef)


if __name__ == "__main__":
    satir = int(sys.argv[4]) if len(sys.argv) > 4 else 30
    uret(sys.argv[1], sys.argv[2], sys.argv[3], satir)
