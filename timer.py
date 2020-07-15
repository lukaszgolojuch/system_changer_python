import time
import sys
import os


def change_counter(min_nr):
    minuty = min_nr - 1
    sekundy = 59

    time_start = time.time()
    seconds = 0
    minutes = 0

    while True:
        try:
           # sys.stdout.write("\rCzas oczekiwania: {minutes} Minut {seconds} Sekund".format(minutes=minuty - minutes, seconds= sekundy - seconds))
            sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minuty - minutes, seconds= sekundy - seconds))
            sys.stdout.flush()
            time.sleep(1)
            seconds = int(time.time() - time_start) - minutes * 60
            if seconds >= 60:
                minutes += 1
                seconds = 0
            if minuty - minutes == 0 and sekundy - seconds == 0:
                #os.system('cls')  # For Windows
                #os.system('clear')  # For Linux/OS X
                break
        except:
            break
