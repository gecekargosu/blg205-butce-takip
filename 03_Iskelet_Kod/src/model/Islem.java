package model;

/**
 * Gelir ve gider kayitlarinin ortak ust sinifi.
 * Bu sinif soyut cunku tek basina bir islem anlami yok.
 * Islemin gelir mi gider mi olduguna alt siniflar karar veriyor.
 *
 * Id uretimi icin static sayac kullaniliyor. Boylece her yeni islem
 * kendi numarasini otomatik aliyor, programin baska yerinde numara tutmak
 * gerekmiyor.
 */
public abstract class Islem {

    private static int sayac = 0;

    private int id;
    private String aciklama;
    private double tutar;
    private String tarih;          // gg.aa.yyyy biciminde metin
    private Kategori kategori;

    public Islem(String aciklama, double tutar, String tarih, Kategori kategori) {
        sayac = sayac + 1;
        this.id = sayac;
        setAciklama(aciklama);
        setTutar(tutar);
        this.tarih = tarih;
        this.kategori = kategori;
    }

    public int getId() {
        return id;
    }

    public String getAciklama() {
        return aciklama;
    }

    public double getTutar() {
        return tutar;
    }

    public String getTarih() {
        return tarih;
    }

    public Kategori getKategori() {
        return kategori;
    }

    // Aciklama bos birakilamaz.
    public void setAciklama(String aciklama) {
        if (aciklama == null || aciklama.trim().equals("")) {
            System.out.println("Uyari: aciklama bos birakilamaz, eski deger korundu.");
            return;
        }
        this.aciklama = aciklama;
    }

    // Tutar sifir veya eksi olamaz.
    public void setTutar(double tutar) {
        if (tutar <= 0) {
            System.out.println("Uyari: tutar sifir veya eksi olamaz, eski deger korundu.");
            return;
        }
        this.tutar = tutar;
    }

    public static int getSayac() {
        return sayac;
    }

    // Bu islemin butceye etkisi. Gelirde arti, giderde eksi doner.
    // Govdesi yok, cunku her alt sinif kendi isaretini kendisi biliyor.
    public abstract double butceEtkisi();

    // Islemin turu. Ekranda yazilan etiketi alt sinif belirliyor.
    public abstract String tip();

    /**
     * Parayi nokta ayirici ile yazar. Metot static, cunku bir nesneye
     * bagli degil, sadece sayiyi bicimlendiriyor.
     */
    public static String paraYaz(double deger) {
        long kurus = Math.round(Math.abs(deger) * 100);
        long tam = kurus / 100;
        long kalan = kurus % 100;
        String sonuc = "" + tam + ".";
        if (kalan < 10) {
            sonuc = sonuc + "0";
        }
        return sonuc + kalan;
    }

    /**
     * Ekranda gorunen satir. Alt siniflar bunu super.toString() ile
     * genisletiyor, yani ortak kismi bir kere burada yaziyorum.
     */
    @Override
    public String toString() {
        String kategoriAdi = "yok";
        if (kategori != null) {
            kategoriAdi = kategori.getAd();
        }

        String isaret = "+";
        if (butceEtkisi() < 0) {
            isaret = "-";
        }

        return "#" + id + " | " + tip() + " | " + tarih + " | " + aciklama
                + " | " + isaret + paraYaz(tutar) + " TL | Kategori: " + kategoriAdi;
    }
}
