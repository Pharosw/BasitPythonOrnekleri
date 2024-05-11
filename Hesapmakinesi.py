import pyfiglet
import os 
import time
Gri= '\033[30m'
Kirmizi = '\033[1;31m'
Yesil ='\033[1;32m'
Sari ='\033[1;33m'
Mavi ='\033[1;34m'
Beyaz ='\033[1;37m'
banner = pyfiglet.figlet_format("Calcutor")
print(Kirmizi+banner)
print(""" 
###################################
#                                 #
#  HESAP MAKİNESİNE HOŞGELDİNİZ!  #                                  
#                                 #
#                                 #
###################################
"""+Mavi) 
islemler = """
1. Toplama işlemi yapar
2. Çıkarma işlemi yapar
3. Çarpma işlemi yapar
4. Bölme işlemi yapar
5. Kuvvet alma
6. Karekok bulma
99. Çıkış işlemini yapar 
""" +Beyaz
print(islemler)
while True:
  secim = input("işlem seçiminizi giriniz:")
  if secim == "99":
    print("Görüşmek üzere !")
    time.sleep(1)
    os.system("clear")
    exit()
  
  elif secim == "1":
    sayi1 = int(input("1. sayıyı giriniz: "))
    sayi2 = int(input("2. sayıyı giriniz: "))
    print(sayi1, "+", sayi2, "=", sayi1+sayi2)
  
  elif secim == "2":
    sayi1 = int(input(" 1. sayıyı giriniz: "))
    sayi2 = int(input(" 2. sayıyı giriniz: "))
    print(sayi1, "-", sayi2, "=", sayi1-sayi2)
  
  elif secim == "3":
    sayi1 = int(input("1. sayıyı giriniz: "))
    sayi2 = int(input("2. sayıyı giriniz: "))
    print(sayi1, "*", sayi2, "=", sayi1*sayi2)
  elif secim == "4":
    sayi1 = int(input("1. sayıyı giriniz: "))
    sayi2 = int(input("2. sayıyı giriniz: "))
    print(sayi1, "/", sayi2, "=", sayi1/sayi2)
    	
  elif secim == "5":
    sayi1 = int(input("1. sayıyı giriniz: "))
    sayi2 = int(input("2. sayıyı giriniz: "))
    print(sayi1, "**", sayi2, "=", sayi1**sayi2)
  
  elif secim == "6":
    sayi = int(input("Sayıyı giriniz: "))
    print("Sayinin karekoku:", sayi ** 0.5 )
  
  else:
    print("Bir işlem girmelisin")
    input()
    
  
  




