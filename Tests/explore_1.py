#!/usr/bin/python3
import sys
import random
import selenium.common.exceptions as seleEx


sys.path.append('/home/pi/Instagram/')

from src import utility as ut
from src import modeUtil as mut


tagdic = ut.tagdic
dictionary = ut.dictionary
keydict=ut.keydict
path = 'D:\Workspace/loginData.csv'
testing = []



while True:
    try:
        keyword = random.choice(keydict)
        print(keyword)
        username, passw = ut.getUserData(path, keyword)
        logger = ut.initlog(username)
        mut.explore(username, passw, logger,linux=False,headless=False)
    except (TimeoutError,RuntimeError,seleEx,TypeError) as e:
        logger.error('-->%s'%e)
