#!/usr/bin/python3
import sys
import random
import selenium.common.exceptions as seleEx
sys.path.append('/home/pi/Instagram/')
import threading


from src import utility as ut
from src import modeUtil as mut


tagdic = ut.tagdic
dictionary = ut.dictionary
keydict=ut.keydict
path = 'D:\Workspace/loginData.csv'
testing = []


class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q


    def run(self):
        print("Starting " + self.name)
        # threadLock.acquire()
        process()
        # threadLock.release()

        print("Exiting " + self.name)


def process():
    global testing
    try:
        while True:
            keyword = random.choice(keydict)
            if keyword in testing:
                continue
            testing.append(keyword)
            username, passw = ut.getUserData(path, keyword)
            logger = ut.initlog(username)
            mut.explore(username=username, passw=passw, logger=logger,linux=False,headless=False)
    except (TimeoutError,RuntimeError,seleEx.NoSuchElementException) as e:
        logger.error('-->%s'%e)

# threadLock = threading.Lock()
while True:
    threads = []
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)
    thread3 = myThread(3, "Thread-3", 3)
    thread1.start()
    thread2.start()
    thread3.start()
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)
    for t in threads:
        t.join()
    print("Exiting Main Thread")