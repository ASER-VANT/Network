#!usr/bin/env python3
#-*-coding:utf-8-*-

import os

os.system("apt install figlet")
os.system("clear")
os.system("figlet MAKRO")

print("Lütfen Kali Linux Kullanıyorsanız Bu aracı Kullanın\nAksi Halde Soru Yapabilir")

print("""

Network Programına Hoş Geldiniz.

1)Network True False Ayarı
2)Local IP Sabitleme
3)Sabit IP'yi Dinamik IP'ye Çevirme
4)Kali Linux Wifi Ağ Görme Sorunu
5)Kali Linux Depo Güncelleme
6)Çıkış
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
    sorular = input("Wirelass kart mı kullanıyorsun [Y/n] ")
    if sorular=="Y" or sorular=="y":
        dosya = open("/etc/NetworkManager/NetworkManager.conf","w")
        dosya.write("[main]\nplugins=ifupdown,keyfile\n\n[ifupdown]\nmanaged=false\n\n[device]\nwifi.scan-rand-mac-address=no")
        os.system("systemctl restart NetworkManager.service")
        os.system("systemctl restart network_manager.service")
        os.system("systemctl restart wpa_supplicant.service")
        res = input("Kali Linuxu Yeniden Başlatmanız Gerekiyor Yeniden Başlasınmı [Y/n] ")
        if res=="Y" or res=="y":
            os.system("reboot")
        elif res=="N" or res=="n":
            print("O zaman kendin yeniden başlat yoksa birşey çalışmayacak")
        else:
            print("Yanlış Seçim Program Kapatılıyor")
    elif sorular=="N" or sorular=="n":
        print("Wirelass Kart Kullanıyorsan Bu Ayarı Yapabilirsin")
    else:
        print("Yanlış Seçim Program Kapatılıyor")

elif soru=="5":
    dosya = open("/etc/apt/soruces.list")
    dosya.write("deb http://http.kali.org/kali kali-rolling main contrib non-free\n\ndeb-src http://http.kali.org/kali kali-rolling main contrib non-free")
    print("\nKali Linux Depo Güncelleme Tamamlandı")

elif soru=="6":
	print("Güle Güle")

else:
	print("Yanlış Seçim Yaptınız \nProgram Kapatıldı")
