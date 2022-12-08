import os
import time
time.sleep(1)
import random 
try:
	import pyzipper
except:
	os.system("pip install pyzipper")
import pyzipper
import sys
W='\33[0m'
R='\33[1;31m'
G='\33[1;32m'
O='\33[1;33m'
B='\33[1;34m'
P='\33[1;35m'
C='\33[1;36m'
GR='\33[1;37m'
RR="\033[0;101m"
gg='\033[0;102m'
def a(s):
		for i in s:
			sys.stdout.write(i)
			sys.stdout.flush()
			time.sleep(0)
def w(s):
		for i in s:
			sys.stdout.write(i)
			sys.stdout.flush()
			time.sleep(0.02)
def xx(s):
		for i in s:
			sys.stdout.write(i)
			sys.stdout.flush()
			time.sleep(0.5)
na=1
try:
	print(f"""
{G} __I__ 
  |{RR}|{W}{G}|   
 {O}Z{G}|{O}I{W}{O}|P  {R}[*]{W} github: github.com/issamiso
  |{RR}|{W}{G}|   {R}[*]{W}{C} 5.12.26
   {B}V""")
	def p(s):
		for i in s:
			sys.stdout.write(i)
			sys.stdout.flush()
			time.sleep(0.04)
	p(f"{P}[-]{RR} {G}Hacking zip files{W} \n")
	print(O+"————————————————————————————————")
	print(f"""{G}[{W}1{G}]{W} automatic list password 4 ML
{G}[{W}2{G}]{W} add list password """) 
	try: 
		xll=input(G+f"[{W}*{G}]{W} Namber > ")
	except:
		print(R+"[!] ERROR")
	if xll =="1":
		try:
			name=input(f"{G}[-]{W} Name_File Zip > ")
			print(O+"————————————————————————————————")
			a(f"{G}[*]{W} STARTING ");w(R+".....");xx(R+"....\n")
		except:
			print(R+"[!] ERROR")
		with open(".passwordiso.txt","rb") as ll:
			for i in ll.readlines():
				pw=i.strip()
				try:
					with pyzipper.AESZipFile(name,"r") as pp:
						pp.extractall(pwd=pw)
						print(f"{B}--------------------------------\n{R}[*]{W} Zip_File:{G} {name}")
						print(R+"[*]\33[0m password:\33[1;32m {}\33[1;34m \n--------------------------------".format(pw.decode("utf-8")))
						break
				except:
					na+=1
					print("{}[{}{}{}]{} password Error{}: {}".format(R,G,na,R,R,W,pw.decode("utf-8")))
				#	print("Errro ",pw.decode("utf-8"))
	if xll=="2":
		try:
			name=input(f"{G}[-]{W} Name_File Zip > ")
			print(O+"————————————————————————————————")
			pas=input(f"{G}[-]{W} List_Password > ")
			print(O+"————————————————————————————————")
			a(f"{G}[*]{W} STARTING ");w(R+".....");xx(R+"....\n")
		except:
			print(R+"[!] ERROR")
		with open(pas,"rb") as ll:
			for i in ll.readlines():
				pw=i.strip()
				try:
					with pyzipper.AESZipFile(name,"r") as pp:
						pp.extractall(pwd=pw)
						print(f"{B}--------------------------------\n{R}[*]{W} Zip_File:{G} {name}")
						print(R+"[*]\33[0m password:\33[1;32m {}\33[1;34m \n--------------------------------".format(pw.decode("utf-8")))
						break
				except:
					na+=1
					print("{}[{}{}{}]{} password Error{}: {}".format(R,G,na,R,R,W,pw.decode("utf-8")))
				#	pri
except:
		print(R+"[!]ERRRO")	

	