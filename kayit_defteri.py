# kayit_defteri.py - Sosyoloji saha araştırması görüşme kayıt defteri
# Görüşmeler sözlüklerden oluşan bir listede tutulur. Katılımcı adı yerine anonim kod kullanılır.

from datetime import date

def gorusme_ekle(gorusmeler, kod, tarih, mahalle, sure):
    """Yeni görüşmeyi listeye ekler. Eklenirse True, kod zaten varsa False döndürür."""
    # Kodları büyük harfe çeviriyoruz; böylece "g01" ile "G01" aynı kabul edilir
    kod = kod.upper()
    # Listedeki her görüşmenin kodunu yeni kodla karşılaştırıyoruz
    for gorusme in gorusmeler:
        # Aynı kod bulunursa kayıt eklenmeden False döndürülür
        if gorusme["kod"] == kod:
            return False
    # Kod yeni ise görüşmeyi bir sözlük olarak listenin sonuna ekliyoruz
    gorusmeler.append({"kod": kod, "tarih": tarih, "mahalle": mahalle, "sure": sure})
    # Eklemenin başarılı olduğunu bildirmek için True döndürüyoruz
    return True


def gorusmeleri_yazdir(gorusmeler):
    """Görüşmeleri tablo hâlinde ekrana yazdırır; değer döndürmez."""
    # Gösterilecek kayıt yoksa bilgi verip fonksiyonu bitiriyoruz
    if not gorusmeler:
        print("Defterde gösterilecek görüşme yok.")
        return
    # Sütun başlıklarını dikey çizgilerle ayırarak yazdırıyoruz
    print(f"| {'Kod':<5} | {'Tarih':<10} | {'Mahalle':<15} | {'Süre (dk)':>9} |")
    # Başlık ile kayıtların arasına çizgi çekiyoruz
    print("|" + "-" * 7 + "|" + "-" * 12 + "|" + "-" * 17 + "|" + "-" * 11 + "|")
    # Her görüşmeyi aynı sütun genişlikleriyle bir satıra yazıyoruz
    for gorusme in gorusmeler:
        print(f"| {gorusme['kod']:<5} | {gorusme['tarih']:<10} | "
              f"{gorusme['mahalle']:<15} | {gorusme['sure']:>9} |")
    # Tablonun altına kaç kayıt gösterildiğini yazıyoruz
    print(f"Toplam {len(gorusmeler)} görüşme gösterildi.")


def tarihten_sonra_yapilanlar(gorusmeler, tarih):
    """Verilen tarihten SONRA yapılan görüşmeleri yeni bir liste olarak döndürür."""
    # Sonuçları biriktireceğimiz boş liste
    bulunanlar = []
    # Her görüşmenin tarihini verilen tarihle karşılaştırıyoruz
    for gorusme in gorusmeler:
        # "YYYY-AA-GG" biçimindeki metinler tarih sırasıyla aynı sırada karşılaştırılır
        if gorusme["tarih"] > tarih:
            bulunanlar.append(gorusme)
    # Bulunanları döndürüyoruz; koşula uyan yoksa boş liste döner
    return bulunanlar


def ozet_cikar(gorusmeler):
    """Görüşme sayısı, toplam ve ortalama süre ile en uzun görüşmeyi sözlük olarak döndürür."""
    # Toplam görüşme sayısını listenin uzunluğundan buluyoruz
    sayi = len(gorusmeler)
    # Hiç görüşme yoksa sıfıra bölmemek için boş değerlerle dönüyoruz
    if sayi == 0:
        return {"sayi": 0, "toplam_sure": 0, "ortalama_sure": 0, "en_uzun_kod": "-"}
    # Toplam süre ve en uzun görüşme için başlangıç değerlerini veriyoruz
    toplam_sure = 0
    en_uzun = gorusmeler[0]
    # Her görüşmenin süresini topluyor, en uzununu takip ediyoruz
    for gorusme in gorusmeler:
        toplam_sure += gorusme["sure"]
        if gorusme["sure"] > en_uzun["sure"]:
            en_uzun = gorusme
    # Sonuçları tek bir sözlükte döndürüyoruz
    return {
        "sayi": sayi,
        "toplam_sure": toplam_sure,
        "ortalama_sure": toplam_sure / sayi,
        "en_uzun_kod": en_uzun["kod"],
    }


def tarih_gecerli_mi(metin):
    """Metin YYYY-AA-GG biçiminde gerçek bir tarihse True, değilse False döndürür."""
    try:
        # date.fromisoformat geçersiz tarihlerde (ör. 2026-02-30) hata verir
        date.fromisoformat(metin)
        return True
    except ValueError:
        return False


def menu():
    """Kullanıcı Ç (çıkış) seçene kadar menüyü tekrar gösterir."""
    # Bütün görüşmelerin tutulacağı liste
    gorusmeler = []
    # Kullanıcı çıkış seçene kadar döngü devam eder
    calisiyor = True
    while calisiyor:
        print("\n--- SAHA GÖRÜŞME DEFTERİ ---")
        print("[E] Görüşme ekle   [L] Listele   [F] Tarihe göre filtrele")
        print("[O] Özet           [Ç] Çıkış")
        # Küçük/büyük harf farkı olmasın diye cevabı büyük harfe çeviriyoruz
        secim = input("Seçim: ").strip().upper()

        if secim == "E":
            kod = input("Görüşme kodu (ör. G01): ").strip()
            tarih = input("Tarih (YYYY-AA-GG): ").strip()
            mahalle = input("Mahalle: ").strip()
            sure_metni = input("Süre (dakika): ").strip()
            # Bilgileri tek tek kontrol ediyoruz; hatalıysa kayıt eklenmeden menüye dönülür
            if kod == "" or mahalle == "":
                print("  Uyarı: Kod ve mahalle boş bırakılamaz.")
            elif not tarih_gecerli_mi(tarih):
                print("  Uyarı: Tarih YYYY-AA-GG biçiminde ve gerçek bir tarih olmalı.")
            elif not sure_metni.isdigit() or not 1 <= int(sure_metni) <= 600:
                print("  Uyarı: Süre 1 ile 600 arasında tam sayı olmalı.")
            elif gorusme_ekle(gorusmeler, kod, tarih, mahalle, int(sure_metni)):
                print(f"  {kod.upper()} eklendi. Defterde {len(gorusmeler)} görüşme var.")
            else:
                print(f"  Uyarı: {kod.upper()} kodu zaten kullanılmış.")
        elif secim == "L":
            gorusmeleri_yazdir(gorusmeler)
        elif secim == "F":
            tarih = input("Hangi tarihten sonra? (YYYY-AA-GG): ").strip()
            if tarih_gecerli_mi(tarih):
                gorusmeleri_yazdir(tarihten_sonra_yapilanlar(gorusmeler, tarih))
            else:
                print("  Uyarı: Geçerli bir tarih girin.")
        elif secim == "O":
            ozet = ozet_cikar(gorusmeler)
            print(f"  Görüşme sayısı : {ozet['sayi']}")
            print(f"  Toplam süre    : {ozet['toplam_sure']} dk")
            print(f"  Ortalama süre  : {ozet['ortalama_sure']:.1f} dk")
            print(f"  En uzun        : {ozet['en_uzun_kod']}")
        elif secim in ("Ç", "ÇIKIŞ"):
            # Döngünün koşulunu False yaparak menüden çıkıyoruz
            calisiyor = False
            print("Defter kapatıldı.")
        else:
            print("  Uyarı: Menüde olmayan bir seçim yaptınız (E, L, F, O veya Ç).")


# Dosya doğrudan çalıştırıldığında menüyü başlatıyoruz
if __name__ == "__main__":
    menu()
