import requests
import colorama
from colorama import Fore
import ctypes
import os
import art 
from art import *




tokens = open("tokens.txt", encoding="UTF-8").read().splitlines()


print("[1] Get Token Info")
print("[2] Check All Tokens")
options = int(input("Option > "))



if options == 1:

    onetoken = input("Token >")
    
    
    
    headers1 = {
    'authorization': onetoken
    }

    req1 = requests.get('https://discord.com/api/v9/users/@me', headers=headers1 )
    username1 = req1.json() ["username"]
    verified1 = req1.json() ["verified"]
    phone1 = req1.json() ["phone"]
    email1 = req1.json() ["email"]
    flags1 = req1.json() ["flags"]
    if req1.status_code == 200:
        print("Username:",username1)
        print("Verified:", verified1)
        print("Phone:", phone1)
        print("Email", email1)
        print("Flags:", flags1)
    else:
        print("[-] Locked")
elif options == 2:
    for i in tokens:
        token = i
        headers2 = {
        'authorization': i
        }

        req69 = requests.get('https://discord.com/api/v9/users/@me/affinities/guilds', headers=headers2)
        
        if req69.status_code == 200:
                print( Fore.MAGENTA ,f"[+] Valid > {token[20:]}******")
                with open("valid-tokens.txt", "a", encoding="utf-8") as file:
                    file.write(f"{token}\n")
        elif req69.status_code == 403:
                print(Fore.BLUE,f"[-] Locked > {token[20:]}******")
               
        elif req69.status_code == 429:
            print("[!] Ratelimited")
        else:
            print("[!] Error")

   

    
  
 



            
        
    

    
