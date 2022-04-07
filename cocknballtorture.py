# saturn cheat loader was proudly coded by autumn (https://github.com/autumnlikescode).
# Copyright (c) 2021 autumn#{myhashtag} | https://www.google.com/
# saturn cheat loader under the GNU General Public Liscense v2 (1991).


import fade
import os
import os.path
import platform
import hashlib
import sys


from colorama import Fore
from updtcheck import update, THIS_VERSION, setTitle
from time import sleep
from keyauth.keyauth import api
from progress.bar import ChargingBar, Bar
from common import *
from os import system
from datetime import datetime

# Set Title
os.system('title Saturn')

# Set Window Size
system('mode con: cols=100 lines=30')

###### Texts ######
tktext = colored(95, 0, 255, 'Input')
locate = colored(95, 0, 255, 'Locating')
found = colored(95, 0, 255, 'Found Files')
dldrv = colored(95, 0, 255, 'Downloading Drivers')
fndrv = colored(95, 0, 255, 'Found Drivers')
loaddrv = colored(95, 0, 255, 'Loading Drivers')

###################

def gmoddl():
    print(f'{Fore.RESET}| {dldrv}{Fore.RESET}| G-MOD ')



################################################### Login ###################################################



main()
print('═══════════════════════════════════════════════════════════════════════════════════════════════════')
key = input(f'{Fore.RESET}| {tktext}{Fore.RESET}| License: ')
keyauthapp.license(key)

    # Call Update
update()
sleep(0.5)
os.system('title Saturn')
# Print Main Screen
mainsel()
###### Program Start ######
selector = input(f'{Fore.RESET}| {tktext}{Fore.RESET}| Choice: ')

if selector == '1':
    clear()
    gmodsel()
    input()
    # print(f'{Fore.RESET}| {locate}{Fore.RESET}| G-MOD ')
   #  sleep(1)
   #  print(f'{Fore.RESET}| {found}{Fore.RESET}| G-MOD ')
   #  sleep(0.5)
   #  print(f'{Fore.RESET}| {dldrv}{Fore.RESET}| G-MOD ')
    
    sleep(0.5)



















input()