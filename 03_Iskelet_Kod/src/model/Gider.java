package model;

/**
 * Gider kaydi. Islem sinifindan tureiyor ve butceye eksi yonde etki ediyor.
 * Odeme yontemi ve zorunlu olup olmadigi gidere ozgu alanlar.
 */
public class Gider extends Islem {

    private String odemeYontemi;
    private boolean zorunluMu;

    public Gider(String aciklama, double tutar, String tarih, Kategori kategori,
                 String odemeYontemi, boolean zorunluMu) {
        super(aciklama, tutar, tarih, kategori);
        setOdemeYontemi(odemeYontemi);
        this.zorunluMu = zorunluMu;
    }

    public String getOdemeYontemi() {
        return odemeYontemi;
    }

    public boolean isZorunluMu() {
        return zorunluMu;
    }

    public void setOdemeYontemi(String odemeYontemi) {
        if (odemeYontemi == null || odemeYontemi.trim().equals("")) {
            System.out.println("Uyari: odeme yontemi bos olamaz, eski deger korundu.");
            return;
        }
        this.odemeYontemi = odemeYontemi;
    }

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

    @Override
    public String tip() {
        return "Gider";
    }

    @Override
    public String toString() {
        return super.toString() + " | Odeme: " + odemeYontemi;
    }
}
