import datetime
import random
import time
import subprocess
from pynput.keyboard import Key, Controller as KeyboardController


keyboard = KeyboardController()
slack = r'/Applications/Slack.app'
subprocess.call(['open', slack])

done = False
while not done:
    time.sleep(random.randint(1, 60))
    currenttime = datetime.datetime.now().strftime("%H%M%S")
    if (currenttime) >= "170000":
        done = True
    else:
        keyboard.tap(Key.ctrl)
        print(f'{datetime.datetime.now()}', end='\r\r')
