pipimport colorama
import sys
import fade
import time
import platform
import os
import json
import hashlib
from time import sleep
from datetime import datetime
from optparse import Option
import requests, threading, os, random, time
import colorama 
import sys
import ctypes
import subprocess
from colorama import Fore, init
from capmonster_python import RecaptchaV2Task
import json

from pystyle import Add, Center, Anime, Colors, Colorate, Write, System


from colorama import Fore
import random
#########################################

THIS_VERSION = "2.5.1"

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
# r = Fore.RESET

google_target_ver = 0
edge_target_ver = 0

lunar = r'''

          _______  _______  _______  _______  _______           _                          ______  
|\     /|(  ____ \(  ____ )(  ____ \(  ___  )(  ____ \|\     /|( \      |\     /||\     /|(  ___ \ 
| )   ( || (    \/| (    )|| (    \/| (   ) || (    \/| )   ( || (      | )   ( || )   ( || (   ) )
| |   | || (__    | (____)|| (_____ | (___) || (__    | |   | || |      | (___) || |   | || (__/ / 
( (   ) )|  __)   |     __)(_____  )|  ___  ||  __)   | |   | || |      |  ___  || |   | ||  __ (  
 \ \_/ / | (      | (\ (         ) || (   ) || (      | |   | || |      | (   ) || |   | || (  \ \ 
  \   /  | (____/\| ) \ \__/\____) || )   ( || )      | (___) || (____/\| )   ( || (___) || )___) )
   \_/   (_______/|/   \__/\_______)|/     \||/       (_______)(_______/|/     \|(_______)|/ \___/ 
                                                                                                    


                               https://discord.gg/JwDJZdjMMN
'''
System.Clear()
Anime.Fade(Center.Center(lunar), Colors.purple_to_blue, Colorate.Vertical, interval=0.030, enter=True)

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX

def removeToken(user, token: str):
    with open(f'tokens.txt', "r") as f:
        Tokens = f.read().split("\n")
        for t in Tokens:
            if len(t) < 5 or t == token:
                Tokens.remove(t)
        open(f'tokens.txt', "w").write("\n".join(Tokens))


done = 0
retries = 0
bypass = 0

cmd = 'mode 120,35'
os.system(cmd)

ctypes.windll.kernel32.SetConsoleTitleW(".gg/JwDJZdjMMN | Boost Tool")

def start():
    removeDuplicates("tokens.txt")
    save_tokens()

def title():
    global done, retries, bypass
    while True:
        os.system(f'')

def removeToken(token: str):
    with open('tokens.txt', "r") as f:
        Tokens = f.read().split("\n")
        for t in Tokens:
            if len(t) < 5 or t == token:
                Tokens.remove(t)
        open("tokens.txt", "w").write("\n".join(Tokens))

def finger():
    r = requests.get('https://discordapp.com/api/v9/experiments')
    if r.status_code == 200:
        fingerprint = r.json()['fingerprint']
        return fingerprint
    else:
        print('sum went wrong')

def cookies():
    r = requests.get('https://discord.com')
    if r.status_code == 200:
        cookies = r.cookies.get_dict()
        few = cookies['__dcfduid']
        few2 = cookies['__sdcfduid']
        lmao  = f"__dcfduid={few}; __sdcfduid={few2}; locale=en-US"
        return lmao
    else:
        print('sum went wrong')

with open("tokens.txt", "r") as f: tokens = f.read().splitlines()
def save_tokens():
    with open("tokens.txt", "w") as f: f.write("")
    for token in tokens:
        with open("tokens.txt", "a") as f: f.write(token + "\n")
def removeDuplicates(file):
    lines_seen = set()
    with open(file, "r+") as f:
        d = f.readlines(); f.seek(0)
        for i in d:
            if i not in lines_seen: f.write(i); lines_seen.add(i)
        f.truncate()

def boost(line, invite):
    global done

    try:
        token = line.strip()

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me', 
            'sec-fetch-dest': 'empty', 
            'sec-fetch-mode': 'cors',
            'cookie': '__dcfduid=23a63d20476c11ec9811c1e6024b99d9; __sdcfduid=23a63d21476c11ec9811c1e6024b99d9e7175a1ac31a8c5e4152455c5056eff033528243e185c5a85202515edb6d57b0; locale=en-GB',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSJ9',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMS45Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTc3NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTM1NTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
            'te': 'trailers',
        }
        r = requests.get("https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)
        if r.status_code == 200:
            slots = r.json()
            if len(slots) != 0:
                guid = None
                joined = False
                headers["content-type"] = 'application/json'
                for i in range(15):
                    try:
                        join_server = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={
                        })
                        if "captcha_sitekey" in join_server.text:
                            createTask = requests.post("https://api.capmonster.cloud/createTask", json={
                                "clientKey": "32a0b539ebdb5e84e1d5194c99d96008",
                                "task": {
                                    "type": "HCaptchaTaskProxyless",
                                    "websiteURL": "https://discord.com/channels/@me",
                                    "websiteKey": join_server.json()['captcha_sitekey']
                                }
                            }).json()["taskId"]
                            print("Captcha created: {}".format(createTask))
                            getResults = {}
                            getResults["status"] = "processing"
                            while getResults["status"] == "processing":
                                getResults = requests.post("https://api.capmonster.cloud/getTaskResult", json={
                                    "clientKey": "32a0b539ebdb5e84e1d5194c99d96008",
                                    "taskId": createTask
                                }).json()

                                time.sleep(1)

                            solution = getResults["solution"]["gRecaptchaResponse"]

                            print(f"\n                               Captcha Solved")

                            join_server = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={
                                "captcha_key": solution
                            })

                        if join_server.status_code == 200:
                            join_outcome = True
                            guid = join_server.json()["guild"]["id"]
                            print(f"\n{b}{Fore.RESET}{m}[{w}  Joined Server:{Fore.RESET}{m}]\n    {token[:40]}{Fore.RESET}")
                            removeToken(token)
                            break
                        else: 
                            print(f"\n{Fore.RESET}{m}[{w}{lr}  Error Joining:{Fore.RESET}{m}]\n    {token[:40]}{Fore.RESET} ")
                            removeToken(token)
                            return
                    except Exception as e:
                        print(e)
                        pass
            for slot in slots:
                slotid = slot['id']
                payload = {"user_premium_guild_subscription_slot_ids": [slotid]}
                r2 = requests.put(f'https://discord.com/api/v9/guilds/{guid}/premium/subscriptions', headers=headers, json=payload)
                if r2.status_code == 201:
                    done += 1
                else:
                    print(r2.json())
        else:
            print(r.json())

    except Exception as e:
        retries += 1

tokensAmount = len(open('tokens.txt', encoding='utf-8').read().splitlines())
BoostsAmmount = tokensAmount * 2
    

def print_banner(BoostsAmmount: int):
    global threads
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    print('')
    print('')
    Write.Print("                                     \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                                  Legit Boost                                \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                                     tool                            \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f'                                    \n', Colors.purple_to_blue, interval=0.000)
    Write.Print(f"                                     https://discord.gg/JwDJZdjMMN\n\n\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"                                     Boosts Available:{BoostsAmmount}\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_blue, interval=0.000)
    print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
{m}[{w}1{Fore.RESET}{m}]{Fore.RESET} Server Boosts   {b}|{Fore.RESET}{m}[{w}2{Fore.RESET}{m}]{Fore.RESET}  Stock             {b}|{Fore.RESET}{m}[{w}3{Fore.RESET}{m}]{Fore.RESET}{lr} EXIT{Fore.RESET}   

''')
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.blue_to_purple, interval=0.000)



def menu():
    global done
    while True:
        option = input(f'{m}[{w}>{m}]{w} Select Option: ')
        if option == "1":
            inv = input(f'{m}[{w}>{m}]{w} Invite https://discord.gg/: ')
            amount = int(input(f"{m}[{w}>{m}]{w} Boosts: "))
            with open('tokens.txt', 'r') as f:
                for line in f.readlines():
                    try:
                        boost(line, inv)
                        removeToken(line)
                    except Exception as e:
                        print(e)
                        pass
                    if done >= amount:
                        # removeToken(line)
                        print(f"Boosted {inv} {amount}x")              
                        done = 0
                        break

            done = 0

        if option == "2":
            os.system("tokens.txt")

            
            tokensAmount = len(open('tokens.txt', encoding='utf-8').read().splitlines())
            BoostsAmmount = tokensAmount * 2
            
            print_banner(BoostsAmmount)


            
        if option == "3":
            os._exit(0)
        


    
print_banner(BoostsAmmount)
    

    
threading.Thread(target=title).start()
    
print()
start()
menu()
