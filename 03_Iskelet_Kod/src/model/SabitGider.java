package model;

/**
 * Her ay tekrarlayan gider. Gider sinifindan tureiyor.
 * Boylece kalitim hiyerarsisi uc seviye oluyor: Islem, Gider, SabitGider.
 * Ek olarak odeme gununu tutuyor, ornek kira her ayin 5. gunu.
 */
public class SabitGider extends Gider {

    private int odemeGunu;   // 1 ile 31 arasi

    public SabitGider(String aciklama, double tutar, String tarih, Kategori kategori,
                      String odemeYontemi, int odemeGunu) {
        super(aciklama, tutar, tarih, kategori, odemeYontemi, true);   // sabit giderler zorunludur
        setOdemeGunu(odemeGunu);
    }

    public int getOdemeGunu() {
        return odemeGunu;
    }

    // Ayin gunu 1 ile 31 arasinda olmali.
    public void setOdemeGunu(int odemeGunu) {
        if (odemeGunu < 1 || odemeGunu > 31) {
            System.out.println("Uyari: odeme gunu 1 ile 31 arasinda olmali, eski deger korundu.");
            return;
        }
        this.odemeGunu = odemeGunu;
    }

    // Ust siniftaki etiketi degistiriyor, ekranda "Sabit Gider" yazacak.
    @Override
    public String tip() {
        return "Sabit Gider";
    }

    @Override
    public String toString() {
        return super.toString() + " | Her ayin " + odemeGunu + ". gunu";
    }
}
