package model;

/**
 * Kategori sinifi, bir islemin hangi basliga ait oldugunu tutar.
 * Ornek: Maas, Burs, Kira, Fatura, Market.
 * Her kategori olusturuldugunda static sayac bir artar ve id otomatik verilir.
 */
public class Kategori {

    // Sinifin tamamina ait sayac, her yeni kategoriye sira numarasi verir.
    private static int sayac = 0;

    private int id;
    private String ad;
    private String tip;   // "GELIR" veya "GIDER"

    /** Yeni bir Kategori nesnesi olusturur. */
    public Kategori(String ad, String tip) {
        sayac = sayac + 1;
        this.id = sayac;
        setAd(ad);
        this.tip = tip;
    }

    /** Id degerini dondurur. */
    public int getId() {
        return id;
    }

    /** Ad degerini dondurur. */
    public String getAd() {
        return ad;
    }

    /** Tip degerini dondurur. */
    public String getTip() {
        return tip;
    }

    /** Kategori adi bos birakilamaz. */
    public void setAd(String ad) {
        if (ad == null || ad.trim().equals("")) {
            System.out.println("Uyari: kategori adi bos olamaz, eski deger korundu.");
            return;
        }
        this.ad = ad;
    }

    /** Sayac degerini dondurur. */
    public static int getSayac() {
        return sayac;
    }

    /** Nesnenin ekranda gorunen metin karsiligini dondurur. */
    @Override
    public String toString() {
        return id + " - " + ad + " (" + tip + ")";
    }
}
