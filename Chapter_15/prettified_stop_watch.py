#!python3.6

# prettified_stop_watch.py - A simple stopwatch program with pretty output.

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                     # press Enter to begin
print('Started.')
start_time = time.time()    # get the first lap's start time
last_time = start_time
lap_num = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print('Lap #' + str(lap_num).rjust(3) + ':' + str(total_time).rjust(7) + ' (' + str(lap_time).rjust(6) + ')')
        lap_num += 1
        last_time = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')