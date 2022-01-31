#! python3
# stopwatch.py - A simple stopwatch program

import time

# Display the program's instructions
print('Press ENTER to begin. Afterward, press ENTER tto click the stopwatch')
input()
print('STarted')
start_time = time.time()
last_time = start_time
lap_number = 1

# Start tracking the lap times
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f'Lap {lap_number}: {total_time} {lap_time}', end='')
        lap_number += 1
        last_time = time.time()
except KeyboardInterrupt:
    # Handle the  Ctrl-C interruption to keep its error message from displaying
    print('\nDone')
