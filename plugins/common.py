import fade
import os
from time import sleep
import sys
import ctypes
import os.path
import platform
import hashlib
import requests
import random

from keyauth.keyauth import api

def mainsel():
    clear()
    mainseltxt = '''
               *         ███████╗ █████╗ ████████╗██╗   ██╗██████╗ ███╗   ██╗     *       
    *   *        |       ██╔════╝██╔══██╗╚══██╔══╝██║   ██║██╔══██╗████╗  ██║       |      *
           *   - o -     ███████╗███████║   ██║   ██║   ██║██████╔╝██╔██╗ ██║     - o -
       *         |       ╚════██║██╔══██║   ██║   ██║   ██║██╔══██╗██║╚██╗██║ *     |
                         ███████║██║  ██║   ██║   ╚██████╔╝██║  ██║██║ ╚████║       *
      *        *         ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  *        * 
═══════════════════════════════════════════════════════════════════════════════════════════════════     
                        [01] G-MOD      | [04] Apex     | [07] GTA
                        [02] CS:GO      | [05] MC       | [08] Discord
                        [03] Fortnite   | [06] FiveM    | [00] _      
                            
═══════════════════════════════════════════════════════════════════════════════════════════════════      
'''
    faded_mainseltxt = fade.purpleblue(mainseltxt)
    print(faded_mainseltxt)



def gmodsel():
    clear()
    mainseltxt = '''
               *         ███████╗ █████╗ ████████╗██╗   ██╗██████╗ ███╗   ██╗     *       
    *   *        |       ██╔════╝██╔══██╗╚══██╔══╝██║   ██║██╔══██╗████╗  ██║       |      *
           *   - o -     ███████╗███████║   ██║   ██║   ██║██████╔╝██╔██╗ ██║     - o -
       *         |       ╚════██║██╔══██║   ██║   ██║   ██║██╔══██╗██║╚██╗██║ *     |
                         ███████║██║  ██║   ██║   ╚██████╔╝██║  ██║██║ ╚████║       *
      *        *         ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  *        * 
═══════════════════════════════════════════════════════════════════════════════════════════════════     
                                [01] Cheat    |    [02] Lua Stealer    
                            
═══════════════════════════════════════════════════════════════════════════════════════════════════      
'''
    faded_mainseltxt = fade.purpleblue(mainseltxt)
    print(faded_mainseltxt)



def main():
    clear()
    maintxt = '''
               *         ███████╗ █████╗ ████████╗██╗   ██╗██████╗ ███╗   ██╗     *       
    *   *        |       ██╔════╝██╔══██╗╚══██╔══╝██║   ██║██╔══██╗████╗  ██║       |      *
           *   - o -     ███████╗███████║   ██║   ██║   ██║██████╔╝██╔██╗ ██║     - o -
       *         |       ╚════██║██╔══██║   ██║   ██║   ██║██╔══██╗██║╚██╗██║ *     |
                         ███████║██║  ██║   ██║   ╚██████╔╝██║  ██║██║ ╚████║       *
      *        *         ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  *        *     
'''
    faded_maintxt = fade.purpleblue(maintxt)
    print(faded_maintxt)


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def getchecksum():
	path = os.path.basename(__file__)
	if not os.path.exists(path):
		path = path[:-2] + "exe"
	md5_hash = hashlib.md5()
	a_file = open(path,"rb")
	content = a_file.read()
	md5_hash.update(content)
	digest = md5_hash.hexdigest()
	return digest

keyauthapp = api(
	name = "autumn",
	ownerid = "vvgz0mGIka",
	secret = "48baf2c686749977d5ee9fb37e0e70c398c3e64107b65a37d686b09e468ea99d",
	version = "1.0",
	hash_to_check = getchecksum()
)

def clear():
    os.system('cls')



titleurl = 'https://pastebin.com/raw/CBuLUe6P'
r = requests.get(titleurl)
content = r.text.splitlines()
userprint =random.choice(content)



def setTitleUrl():
    os.system(f'title {userprint}')











