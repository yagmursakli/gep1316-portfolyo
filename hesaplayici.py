# hesaplayici.py - Bir anket için gereken örneklem büyüklüğünü Cochran formülüyle hesaplar

# Beklenen oran: önceden bilinmediği için en güvenli değer olan 0.5 kullanılır (float)
BEKLENEN_ORAN = 0.5

# Araştırmanın adını alıyoruz; input() her zaman metin (str) döndürür
arastirma_adi = input("Araştırmanın adı: ")

# Evren büyüklüğünü (toplam kişi sayısı) alıp int() ile tam sayıya çeviriyoruz
evren = int(input("Evren büyüklüğü (kişi): "))

# Güven düzeyini (90, 95 veya 99) alıp int() ile tam sayıya çeviriyoruz
guven_duzeyi = int(input("Güven düzeyi (90/95/99): "))

# Hata payını yüzde olarak alıp float() ile ondalıklı sayıya çeviriyoruz (ör. 5 veya 2.5)
hata_payi_yuzde = float(input("Hata payı (%): "))

# Şu ana kadar toplanan anket yanıtı sayısını alıp int() ile tam sayıya çeviriyoruz
toplanan_yanit = int(input("Toplanan yanıt sayısı: "))

# Güven düzeyine karşılık gelen Z değerini seçiyoruz
if guven_duzeyi == 90:
    z_degeri = 1.645
elif guven_duzeyi == 99:
    z_degeri = 2.576
else:
    # 90 ya da 99 dışındaki her değerde en yaygın düzey olan %95 kullanılır
    z_degeri = 1.96

# Hata payını yüzdeden ondalığa çeviriyoruz (5 -> 0.05)
hata_payi = hata_payi_yuzde / 100

# 1. adım: Sonsuz evren için örneklem n0 = Z² × p × (1 − p) ÷ e²
n0 = (z_degeri ** 2) * BEKLENEN_ORAN * (1 - BEKLENEN_ORAN) / (hata_payi ** 2)

# 2. adım: Sonlu evren düzeltmesi n = n0 ÷ (1 + (n0 − 1) ÷ N)
duzeltilmis_n = n0 / (1 + (n0 - 1) / evren)

# Sonucu tam sayı kişi sayısına çeviriyoruz; yarım kişiye anket yapılamaz
gereken_kisi = round(duzeltilmis_n)

# Karşılaştırma operatörü (>=) ile toplanan yanıtların yeterli olup olmadığını buluyoruz (bool)
yeterli_mi = toplanan_yanit >= gereken_kisi

# Yeterli değilse kaç yanıt daha gerektiğini hesaplıyoruz
eksik_yanit = gereken_kisi - toplanan_yanit

# Sonuçları f-string ile biçimli olarak yazdırıyoruz
print(f"\n--- {arastirma_adi} için örneklem raporu ---")
print(f"Güven düzeyi / Z değeri : %{guven_duzeyi} / {z_degeri}")
print(f"Sonsuz evren için (n0)  : {n0:.2f}")
print(f"Düzeltilmiş örneklem    : {duzeltilmis_n:.2f}")
print(f"Gereken kişi sayısı     : {gereken_kisi}")
print(f"Toplanan yanıt          : {toplanan_yanit}")
print(f"Örneklem yeterli mi?    : {yeterli_mi}")

# Yanıtlar yeterli değilse kaç kişiye daha ulaşılması gerektiğini söylüyoruz
if not yeterli_mi:
    print(f"En az {eksik_yanit} yanıt daha toplanmalı.")
