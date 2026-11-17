package model;

import java.time.LocalDate;
import java.time.YearMonth;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.format.ResolverStyle;

/**
 * Gelir ve gider kayitlarinin ortak ust sinifi.
 * Bu sinif soyut cunku tek basina bir islem anlami yok.
 * Islemin gelir mi gider mi olduguna alt siniflar karar veriyor.
 *
 * Id uretimi icin static sayac kullaniliyor. Boylece her yeni islem
 * kendi numarasini otomatik aliyor, programin baska yerinde numara tutmak
 * gerekmiyor.
  *
  * @author Cengiz Kilic
 */
public abstract class Islem {

    private static int sayac = 0;

    private int id;
    private String aciklama;
    private double tutar;
    private String tarih;          // gg.aa.yyyy biciminde metin

    /** Tarihlerin beklenen bicimi. Hem dogrulamada hem ay filtresinde kullanilir. */
    private static final DateTimeFormatter TARIH_BICIMI =
            DateTimeFormatter.ofPattern("dd.MM.uuuu").withResolverStyle(ResolverStyle.STRICT);

    /** 1.1.2026 gibi tek haneli gun ve ay yazimlarini da kabul eden ikinci bicim. */
    private static final DateTimeFormatter TARIH_BICIMI_KISA =
            DateTimeFormatter.ofPattern("d.M.uuuu").withResolverStyle(ResolverStyle.STRICT);

    /** Ay filtresi icin kullanilan bicim: 11.2026 */
    private static final DateTimeFormatter AY_BICIMI =
            DateTimeFormatter.ofPattern("MM.uuuu").withResolverStyle(ResolverStyle.STRICT);
    private Kategori kategori;

    /** Yeni bir Islem nesnesi olusturur. */
    public Islem(String aciklama, double tutar, String tarih, Kategori kategori) {
        sayac = sayac + 1;
        this.id = sayac;
        setAciklama(aciklama);
        setTutar(tutar);
        setTarih(tarih);
        setKategori(kategori);
    }

    /** Id degerini dondurur. */
    public int getId() {
        return id;
    }

    /** Aciklama degerini dondurur. */
    public String getAciklama() {
        return aciklama;
    }

    /** Tutar degerini dondurur. */
    public double getTutar() {
        return tutar;
    }

    /** Tarih degerini dondurur. */
    public String getTarih() {
        return tarih;
    }

    /** Kategori degerini dondurur. */
    public Kategori getKategori() {
        return kategori;
    }

    /** Aciklama bos birakilamaz. */
    public void setAciklama(String aciklama) {
        if (aciklama == null || aciklama.trim().equals("")) {
            System.out.println("Uyari: aciklama bos birakilamaz, eski deger korundu.");
            return;
        }
        this.aciklama = aciklama;
    }

    /** Tutar sifir veya eksi olamaz. */
    public void setTutar(double tutar) {
        if (tutar <= 0) {
            System.out.println("Uyari: tutar sifir veya eksi olamaz, eski deger korundu.");
            return;
        }
        this.tutar = tutar;
    }

    /**
     * Tarihi dogrular ve atar. gg.aa.yyyy biciminde olmayan metin reddedilir,
     * eski deger korunur. Dogrulama java.time.LocalDate ile yapiliyor.
     */
    public void setTarih(String tarih) {
        if (!gecerliTarih(tarih)) {
            System.out.println("Uyari: tarih gg.aa.yyyy biciminde olmali, eski deger korundu.");
            return;
        }
        this.tarih = tarih;
    }

    /** Kategori null olamaz, eski deger korunur. */
    public void setKategori(Kategori kategori) {
        if (kategori == null) {
            System.out.println("Uyari: kategori bos olamaz, eski deger korundu.");
            return;
        }
        this.kategori = kategori;
    }

    /**
     * Metnin gg.aa.yyyy biciminde gecerli bir tarih olup olmadigini soyler.
     * 31.02.2026 gibi takvimde olmayan gunler de reddedilir.
     */
    public static boolean gecerliTarih(String tarih) {
        if (tarih == null || tarih.trim().equals("")) {
            return false;
        }
        try {
            LocalDate.parse(tarih.trim(), TARIH_BICIMI);
            return true;
        } catch (DateTimeParseException hata) {
            try {
                LocalDate.parse(tarih.trim(), TARIH_BICIMI_KISA);
                return true;
            } catch (DateTimeParseException ikinciHata) {
                return false;
            }
        }
    }

    /** Ay filtresi icin tarihin ay ve yilini MM.yyyy biciminde dondurur. */
    public String ayYil() {
        return ay().format(AY_BICIMI);
    }

    /** Tarihi YearMonth olarak dondurur, karsilastirma ve filtre bunu kullanir. */
    public YearMonth ay() {
        String temiz = tarih.trim();
        try {
            return YearMonth.from(LocalDate.parse(temiz, TARIH_BICIMI));
        } catch (DateTimeParseException hata) {
            return YearMonth.from(LocalDate.parse(temiz, TARIH_BICIMI_KISA));
        }
    }

    /** Sayac degerini dondurur. */
    public static int getSayac() {
        return sayac;
    }

    // Bu islemin butceye etkisi. Gelirde arti, giderde eksi doner.
    /** Govdesi yok, cunku her alt sinif kendi isaretini kendisi biliyor. */
    public abstract double butceEtkisi();

    /** Islemin turu. Ekranda yazilan etiketi alt sinif belirliyor. */
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
