import string
from random import *
adres = input("Ne Icin Sifre Olusturacaksiniz = ")
kullaniciadi = input("Kullanici Adi Giriniz = ")
f = open("Sifreler.txt", "a")
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters) for x in range(randint(8, 16)))
f.write(" --- " + adres + " --- \n") 
f.write("Kullanici Adi = " + kullaniciadi + "\n")
f.write("Sifre = " + password + "\n\n")
f.close()
print("Sifre Olusturuldu")