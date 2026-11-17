package app;

import java.util.Scanner;

import model.ButceHesabi;
import model.Gelir;
import model.Gider;
import model.Islem;
import model.Kategori;
import model.SabitGider;
import service.ButceService;

/**
 * Programin baslangic noktasi. Burada is mantigi yok,
 * sadece menu ve ornek veriler var. Hesaplamalarin hepsi ButceService icinde.
  *
  * @author Cengiz Kilic
 */
public class Main {

    /** Menuyu calistiran giris noktasi. */
    public static void main(String[] args) {
        ButceHesabi hesap = new ButceHesabi("Cengiz Kilic", "251205027", 25000.0, 5000.0);
        ButceService servis = new ButceService(hesap, 100);

        ornekVerileriYukle(servis);
        servis.enSonAyiSec();   // sunumda ozet bos gorunmesin, en son ay acilir

        Scanner giris = new Scanner(System.in);
        boolean calisiyor = true;

        while (calisiyor) {
            menuYazdir();
            if (!giris.hasNextLine()) {
                System.out.println("Giris akisi bitti, program kapatiliyor.");
                break;
            }
            String secim = giris.nextLine().trim();

            if (secim.equals("1")) {
                servis.tumIslemleriListele();
            } else if (secim.equals("2")) {
                servis.butceOzeti();
            } else if (secim.equals("3")) {
                servis.tipAnalizi();
            } else if (secim.equals("4")) {
                gelirEkle(servis, giris);
            } else if (secim.equals("5")) {
                giderEkle(servis, giris);
            } else if (secim.equals("6")) {
                aySec(servis, giris);
            } else if (secim.equals("0")) {
                System.out.println("Program kapatiliyor.");
                calisiyor = false;
            } else {
                System.out.println("Gecersiz secim. Menudeki bir numarayi girin.");
            }
        }

        giris.close();
    }

    /**
     * Acilista ornek kayitlari ekliyor. Boylece menu ilk acildiginda
     * liste bos gorunmuyor. Menu 4 ve 5 ile kullanici kendi kayitlarini da
     * ekleyebiliyor, ornek kayitlar yalnizca baslangic icin var.
     */
    private static void ornekVerileriYukle(ButceService servis) {
        Kategori maas = new Kategori("Maas", "GELIR");
        Kategori burs = new Kategori("Burs", "GELIR");
        Kategori kira = new Kategori("Kira", "GIDER");
        Kategori fatura = new Kategori("Fatura", "GIDER");
        Kategori market = new Kategori("Market", "GIDER");

        servis.kategoriEkle(maas);
        servis.kategoriEkle(burs);
        servis.kategoriEkle(kira);
        servis.kategoriEkle(fatura);
        servis.kategoriEkle(market);

        servis.islemEkle(new Gelir("Proje geliri", 32000.0, "01.11.2026", maas, "Serbest"));
        servis.islemEkle(new Gelir("Burs", 6000.0, "05.11.2026", burs, "Burs"));
        servis.islemEkle(new SabitGider("Ev kirasi", 12500.0, "05.11.2026", kira, "Havale", 5));
        servis.islemEkle(new SabitGider("Internet faturasi", 650.0, "10.11.2026", fatura, "Otomatik odeme", 10));
        servis.islemEkle(new Gider("Market alisverisi", 2450.0, "12.11.2026", market, "Kredi karti", false));
        servis.islemEkle(new Gider("Java kitabi", 580.0, "14.11.2026", market, "Nakit", false));
    }

    /**
     * Kullanicidan gelir bilgilerini alip listeye ekler.
     * Gecersiz tutar veya olmayan kategori girilirse kayit eklenmez,
     * program cokmez, menuye geri doner.
     */
    private static void gelirEkle(ButceService servis, Scanner giris) {
        System.out.println("------------------ YENI GELIR ------------------");
        servis.kategorileriListele();
        System.out.print("Aciklama       : ");
        String aciklama = satirOku(giris).trim();
        System.out.print("Tutar (TL)     : ");
        double tutar = metindenSayi(satirOku(giris));
        System.out.print("Tarih          : ");
        String tarih = satirOku(giris).trim();
        System.out.print("Kategori adi   : ");
        Kategori kategori = servis.kategoriBul(satirOku(giris));
        System.out.print("Kaynak         : ");
        String kaynak = satirOku(giris).trim();

        if (tutar <= 0) {
            System.out.println("Hata: tutar sifirdan buyuk bir sayi olmali. Kayit eklenmedi.");
            return;
        }
        if (kategori == null) {
            System.out.println("Hata: boyle bir kategori yok. Kayit eklenmedi.");
            return;
        }
        if (aciklama.equals("")) {
            System.out.println("Hata: aciklama bos olamaz. Kayit eklenmedi.");
            return;
        }
        if (kaynak.equals("")) {
            System.out.println("Hata: kaynak bos olamaz. Kayit eklenmedi.");
            return;
        }
        if (!kategori.getTip().equals("GELIR")) {
            System.out.println("Hata: " + kategori.getAd() + " bir gider kategorisi, gelire eklenemez. Kayit eklenmedi.");
            return;
        }
        if (!Islem.gecerliTarih(tarih)) {
            System.out.println("Hata: tarih gg.aa.yyyy biciminde olmali (ornek 16.11.2026). Kayit eklenmedi.");
            return;
        }

        boolean eklendi = servis.islemEkle(new Gelir(aciklama, tutar, tarih, kategori, kaynak));
        if (!eklendi) {
            System.out.println("Hata: kayit eklenemedi.");
            return;
        }
        System.out.println("Kayit eklendi. Numara: #" + servis.sonEklenenId());
    }

    /**
     * Kullanicidan gider bilgilerini alip listeye ekler.
     * Gelir eklemeyle ayni dogrulama kurallarini kullanir.
     */
    private static void giderEkle(ButceService servis, Scanner giris) {
        System.out.println("------------------ YENI GIDER ------------------");
        servis.kategorileriListele();
        System.out.print("Aciklama       : ");
        String aciklama = satirOku(giris).trim();
        System.out.print("Tutar (TL)     : ");
        double tutar = metindenSayi(satirOku(giris));
        System.out.print("Tarih          : ");
        String tarih = satirOku(giris).trim();
        System.out.print("Kategori adi   : ");
        Kategori kategori = servis.kategoriBul(satirOku(giris));
        System.out.print("Odeme yontemi  : ");
        String odeme = satirOku(giris).trim();

        if (tutar <= 0) {
            System.out.println("Hata: tutar sifirdan buyuk bir sayi olmali. Kayit eklenmedi.");
            return;
        }
        if (kategori == null) {
            System.out.println("Hata: boyle bir kategori yok. Kayit eklenmedi.");
            return;
        }
        if (aciklama.equals("")) {
            System.out.println("Hata: aciklama bos olamaz. Kayit eklenmedi.");
            return;
        }
        if (odeme.equals("")) {
            System.out.println("Hata: odeme yontemi bos olamaz. Kayit eklenmedi.");
            return;
        }
        if (!kategori.getTip().equals("GIDER")) {
            System.out.println("Hata: " + kategori.getAd() + " bir gelir kategorisi, gidere eklenemez. Kayit eklenmedi.");
            return;
        }
        if (!Islem.gecerliTarih(tarih)) {
            System.out.println("Hata: tarih gg.aa.yyyy biciminde olmali (ornek 16.11.2026). Kayit eklenmedi.");
            return;
        }

        boolean eklendi = servis.islemEkle(new Gider(aciklama, tutar, tarih, kategori, odeme, false));
        if (!eklendi) {
            System.out.println("Hata: kayit eklenemedi.");
            return;
        }
        System.out.println("Kayit eklendi. Numara: #" + servis.sonEklenenId());
    }

    /**
     * Bir satir okur. Girdi akisi bittiyse bos metin doner,
     * boylece program istisna firlatip cokmez.
     */
    private static String satirOku(Scanner giris) {
        if (giris.hasNextLine()) {
            return giris.nextLine();
        }
        return "";
    }

    /**
     * Kullanicinin yazdigi metni sayiya cevirir.
     * Hem nokta hem virgul ondalik ayirici olarak kabul edilir.
     * Metin sayi degilse -1 doner, boylece cagiran taraf kaydi eklemez.
     */
    private static double metindenSayi(String metin) {
        if (metin == null) {
            return -1;
        }
        String temiz = metin.trim().replace(",", ".");
        if (!temiz.matches("[0-9]+(\\.[0-9]{1,2})?")) {
            return -1;
        }
        return Double.parseDouble(temiz);
    }

    /**
     * Butce ozeti ve aylik limit icin kullanilan ayi degistirir.
     * Sunumda farkli bir ay gostermek gerektiginde kullanilir.
     */
    private static void aySec(ButceService servis, Scanner giris) {
        System.out.print("Ay (MM.yyyy, ornek 11.2026): ");
        String metin = satirOku(giris).trim();
        if (servis.seciliAyAyarla(metin)) {
            System.out.println("Ozet ayi " + servis.getSeciliAy().format(java.time.format.DateTimeFormatter.ofPattern("MM.yyyy")) + " olarak degistirildi.");
        } else {
            System.out.println("Hata: ay MM.yyyy biciminde olmali. Eski ay korundu.");
        }
    }

    private static void menuYazdir() {
        System.out.println("");
        System.out.println("=======================================================");
        System.out.println("     KISISEL GELIR GIDER VE BUTCE TAKIP SISTEMI");
        System.out.println("=======================================================");
        System.out.println("1) Tum islemleri listele");
        System.out.println("2) Butce ozeti");
        System.out.println("3) Islem turu analizi");
        System.out.println("4) Yeni gelir ekle");
        System.out.println("5) Yeni gider ekle");
        System.out.println("6) Ozet ayini sec (MM.yyyy)");
        System.out.println("0) Cikis");
        System.out.print("Seciminiz: ");
    }
}
