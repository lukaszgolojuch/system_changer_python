import os
import subprocess
import getpass 
import sys
import timer
import datetime
import main

def open():
    print("Menu Open Program")
    print("1 - open program after some time")
    print("2 - open program at time")
    print("3 - back")
    argument = input("Your choice: ")

    if argument == 1 : 
        time = int(input("How much time to wait: "))
        after_time(time)
    elif argument == 2:
        on_time()
    elif argument == 3:
        main.main()
    else :
        print("Incorrect input")
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        open()

def on_time():

    path = raw_input("Drop program HERE: ")

    hr = int(input("Hour: "))
    minut = int(input("Minute: "))

    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X
    print("Program will open at " + str(hr) + ":" + str(minut))

    while(1):
        now = datetime.datetime.now()
        if now.hour==hr and now.minute ==minut:
                a = 'open '+ path
                os.popen(a,'r',1)
                break
    print("What now?")
    print("1 - Home")
    print("2 - Next program")

    answ = input("Your choice: ")

    if answ == 1 :
        main.main()
    elif answ == 2:
        open()

        

def after_time(time):
    path = raw_input("Drop program HERE: ")

    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X

    print("Program will open after: \n")
 
    timer.change_counter(time)

    while(1):
        a = 'open '+ path

        os.popen(a,'r',1)

    print("Program is opening... ")

    print("What now?")
    print("1 - Home")
    print("2 - Next program")

    answ = input("Your choice: ")

    if answ == 1 :
        main.main()
    elif answ == 2:
        open()

