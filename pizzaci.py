import os 
import pyfiglet
import time
hesap_ucreti = 0
Gri='\033[30m'
Kirmizi='\033[1;31m'
Yesil='\033[1;32m'
Sari='\033[1;33m'
Mavi='\033[1;34m'
Beyaz='\033[1;37m'
text = pyfiglet.figlet_format("PHAROS PIZZA")
print(text+Beyaz)
while True:
  print("Pizzaciya hoşgeldiniz toplam 2 seçenek vardır: \n 1. secenek pizza siparisi \n 2.secenek çıkış yapma")
  n = input("Seçiminizi yapınız:")
  
  if n == "1":
    kucuk = 30
    orta = 40
    buyuk = 50
    icecek = 12
    ekstra_peynir = 17
    boy = input("Boy secimini yapınız S,M,L:").upper()
    w = input("İçecek alırmıydınız Evet yada Hayır:").capitalize()
    z = input("Ekstra peynir istermisiniz Evet yada Hayır:").capitalize()
    
    if boy == "S":
      hesap_ucreti += kucuk
      
    elif boy == "M":
      hesap_ucreti += orta
      
    elif boy == "L":
      hesap_ucreti += buyuk
    
    elif w == "Evet":
      hesap_ucreti += icecek
    
    elif z == "Evet":
      hesap_ucreti += ekstra_peynir
    
    print("Toplam hesap ücretiniz:", hesap_ucreti)
  
  elif n == "2":
    dogrula = input("Eminmisiniz Evet yada Hayır:").capitalize()
    
    if dogrula == "Evet":
      print("Görüşmek üzere ")
      time.sleep(1)
      exit()
    elif dogrula == "Hayır":
      n = input("Secim giriniz:")
      
  
    
 