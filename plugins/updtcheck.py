import os
from time import sleep
import sys
import ctypes


THIS_VERSION = 'B01'

def update():
    print('')
    os.system('title Checking For Updates.')
    sleep(0.5)
    os.system('title Checking For Updates..')
    sleep(0.5)
    os.system('title Checking For Updates...')
    sleep(0.5)



def setTitle(_str):
    system = os.name
    if system == 'nt':
        #if its windows
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | made by autumn#4173")
    elif system == 'posix':
        #if its linux
        sys.stdout.write(f"\x1b]0;{_str} | Made By Rdimo#6969\x07")
    else:
        #if its something else or some err happend for some reason, we do nothing
        pass


