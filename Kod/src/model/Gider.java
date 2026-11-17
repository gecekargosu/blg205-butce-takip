package model;

/**
 * Gider kaydi. Islem sinifindan tureiyor ve butceye eksi yonde etki ediyor.
 * Odeme yontemi ve zorunlu olup olmadigi gidere ozgu alanlar.
  *
  * @author Cengiz Kilic
 */
public class Gider extends Islem {

    private String odemeYontemi;
    private boolean zorunluMu;

    /** Yeni bir Gider nesnesi olusturur. */
    public Gider(String aciklama, double tutar, String tarih, Kategori kategori,
                 String odemeYontemi, boolean zorunluMu) {
        super(aciklama, tutar, tarih, kategori);
        setOdemeYontemi(odemeYontemi);
        this.zorunluMu = zorunluMu;
    }

    /** OdemeYontemi degerini dondurur. */
    public String getOdemeYontemi() {
        return odemeYontemi;
    }

    /** Giderin zorunlu olup olmadigini soyler. */
    public boolean isZorunluMu() {
        return zorunluMu;
    }

    /** OdemeYontemi degerini dogrulayarak atar. */
    public void setOdemeYontemi(String odemeYontemi) {
        if (odemeYontemi == null || odemeYontemi.trim().equals("")) {
            System.out.println("Uyari: odeme yontemi bos olamaz, eski deger korundu.");
            return;
        }
        this.odemeYontemi = odemeYontemi;
    }

    /** ZorunluMu degerini dogrulayarak atar. */
    public void setZorunluMu(boolean zorunluMu) {
        this.zorunluMu = zorunluMu;
    }

    /**
     * Gider butceyi azaltir, bu yuzden tutar eksi olarak donuyor.
     * Gelir sinifinda ayni metot arti donuyor.
     */
    @Override
    public double butceEtkisi() {
        return -getTutar();
    }

    /** Ekranda yazilan islem turu. */
    @Override
    public String tip() {
        return "Gider";
    }

    /** Nesnenin ekranda gorunen metin karsiligini dondurur. */
    @Override
    public String toString() {
        return super.toString() + " | Odeme: " + odemeYontemi;
    }
}
