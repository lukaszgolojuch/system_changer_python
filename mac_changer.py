import os
import random
import subprocess
import getpass 
import sys
import timer
import random
import time
import main

#zmienianie adresu mac karty sieciowej 
def change_mac():
    print("Menu Change MAC adress")
    print("1 - random change time")
    print("2 - change adress frequently")
    print("3 - back")
    argument = input("Your choice: ")

    if argument == 1 : 
        interval = int(input("Maximum interval: "))
        random_bool = 1
    elif argument == 2:
        interval = int(input("Interval: "))
        random_bool = 0
    elif argument == 3:
        main.main()
    else :
        print("\nIncorrect input \n")
        print("Wait...")
        time.sleep(3)
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        change_mac()

    sudoPassword = getpass.getpass("System password: ")

    while 1:
        
        if random_bool == 1:
            interval = random.randrange(interval)
    
        #os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X

        zdanie = "Twoj aktualny Mac adres to: " + actual_mac()
        print(zdanie)

        timer.change_counter(interval)

        new_mac = generate_mac()
        command = 'sudo ifconfig en0 ether '+new_mac
        os.popen("sudo -S %s"%(command), 'w').write(sudoPassword)


def random_min():

    return time

def actual_mac():
    command="ifconfig | grep ether | head -1"
    result = subprocess.check_output(command, shell=True)
    result = result[7:]

    return result

def generate_mac():
    old_mac = actual_mac()
    old_mac = old_mac[:15]

    losowa = random.randrange(17)
    liczba1 = hex(losowa)
    l1 = str(liczba1)[2:]

    losowa = random.randrange(17)
    losowa =random.randrange(losowa)
    liczba2 = hex(losowa)
    l2 = str(liczba2)[2:]
    new_mac = old_mac + l1 + l2
    
    return new_mac
    

