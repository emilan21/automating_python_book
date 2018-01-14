#!/usr/bin/python3.5

# countdown.py - A simple countdown script.

import time
import subprocess

time_left = 60
while time_left > 0:
    print(time_left)
    time.sleep(1)
    time_left = time_left - 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['see', 'alarm.wav'])