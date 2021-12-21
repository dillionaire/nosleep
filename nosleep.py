import datetime
import random
import time
import subprocess
from pynput.keyboard import Key, Controller as KeyboardController
import logging
import sys

#Creating and Configuring Logger
Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "nosleep.log",
                    filemode = "w",
                    format = Log_Format,
                    level = logging.DEBUG)

logger = logging.getLogger()


def main():
    logger.info("Started")
    keyboard = KeyboardController()
    slack = r'/Applications/Slack.app'
    subprocess.call(['open', slack])

    done = False
    while not done:
        time.sleep(random.randint(1, 189))
        currenttime = datetime.datetime.now().strftime("%H%M%S")
        if (currenttime) >= "170000":
            done = True
            print('done')
            sys.exit(0)
        else:
            keyboard.tap(Key.ctrl)
            print(f'{datetime.datetime.now()}', end='\r\r')
            logger.info(f'{datetime.datetime.now()}')
    logger.info("Ended")

if __name__ == "__main__":
    main()