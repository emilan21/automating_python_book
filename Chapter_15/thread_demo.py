#!/usr/bin/python3.5

import threading
import time

print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

thread_obj = threading.Thread(target=takeANap)
thread_obj.start()

print('End of program.')