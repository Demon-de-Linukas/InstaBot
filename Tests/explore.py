#!/usr/bin/python3
import sys
import random
import time
from selenium.common import exceptions as exceptionsln


sys.path.append('/home/pi/Instagram/')

from src import utility as ut
from src import modeUtil as mut


tagdic = ut.tagdic
dictionary = ut.dictionary
keydict=ut.keydict
path = '/home/pi/loginData.csv'

testing = []


while True:
    for keyword in keydict:
        try:
            print(keyword)
            username, passw = ut.getUserData(path, keyword)
            logger = ut.initlog(username)
            ut.init_comment_cache(username)
            mut.explore(username, passw, logger,linux=True,headless=True)
        except (TimeoutError,RuntimeError,TypeError) as e:
            logger.error('-->%s'%e)
    time.sleep(2*60*60)