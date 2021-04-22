#!usr/bin/env python3
#-*-coding:utf-8-*-

import os

os.system("apt install figlet")
os.system("clear")
os.system("figlet NETWORK")

print("""

Network Programına Hoş Geldiniz.

1)Network True False Ayarı
2)Local IP Sabitleme
3)Sabit IP'yi Dinamik IP'ye Çevirme
4)Çıkış
""")

soru = input("Seçim: ")

if soru=="1":
    dosya = open("/etc/NetworkManager/NetworkManager.conf","w")
    dosya.write("[main]\nplugins=ifupdown,keyfile\n\n[ifupdown]\nmanaged=true")
    print("Kali Network True Talse Ayarı Yapıldı")

elif soru=="2":
    sor = input("Ağ Kartınızı Girin: ")
    sor1 = input("Local IP Adresinizi Girin: ")
    sor2 = input("Netmask Bilgisini Giriniz: ")
    sor3 = input("Broadcast Bilgisini Giriniz: ")
    sor4 = input("Geteway (modem IP) Bilgisini Giriniz: ")
    dosya = open("/etc/network/interfaces","w")
    dosya.write("# This file describes the network interfaces available on your system\n# and how to activate them. For more information, see interfaces(5).\n\nsource /etc/network/interfaces.d/*\n\n# The loopback network interface\nauto lo\niface lo inet loopback\n\niface " + sor + "inet static \n        address " + sor1 + "\n        netmask " + sor2 + "\n        boardcast " + sor3 + "\n        geteway " + sor4)
    print("IP Adresiniz Sabitlendi Bundan Sonra Local IP adresiniz " + sor1 + " Olacaktır")

elif soru=="3":
    soru2 = input("IP Adresinizi Giriniz: ")
    dosya = open("/etc/network/interfaces","w")
    dosya.write("# This file describes the network interfaces available on your system\n# and how to activate them. For more information, see interfaces(5).\n\nsource /etc/network/interfaces.d/*\n\n# The loopback network interface\nauto lo\niface lo inet loopback")
    print("Local IP Adresiniz Şuan Değişkendir IP Adresiniz " + soru2 + " Olacaktır")
elif soru=="4":
	print("Güle Güle")

else:
	print("Yanlış Seçim Yaptınız \nProgram Kapatıldı")
