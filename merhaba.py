# merhaba.py - Kişiye özel karşılama mesajı yazan ve yaş hesaplayan program

# datetime modülünden "date" aracını alıyoruz; bugünün tarihini bize o söyleyecek
from datetime import date

# Programın ne yaptığını kullanıcıya kısaca anlatan bir başlık yazdırıyoruz
print("=== GEP1316 Karşılama Programı ===")

# input() ile kullanıcının ismini soruyoruz ve cevabı "isim" değişkeninde saklıyoruz
isim = input("İsminizi yazın: ")

# Doğum yılını soruyoruz; gelen cevap metin olduğu için int() ile sayıya çeviriyoruz
dogum = int(input("Hangi yıl doğdunuz? "))

# Bilgisayarın takviminden şu anki yılı öğreniyoruz
simdiki_yil = date.today().year

# BENİM DEĞİŞİKLİĞİM: Doğum yılı şu anki yıldan büyükse yaş hesaplanmaz, uyarı verilir
if dogum > simdiki_yil:
    # Gelecekteki bir yıl doğum yılı olamayacağı için kullanıcıyı uyarıyoruz
    print("Bu yıl henüz gelmedi, lütfen doğum yılını kontrol et.")
else:
    # Şu anki yıldan doğum yılını çıkarıp kişinin bu yıl kaç yaşına gireceğini buluyoruz
    yas = simdiki_yil - dogum

    # f-string ile isim ve yaşı cümlenin içine yerleştirip karşılama mesajını yazdırıyoruz
    print(f"Hoş geldin {isim}! {simdiki_yil} yılında {yas} yaşına giriyorsun.")

# Programın bittiğini belirten kısa bir kapanış mesajı yazdırıyoruz
print("Kodlama Okuryazarlığı dersinde başarılar!")
