import os
import subprocess
import getpass 
import sys
import time
import main

def check_ping():
    url = raw_input("What site you would like to check: ")
    response = os.system("ping -c 1 " + url)

    if response == 0:
        print("\nNetwork Active")
    else:
        print("\nNetwork Error")

    print("\nWhat now?")
    print("1 - Home")
    print("2 - Check other site")

    answ = input("Your choice: ")

    if answ == 1 :
        main.main()
    elif answ == 2:
        check_ping()
