import colorama
import os
import time
from colorama import init, Fore


def ipping():
    os.system("cls")
    count = 1
    e = input("Enter IP Address:   ")
    replies = 0
    replies += 1
    hostname = e
    os.system("cls")
    print("-"*100)
    print("="*100)
    print("-"*100)
    print(f'''  
            .d8888b.  888       d8b 888                  888               
            d88P  Y88b 888      Y8P 888               888               
            Y88b.      888          888               888               
             "Y888b.   88888b.  888 888  888  .d88b.  888  888 888  888 
                "Y88b. 888 "88b 888 888 .88P d88""88b 888 .88P 888  888 
                  "888 888  888 888 888888K  888  888 888888K  888  888 
            Y88b  d88P 888  888 888 888 "88b Y88..88P 888 "88b Y88b 888 
             "Y8888P"  888  888 888 888  888  "Y88P"  888  888  "Y88888 
            Jud owns you                          
        ''')
      
    while True:
        response = os.system("ping -n 1 " + hostname + " [insert angled bracket here because youtube description won't let me]nul")
        if response == 0:
            print("\033[1;32;40m" + hostname + " is online!" + " [" +  str(count) + "]" +  '\033[0m')
        else:
            print("\033[31m" + hostname + " is offline!" " [" +  str(count) + "]" +  '\033[0m')
        count += 1
        time.sleep(2)

ipping()
