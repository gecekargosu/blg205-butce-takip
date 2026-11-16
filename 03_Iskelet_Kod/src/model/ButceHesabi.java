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

    /** Yeni bir ButceHesabi nesnesi olusturur. */
    public ButceHesabi(String sahip, String ogrenciNo, double aylikLimit, double baslangicBakiye) {
        setSahip(sahip);
        setOgrenciNo(ogrenciNo);
        setAylikLimit(aylikLimit);
        setBaslangicBakiye(baslangicBakiye);
    }

    /** Sahip degerini dondurur. */
    public String getSahip() {
        return sahip;
    }

    /** OgrenciNo degerini dondurur. */
    public String getOgrenciNo() {
        return ogrenciNo;
    }

    /** AylikLimit degerini dondurur. */
    public double getAylikLimit() {
        return aylikLimit;
    }

    /** BaslangicBakiye degerini dondurur. */
    public double getBaslangicBakiye() {
        return baslangicBakiye;
    }

    /** Hesap sahibi bos olamaz. */
    public void setSahip(String sahip) {
        if (sahip == null || sahip.trim().equals("")) {
            System.out.println("Uyari: hesap sahibi bos olamaz, eski deger korundu.");
            return;
        }
        this.sahip = sahip;
    }

    /** Ogrenci numarasi bos olamaz ve yalnizca rakam icerir. */
    public void setOgrenciNo(String ogrenciNo) {
        if (ogrenciNo == null || !ogrenciNo.trim().matches("[0-9]{6,12}")) {
            System.out.println("Uyari: ogrenci numarasi 6-12 haneli sayi olmali, eski deger korundu.");
            return;
        }
        this.ogrenciNo = ogrenciNo.trim();
    }

    /** Baslangic bakiyesi eksi olamaz. */
    public void setBaslangicBakiye(double baslangicBakiye) {
        if (baslangicBakiye < 0) {
            System.out.println("Uyari: baslangic bakiyesi eksi olamaz, eski deger korundu.");
            return;
        }
        this.baslangicBakiye = baslangicBakiye;
    }

    /** Aylik limit sifir veya eksi olamaz. */
    public void setAylikLimit(double aylikLimit) {
        if (aylikLimit <= 0) {
            System.out.println("Uyari: aylik limit sifir veya eksi olamaz, eski deger korundu.");
            return;
        }
        this.aylikLimit = aylikLimit;
    }

    /** Toplam gider limiti gectiyse true doner. */
    public boolean limitAsildiMi(double toplamGider) {
        if (toplamGider > aylikLimit) {
            return true;
        }
        return false;
    }

    /** Nesnenin ekranda gorunen metin karsiligini dondurur. */
    @Override
    public String toString() {
        return sahip + " " + ogrenciNo;
    }
}
