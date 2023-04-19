#!/usr/bin/env python3
# Created By ybenel

import argparse, os, sys, requests
from hashlib import *
from colorama import *
from datetime import *
__program__ = 'skid'
__version__ = 'v1'
__author__ = 'Ph.Sk1d'
__github__ = 'https://github.com/Knownasjohnn'
class bcolors:
	##############################3
	Green="\033[1;33m"
	Blue="\033[1;34m"
	Grey="\033[1;30m"
	Reset="\033[0m"
	yellow="\033[1;36m"
	Red="\033[1;31m"
	purple="\033[35m"
	Light="\033[95m"
	cyan="\033[96m"
	stong="\033[39m"
	unknown="\033[38;5;82m"
	unknown2="\033[38;5;198m"
	unknown3="\033[38;5;208m"
	unknown4="\033[38;5;167m"
	unknown5="\033[38;5;91m"
	unknown6="\033[38;5;210m"
	unknown7="\033[38;5;165m"
	unknown8="\033[38;5;49m"
	unknown9="\033[38;5;160m"
	unknown10="\033[38;5;51m"
	unknown11="\033[38;5;13m"
	##############################3

print("""
HashDecrypt

a simple hash decryptor

Author: Skid-Dev

Usage:
	
python3 HashDecrypt.py -i input (To generate hash md5, sha1,sha224,sha256, sha384, sha512)

python3 HashDecrypt.py -v value -f wordlist.txt /(to bruteforce md5, sha1, sha224,sha256,sha384,sha512)

python3 HashDecrypt.py -h hash / (for online search md5, sha1, sha224, sha256,sha384,sha512)

""")

def genpass():
	key = 0
	start = datetime.now()
	parser = argparse.ArgumentParser(bcolors.unknown7,
       formatter_class=argparse.RawTextHelpFormatter,
       epilog=bcolors.unknown8 + '''\
use examples:
  {0} -k Key
  {0} -v HASH -f Wordlist
  {0} -n HASH'''.format(__program__ + '.py'))
	parser.add_argument("--hash","-v",help = "Enter Hash Value")
	parser.add_argument("--file","-f",help = "Enter wordlist")
	parser.add_argument("--key","-k",help = "Input Key")
	parser.add_argument("--net","-n",help = "Enter Hash Value")

	x = parser.parse_args()

	if x.key:
		print(bcolors.Red +'Hash Generated For :\033[0m',bcolors.purple+x.key,)
		h = md5(x.key.encode()).hexdigest()
		h1 = sha1(x.key.encode()).hexdigest()
		h2 = sha224(x.key.encode()).hexdigest()
		h3 = sha256(x.key.encode()).hexdigest()
		h4 = sha384(x.key.encode()).hexdigest()
		h5 = sha512(x.key.encode()).hexdigest()
		print (bcolors.unknown10 +'\nmd5    : \033[0m',bcolors.unknown11+h,
				bcolors.unknown10 +'\nsha1   : \033[0m',bcolors.unknown11+h1,
				bcolors.unknown10 +'\nsha224 : \033[0m',bcolors.unknown11+h2,
				bcolors.unknown10 +'\nsha256 : \033[0m',bcolors.unknown11+h3,
				bcolors.unknown10 +'\nsha384 : \033[0m',bcolors.unknown11+h4,
				bcolors.unknown10 +'\nsha512 : \033[0m',bcolors.unknown11+h5,'\n')
		return False
	if x.net:
		if len(x.net) == 32:
			on = requests.get('http://www.nitrxgen.net/md5db/' + x.net).text
			if len (on) == 0:
				print(bcolors.Blue+'Md5 Value Not Found  For -->	: ',Fore.RED,x.net)
			else :
				print(bcolors.purple+'MD5 Value Found  For -->  :',bcolors.unknown3 ,x.net,'\n',bcolors.unknown7,'		 Key -->  :',bcolors.unknown8 ,on)
		else:
			onn = requests.get('https://lea.kz/api/hash/' + x.net).status_code

			if onn == 200:
				onn = requests.get('https://lea.kz/api/hash/' + x.net).text
				print(bcolors.purple+'Value Found  For -->  :',bcolors.unknown6 ,x.net,'\n',Fore.WHITE,'           Key -->  :',bcolors.unknown8,onn)
			else :
				print(bcolors.Blue+'Value Not Found !!! For -->  :',bcolors.Red,x.net)
		return False
	if x.hash:
		if len (x.hash) == 32:
			value = md5
		elif len (x.hash) == 40:
			value = sha1
		elif len (x.hash) == 56:
			value = sha224
		elif len (x.hash) == 64:
			value = sha256
		elif len (x.hash) == 96:
			value = sha384
		elif len (x.hash) == 128:
			value = sha512
		else:
			print(Style.BRIGHT+'\nCheck The Hash !!! :)\n')
			sys.exit()
		with open(x.file,mode='r',encoding='ISO-8859-1') as data:
			for hash in data:
				hash=hash.strip()
				key +=1
				end = datetime.now()
				if value(hash.encode()).hexdigest()==x.hash:
					print(bcolors.purple,'\nValue Found  For -->        :',bcolors.unknown11 ,x.hash,'\n',bcolors.unknown8,'	     Key -->        :',Fore.RED,hash,Fore.WHITE,'\nTested',Fore.RED,key,Fore.WHITE,'word in',Fore.RED,x.file,Fore.WHITE,'elapsed time',Fore.CYAN,end - start,'\n')
					sys.exit()
				else:
					els = x
		x = print(bcolors.Blue+'\nValue Not Found  For -->       :',bcolors.unknown11 ,x.hash,Fore.WHITE,'\nTested',Fore.RED,key,Fore.WHITE,'word in',Fore.RED,x.file,Fore.WHITE,'elapsed time',Fore.GREEN,end - start,'\n')
		sys.exit()

if __name__ == "__main__":
	try:
		genpass()
	except UnicodeDecodeError:
		sys.exit()
	except KeyboardInterrupt:
		os.system("clear")
		sys.exit()
	except requests.exceptions.ConnectionError:
		print('Connection Error !!!')
	except FileNotFoundError:
		print(bcolors.Blue+'Wordlist Not Found !!! "Sorry ):" ')
