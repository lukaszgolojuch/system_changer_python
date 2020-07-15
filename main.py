import mac_changer
import open_program
import shutoff
import sys
import os
import ping

class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

def main():
    os.system('cls')  # For Windows        
    os.system('clear')  # For Linux/OS X

    print("Welcome!")
    print("Menu")
    print("1 - change MAC adress")
    print("2 - open program on time")
    print("3 - shut off computer on time")
    print("4 - PING test")
    print("5 - exit")
    argument = input("Your choice: ")

    os.system('cls')  # For Windows        
    os.system('clear')  # For Linux/OS X

    while switch(argument):
        if case(1):
            mac_changer.change_mac()
            break
        if case(2):
            open_program.open()
            break
        if case(3):
            shutoff.shut()
            break
        if case(4):
            ping.check_ping()
            break
        if case(5):
            exit()

        print "Wrong input."
        break
    
    main()

if __name__ == "__main__": 
    main()




