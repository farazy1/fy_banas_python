#multi threading
import sys
import math
import random
import threading
import time

def execute_thread(i):
    
    print("Thread {} sleeps at {}\n".format(i, time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())), "\n")
    rand_sleep_time = random.randint(1,5)
    time.sleep(rand_sleep_time)
    print("Thread {} stops sleeping at {}".format(i, time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())) , "\n")


for i in range(10):
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()
    print("Active Thread:", threading.active_count(),"\n")
    #print("Thread Objects:", threading.enumerate())