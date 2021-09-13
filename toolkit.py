#!/usr/bin/python3
import os
import sys

os.system("clear")

print ('''
 _____           _ _   ___ _   
|_   _|         | | | / (_) |  
  | | ___   ___ | | |/ / _| |_ 
  | |/ _ \ / _ \| |    \| | __|
  | | (_) | (_) | | |\  \ | |_ 
  \_/\___/ \___/|_\_| \_/_|\__|
                               
                               ''')
print ("")
print ("Developed By King-Nazim And MishalMMSS")
print ("")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")
os.system ("cd")
os.system ("apt upgrade -y")
os.system ("apt install python -y")
os.system ("apt install python2 -y")
os.system ("apt install php -y")
os.system ("apt install python-dev -y")
os.system ("apt install python3 -y")
os.system ("apt install java -y")
os.system ("apt install git -y")
os.system ("apt install perl -y")
os.system ("apt install bash")
os.system ("apt install nano -y")
os.system ("apt install curl -y")
os.system ("apt install openssl -y")
os.system ("apt install openssh -y")
os.system ("apt install wget -y")
os.system ("apt install clang -y")
os.system ("apt install nmap -y")
os.system ("apt install w3m -y")
os.system ("apt install hydra -y")
os.system ("apt install ruby -y")
os.system ("apt install macchanger -y")
os.system ("apt install host -y")
os.system ("apt install dnsutils -y")
os.system ("apt install coreutils -y")
os.system ("apt install fish -y")
os.system ("apt install zip -y")
os.system ("apt install hydra -y")
os.system ("apt install figlet -y")
os.system ("apt install cowsay -y")
os.system ("apt install unzip -y")
os.system ("apt install vim -y")
os.system ("apt install ruby -y")
os.system ("apt install wcalc -y")
os.system ("apt install bmon -y")
os.system ("apt install unrar -y")
os.system ("apt install proot -y")
os.system ("apt install golang -y")
print ("Allow the Button For Access the Storage in Termux")
os.system ("termux-setup-storage")
  
os.system ("bash .install.sh")
