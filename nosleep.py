import datetime
import random
import time
import subprocess
from pynput.keyboard import Key, Controller as KeyboardController
import sys
import logging

#Creating and Configuring Logger
Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "nosleep.log",
                    filemode = "w",
                    format = Log_Format,
                    level = logging.DEBUG)

logger = logging.getLogger()
logger.info("Started")

def main():
    keyboard = KeyboardController()
    slack = r'/Applications/Slack.app'
    subprocess.call(['open', slack])

    done = False
    while not done:
        time.sleep(random.randint(1, 189))
        currenttime = datetime.datetime.now().strftime("%H%M%S")
        if (currenttime) >= "170000":
            done = True
            logger.info("Ended")
        else:
            keyboard.tap(Key.ctrl)
            print(f'{datetime.datetime.now()}', end='\r\r')
            logger.info(f'{datetime.datetime.now()}')
    main()