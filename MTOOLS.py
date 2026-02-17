import os 
import time 
import json 
import requests 
import webbrowser
import yt_dlp
import ctypes
import sys
import subprocess

idk = 0
3

ydl_opts = {
    "outtmpl": r"C:\Users\soanp\Documents\MTOOLS\Output\%(title)s.%(ext)s"
}


logo = """


\033[0;34m▄▄▄      ▄▄▄ ▄▄▄▄▄▄▄▄▄\033[0m   ▄▄▄▄▄     ▄▄▄▄▄  \033[0;31m ▄▄▄       ▄▄▄▄▄▄▄ 
\033[0;34m████▄  ▄████ ▀▀▀███▀▀▀\033[0m ▄███████▄ ▄███████▄\033[0;31m ███      █████▀▀▀ 
\033[0;34m███▀████▀███    ███   \033[0m ███   ███ ███   ███\033[0;31m ███       ▀████▄  
\033[0;34m███  ▀▀  ███    ███   \033[0m ███▄▄▄███ ███▄▄▄███\033[0;31m ███         ▀████ 
\033[0;34m███      ███    ███   \033[0m  ▀█████▀   ▀█████▀ \033[0;31m ████████ ███████▀ 
\033[0m\033\033[7mNEW MULTITOOL BY LOWMOON\033[0m                            
                                                             

"""
menu = """
 _____________________________________________________
|\033[0;31m[1]\033[0m \033[0;32mIP Lookup\033[0m                 | \033[0;31m[X] Close\033[0m            |
|\033[0;31m[2]\033[0m \033[0;32mYoutube video downloader\033[0m  |                      |
|\033[0;31m[3]\033[0m \033[0;32mRun a local Ai(ollama)\033[0m    |                      |
|\033[0;31m[4]\033[0m \033[0;32mFREE ROBUX\033[0m                |                      |
|\033[0;31m[5]\033[0m \033[0;32m\033[0m                          |                      |
|\033[0;31m[6]\033[0m \033[0;32m\033[0m                          |                      |
|\033[0;31m[7]\033[0m \033[0;32m\033[0m                          |                      |
|\033[0;31m[8]\033[0m \033[0;32m\033[0m                          |                      |
|______________________________|______________________|
"""

while True:
    os.system('cls')
    print(logo)
    print(menu)
    x = input("Choose an option : ")
    if x == "1":
        ip = input('Enter IP: ')
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        os.system("cls")
        print("\033[0;34mRESULTS\n")
        print(f"\033[0;31mCountry: \033[0;32m{data["country"]}")
        print(f"\033[0;31mCity: \033[0;32m{data["city"]}")
        print(f"\033[0;31mRegion: \033[0;32m{data["regionName"]}")
        print(f"\033[0;31mTimeZone: \033[0;32m{data["timezone"]}")
        print(f"\033[0;31mLatitude: \033[0;32m{data["lat"]}")
        print(f"\033[0;31mLongitude: \033[0;32m{data["lon"]}")
        pause = input(f'\033[0mPress enter to return...')
        print('Closing...')
        time.sleep(1)
    elif x == "2":
        link = input("Enter video url : ")
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as yt:
             yt.download([link])
        except Exception as e:
            print(f"\033[0;31mWrong URL !\n CLOSING")
            time.sleep(1.5)
    elif x == "3":
        os.system("cls")
        os.system("ollama run llama2-uncensored")
    elif x == "4":
        os.system("cls")
        os.system("color a")
        questione = input("\033[0;31mWarning: Using this option will force you to close and re-open this file.\n Do you still want opening it?\033[0m(y/n?) : ")
        if questione.lower() == "y":
            os.system("cls")
            os.system("curl ascii.live/rick")
        else:
            time.sleep(0.5)
            print("Closing...")
            time.sleep(1.5)
    elif x == "x" or x == "X":
        os.system("cls")
        print("Why :(")
    else:
        print(f"\033[0;31mWrong Input")
        time.sleep(0.5)
        print("Closing...")
        time.sleep(1.5)

        