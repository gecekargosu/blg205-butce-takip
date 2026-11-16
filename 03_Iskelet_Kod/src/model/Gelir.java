package model;

/**
 * Gelir kaydi. Islem sinifindan tureiyor ve butceye arti yonde etki ediyor.
 * Gelire ozgu tek alan kaynak: maas, burs, proje gibi.
 */
public class Gelir extends Islem {

    private String kaynak;

    public Gelir(String aciklama, double tutar, String tarih, Kategori kategori, String kaynak) {
        super(aciklama, tutar, tarih, kategori);   // ortak alanlari ust sinif dolduruyor
        setKaynak(kaynak);
    }

    public String getKaynak() {
        return kaynak;
    }

    // Kaynak bos birakilamaz.
    public void setKaynak(String kaynak) {
        if (kaynak == null || kaynak.trim().equals("")) {
            System.out.println("Uyari: gelir kaynagi bos olamaz, eski deger korundu.");
            return;
        }
        this.kaynak = kaynak;
    }

    /**
     * Gelir butceyi artirir. Bu yuzden tutar oldugu gibi donuyor.
     * Ayni metot Gider sinifinda eksi donuyor, cok bicimlilik burada gorunuyor.
     */
    @Override
    public double butceEtkisi() {
        return getTutar();
    }

    @Override
    public String tip() {
        return "Gelir";
    }

    // Ust sinifin satirini alip sonuna kaynagi ekliyorum.
    @Override
    public String toString() {
        return super.toString() + " | Kaynak: " + kaynak;
    }
}
