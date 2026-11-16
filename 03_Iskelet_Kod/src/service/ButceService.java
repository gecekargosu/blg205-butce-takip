package service;

import model.ButceHesabi;
import model.Gelir;
import model.Gider;
import model.Islem;
import model.Kategori;
import model.SabitGider;

/**
 * Is mantiginin toplandigi sinif. Main icine tek satir is mantigi yazmadim,
 * cunku yonerge is mantigini tek sinifa toplayan projelere tasarim puani vermiyor.
 *
 * Kayitlar su an sabit boyutlu dizide tutuluyor. Bu bilincli bir tercih,
 * cunku ArrayList konusu henuz islenmedi. Hafta 11'den sonra ArrayList'e
 * cevrilecek, metot imzalari ayni kalacagi icin disaridan bir sey degismeyecek.
 */
public class ButceService {

    private ButceHesabi hesap;
    private Islem[] islemler;      // polimorfik dizi, icinde Gelir de Gider de var
    private int islemSayisi;
    private Kategori[] kategoriler;
    private int kategoriSayisi;

    /** Yeni bir ButceService nesnesi olusturur. */
    public ButceService(ButceHesabi hesap, int kapasite) {
        this.hesap = hesap;
        this.islemler = new Islem[kapasite];
        this.kategoriler = new Kategori[kapasite];
        this.islemSayisi = 0;
        this.kategoriSayisi = 0;
    }

    /** Hesap degerini dondurur. */
    public ButceHesabi getHesap() {
        return hesap;
    }

    /** IslemSayisi degerini dondurur. */
    public int getIslemSayisi() {
        return islemSayisi;
    }

    /** kategoriEkle islemini yapar. */
    public void kategoriEkle(Kategori kategori) {
        if (kategoriSayisi >= kategoriler.length) {
            System.out.println("Uyari: kategori kapasitesi doldu.");
            return;
        }
        kategoriler[kategoriSayisi] = kategori;
        kategoriSayisi = kategoriSayisi + 1;
    }

    /**
     * Parametre Islem turunde. Cagirirken Gelir veya Gider gonderiyorum,
     * Java bunlari otomatik olarak ust tipe ceviriyor. Diziye de ust tipten
     * girdigi icin cok bicimlilik burada gerceklesiyor.
     */
    public void islemEkle(Islem islem) {
        if (islemSayisi >= islemler.length) {
            System.out.println("Uyari: islem kapasitesi doldu.");
            return;
        }
        islemler[islemSayisi] = islem;
        islemSayisi = islemSayisi + 1;
    }

    /**
     * Son eklenen kaydin id numarasini dondurur.
     * Ekleme ekraninda kullaniciya "#7 numarali kayit eklendi" demek icin.
     */
    public int sonEklenenId() {
        if (islemSayisi == 0) {
            return 0;
        }
        return islemler[islemSayisi - 1].getId();
    }

    /** tumIslemleriListele islemini yapar. */
    /**
     * Kayitli kategorileri numarasiyla ekrana yazar.
     * Kullanici gelir veya gider eklerken bu listeden secim yapiyor.
     */
    public void kategorileriListele() {
        System.out.println("Kategoriler: ");
        for (int i = 0; i < kategoriSayisi; i++) {
            System.out.println("  " + kategoriler[i]);
        }
    }

    /**
     * Verilen ada gore kategori arar. Buyuk kucuk harf farki gozetilmez.
     * Bulunamazsa null doner, cagiran taraf kaydi eklemez.
     */
    public Kategori kategoriBul(String ad) {
        if (ad == null) {
            return null;
        }
        for (int i = 0; i < kategoriSayisi; i++) {
            if (kategoriler[i].getAd().equalsIgnoreCase(ad.trim())) {
                return kategoriler[i];
            }
        }
        return null;
    }

    /** Kategori sayisini dondurur. */
    public int getKategoriSayisi() {
        return kategoriSayisi;
    }

    public void tumIslemleriListele() {
        System.out.println("------- KAYITLI ISLEMLER --------------------------------");
        if (islemSayisi == 0) {
            System.out.println("Henuz kayit yok.");
            return;
        }
        for (int i = 0; i < islemSayisi; i++) {
            System.out.println(islemler[i]);   // toString hangi alt sinifsa ona gore calisiyor
        }
        System.out.println("--------------------------------------------------------");
        System.out.println("Toplam kayit: " + islemSayisi);
    }

    /** butceEtkisi arti donen kayitlar gelir. */
    public double toplamGelir() {
        double toplam = 0;
        for (int i = 0; i < islemSayisi; i++) {
            if (islemler[i].butceEtkisi() > 0) {
                toplam = toplam + islemler[i].butceEtkisi();
            }
        }
        return toplam;
    }

    /** butceEtkisi eksi donen kayitlar gider. Toplami duz sayi olarak donduruyorum. */
    public double toplamGider() {
        double toplam = 0;
        for (int i = 0; i < islemSayisi; i++) {
            if (islemler[i].butceEtkisi() < 0) {
                toplam = toplam + (-islemler[i].butceEtkisi());
            }
        }
        return toplam;
    }

    /** netBakiye sonucunu hesaplayip dondurur. */
    public double netBakiye() {
        return hesap.getBaslangicBakiye() + toplamGelir() - toplamGider();
    }

    /**
     * Tur bazinda sayim. instanceof ile nesnenin gercek alt tipine bakiyorum.
     * SabitGider kontrolu once yapiliyor, cunku SabitGider ayni zamanda
     * bir Gider ve sira ters olursa hepsi gider sayilirdi.
     */
    public void tipAnalizi() {
        int gelirSayisi = 0;
        int giderSayisi = 0;
        int sabitSayisi = 0;

        for (int i = 0; i < islemSayisi; i++) {
            if (islemler[i] instanceof SabitGider) {
                sabitSayisi = sabitSayisi + 1;
            } else if (islemler[i] instanceof Gelir) {
                gelirSayisi = gelirSayisi + 1;
            } else if (islemler[i] instanceof Gider) {
                giderSayisi = giderSayisi + 1;
            }
        }

        System.out.println("---------------- ISLEM TURU ANALIZI ----------------");
        System.out.println("Gelir kaydi       : " + gelirSayisi);
        System.out.println("Gider kaydi       : " + giderSayisi);
        System.out.println("Sabit gider kaydi : " + sabitSayisi);
        System.out.println("Toplam            : " + islemSayisi);
    }

    /** butceOzeti islemini yapar. */
    public void butceOzeti() {
        double gelir = toplamGelir();
        double gider = toplamGider();
        double net = netBakiye();

        System.out.println("------------------- BUTCE OZETI -------------------");
        System.out.println("Hesap            : " + hesap.toString());
        System.out.println("Baslangic bakiye :   +" + Islem.paraYaz(hesap.getBaslangicBakiye()) + " TL");
        System.out.println("Toplam gelir     :  +" + Islem.paraYaz(gelir) + " TL");
        System.out.println("Toplam gider     :  -" + Islem.paraYaz(gider) + " TL");

        if (net < 0) {
            System.out.println("Net bakiye       :  -" + Islem.paraYaz(net) + " TL");
        } else {
            System.out.println("Net bakiye       :  +" + Islem.paraYaz(net) + " TL");
        }

        System.out.println("Aylik limit      :   " + Islem.paraYaz(hesap.getAylikLimit()) + " TL");

        if (hesap.limitAsildiMi(gider)) {
            System.out.println("Limit durumu     : Sinir asildi");
        } else {
            System.out.println("Limit durumu     : Sinir asilmadi");
        }
    }
}
