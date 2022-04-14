#!/usr/bin/env python
#-*- coding utf8 -*-

import sys
from platform import system
from urllib2 import *
import os

os.system("cls")
banner = """\033[97m            _       _                              
\033[97m           (_)     | |                             
\033[97m   ___  ___ _ _ __ | |_   _ __ ___  ___ ___  _ __  
\033[97m  / _ \/ __| | '_ \| __| | '__/ _ \/ __/ _ \| '_ \ 
\033[94m | (_) \__ \ | | | | |_  | | |  __/ (_| (_) | | | |
\033[94m  \___/|___/_|_| |_|\__| |_|  \___|\___\___/|_| |_|
                                 \033[97m v1.0  Author ~ \033[91msh0kz\033[97m"""
print(banner)

def menu():
	print("\n\033[91m [1] \033[97m Whois lokup ")
	print("\033[91m [2] \033[97m Geolocalizacion de una IP ")
	print("\033[91m [3] \033[97m Escaneo de puerto TCP ")
	print("\033[91m [4] \033[97m Busqueda inversa de IP ")
	print("\033[91m [5] \033[97m Busqueda de DNS ")
	print("\033[91m [6] \033[97m Mi ip publica ")
	print("\033[91m [7] \033[97m Salir ")


def adios():
	op = raw_input("\n\033[94mOsint@Recon:~# \033[97m[1] Continuar \033[97m[2] Salir => ")
	if op == "2":
		print("\nSaliendo...\n")
		exit()
	elif op == "1":
		os.system("cls")
		print(banner)
		menu()
		select()
	elif op == "exit":
		print("\nSaliendo...")
		exit()
	else:
		print("\n\033[91m[-]\033[97m No se encontro la orden!")
		adios()
		
def select():
	try:
		opcion = raw_input("\n\n\033[94mOsint@Recon:~# \033[97m Digita una opcion \033[91m=> \033[97m")
		if opcion == "1":
			ingresar = raw_input("\n\033[94m Osint@Recon:~#\033[97m Ingresa el url \033[91m=> \033[97m")
			url = 'http://api.hackertarget.com/whois/?q=' + ingresar
			whois = urlopen(url).read()
			print(whois)
			adios()
			
		elif opcion == "2":
			ingresar = raw_input("\n \033[97mIngresa el url: \033[91m=> \033[97m")
			url = 'https://api.hackertarget.com/geoip/?q=' + ingresar
			geoip = urlopen(url).read()
			print("\n\033[94m[+] \033[97mINFO: \033[97m{}".format(ingresar))
			print""
			print(geoip)
			adios()

		elif opcion == "3":
			ingresar = raw_input("\n \033[97mIngresa el url \033[91m=> \033[97m")
			url = 'https://api.hackertarget.com/nmap/?q=' + ingresar
			scan = urlopen(url).read()
			print("\n\033[94m[+] \033[97mSCAN: \033[39m{}".format(ingresar))
			print("\n\033[97m{}".format(scan))
			adios()

		elif opcion == "4":
			ingresar = raw_input("\n \033[97mIngresa el url \033[91m=> \033[97m")
			url = 'https://api.hackertarget.com/reverseiplookup/?q=' + ingresar
			scan = urlopen(url).read()
			print("\n\033[94m[+] \033[97mHOST: \033[39m{}".format(ingresar))
			print("\n\033[97m{}".format(scan))
			adios()

		elif opcion == "5":
			ingresar = raw_input("\n \033[97mIngresa el url \033[91m=> \033[97m")
			url = 'https://api.hackertarget.com/dnslookup/?q=' + ingresar
			scan = urlopen(url).read()
			print("\n\033[94m[+] \033[97mDNS: \033[39m{}".format(ingresar))
			print("\n\033[97m{}".format(scan))
			adios()

		elif opcion == "6":
			url = 'https://api.ipify.org/'
			ip = urlopen(url).read()
			print("IP Publica \n\n" + ip)
			adios()

		elif opcion =="7":
			print("\033[91m\nSaliendo...\033[97m")
			exit()

		elif opcion == "exit":
			print("\n\033[91mSaliendo...\033[97m")
			exit()

		else:
			print("\n\033[91m[-]\033[97m No se encontro la orden!")
			adios()

	except KeyboardInterrupt:
		print("\n\n\033[91m adios by CTRL + C ...\n")

menu()
select()
