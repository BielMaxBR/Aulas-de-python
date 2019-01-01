import datetime
import time
import sys

time_start = time.time()
seconds = datetime.datetime.now().second
minutes = datetime.datetime.now().minute

while True:
    try:
        sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
        sys.stdout.flush()
        time.sleep(1)
        seconds = int(datetime.datetime.now().second)
        minutes = int(datetime.datetime.now().minute)
        #if seconds >= 60:
            #minutes += 1
            #seconds = 0
    except KeyboardInterrupt as B:
        break