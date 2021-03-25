#!usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt install figlet")
os.system("clear")
os.system("figlet MAKRO")

#!usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt install figlet")
os.system("clear")
os.system("figlet MAKRO")

kali = raw_input("Kali Linuxda ağ sorunu varmı[Y/n] ")

if(kali=="y"):
	dosya = open("/etc/NetworkManager/NetworkManager.conf","w")
	dosya.write("""[main]
plugins=ifupdown,keyfile

[ifupdown]
managed=true""")
	print("Network false/true ayarı yapılmıştır Güle Güle")
elif(kali=="n"):
	print("")