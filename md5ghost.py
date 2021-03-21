
try :

	import requests
	import sys
	import hashlib
	import platform

except Exception as e :

	print(f"Error : {e}")
	exit()

if platform.system().startswith("Linux") :
	red , green , yellow , blue , endc = '\033[91m' , '\033[92m' ,'\033[93m' , '\033[94m' , '\033[0m'
else :
	red = green = yellow = blue = endc = ""

if len(sys.argv) < 2:
	print(red + "! Usage : " + endc + "python3 MD5Cracker.py <your hash>")
	exit()

hashstr = sys.argv[1]

url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt"
check_url = lambda : True if requests.get(url).status_code == 200 else False

def hashconverter(h) :
	return hashlib.md5(h.strip().encode("utf-8")).hexdigest()

def crack() :

	try :
		if check_url() :
			temp = requests.get(url).text.split("\n")
			for word in temp :
				if hashconverter(word) == hashstr :
					print(green + "[+] Hash Found     : " + endc + word)
					break
				else :
					print(red + "[!] Hash Not Found : " + endc + word)
		else :
			print(red + "! Error : " + endc + f"Cannot Reach {url}")
	except KeyboardInterrupt :
		sys.exit()
	except Exception as e :
		print(red + "Error : " + endc + str(e))

if __name__ == "__main__" :
	crack()
