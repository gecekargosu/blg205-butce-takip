package model;

/**
 * Butce hesabinin kimligi ve siniri. Ucuz bir sinif gibi gorunuyor ama
 * hesap bilgilerini islemlerden ayirdim, cunku islem listesi ile
 * hesap bilgisi ayri sorumluluklar.
 */
public class ButceHesabi {

    private String sahip;
    private String ogrenciNo;
    private double aylikLimit;
    private double baslangicBakiye;

    public ButceHesabi(String sahip, String ogrenciNo, double aylikLimit, double baslangicBakiye) {
        this.sahip = sahip;
        this.ogrenciNo = ogrenciNo;
        setAylikLimit(aylikLimit);
        this.baslangicBakiye = baslangicBakiye;
    }

    public String getSahip() {
        return sahip;
    }

    public String getOgrenciNo() {
        return ogrenciNo;
    }

    public double getAylikLimit() {
        return aylikLimit;
    }

    public double getBaslangicBakiye() {
        return baslangicBakiye;
    }

    // Aylik limit sifir veya eksi olamaz.
    public void setAylikLimit(double aylikLimit) {
        if (aylikLimit <= 0) {
            System.out.println("Uyari: aylik limit sifir veya eksi olamaz, eski deger korundu.");
            return;
        }
        this.aylikLimit = aylikLimit;
    }

    // Toplam gider limiti gectiyse true doner.
    public boolean limitAsildiMi(double toplamGider) {
        if (toplamGider > aylikLimit) {
            return true;
        }
        return false;
    }

    @Override
    public String toString() {
        return sahip + " " + ogrenciNo;
    }
}
