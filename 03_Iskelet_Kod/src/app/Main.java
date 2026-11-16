package app;

import java.util.Scanner;

import model.ButceHesabi;
import model.Gelir;
import model.Gider;
import model.Kategori;
import model.SabitGider;
import service.ButceService;

/**
 * Programin baslangic noktasi. Burada is mantigi yok,
 * sadece menu ve ornek veriler var. Hesaplamalarin hepsi ButceService icinde.
 */
public class Main {

    public static void main(String[] args) {
        ButceHesabi hesap = new ButceHesabi("Cengiz Kilic", "251205027", 25000.0, 5000.0);
        ButceService servis = new ButceService(hesap, 100);

        ornekVerileriYukle(servis);

        Scanner giris = new Scanner(System.in);
        boolean calisiyor = true;

        while (calisiyor) {
            menuYazdir();
            String secim = giris.nextLine().trim();

            if (secim.equals("1")) {
                servis.tumIslemleriListele();
            } else if (secim.equals("2")) {
                servis.butceOzeti();
            } else if (secim.equals("3")) {
                servis.tipAnalizi();
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
     * liste bos gorunmuyor. Ekleme ekrani geldiginde bu metot kalkacak,
     * yerine kullanicinin kendi girdigi kayitlar gelecek.
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

    private static void menuYazdir() {
        System.out.println("");
        System.out.println("=======================================================");
        System.out.println("     KISISEL GELIR GIDER VE BUTCE TAKIP SISTEMI");
        System.out.println("=======================================================");
        System.out.println("1) Tum islemleri listele");
        System.out.println("2) Butce ozeti");
        System.out.println("3) Islem turu analizi");
        System.out.println("0) Cikis");
        System.out.print("Seciminiz: ");
    }
}
