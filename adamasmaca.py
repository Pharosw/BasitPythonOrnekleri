import pyfiglet
import random
kelimeler = ["Balık", "köpek", "kablumbağa", "yunus", "balina", "fok", "arı", "atmaca", "güvercin", "aslan", "baykuş", "papağan", "Geyik","Tavşan","Kuş" ]
secilen_kelime = random.choice(kelimeler)
gecerliHarfler = "abcçdefgğhıijklmnoöpqrsştuüvwxyz"
toplamHak = 10
yapilanTahmin = ""
Gri= '\033[30m'
Kirmizi = '\033[1;31m'
Yesil ='\033[1;32m'
Sari ='\033[1;33m'
Mavi ='\033[1;34m'
Beyaz ='\033[1;37m'
text = pyfiglet.figlet_format("ADAM ASMACA")
print(text+Beyaz)
Adam_Asmaca = [
    """
      --------
      |    |
      |
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |    |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |   /
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |   / \
      |
    """
]
print(Yesil+Adam_Asmaca)
print("Adam Asmaca Oyununa Hoş Geldin")
 
while toplamHak > 0:
    gercekKelime = ""
    for harf in secilen_kelime:
        if harf in yapilanTahmin:
            gercekKelime += harf
        else:
            gercekKelime += "_ "
    
    if gercekKelime == secilen_kelime:
        print(gercekKelime)
        print("Tebrikler kazandın")
        break
    
    print(Adam_Asmaca[5 - toplamHak])
    print("Hayvan adını tahmin edin:", gercekKelime)
    print(f"Kalan hakkınız: {toplamHak}")
  
else:
    print("kaybettiniz doğru kelime:", secilen_kelime)
