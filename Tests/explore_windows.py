#!/usr/bin/python3
import sys
import random
sys.path.append('/home/pi/Instagram/')

from src import utility as ut
from src import modeUtil as mut


tagdic = ut.tagdic
dictionary = ut.dictionary
keydict=ut.keydict
path = 'D:\Workspace/loginData.csv'

process = True
try:
    while True:
        keyword = random.choice(keydict)
        username, passw = ut.getUserData(path, keyword)
        logger = ut.initlog(username)
        mut.explore(username, passw, logger,False,False)
except (TimeoutError,RuntimeError) as e:
    logger.error('-->%s'%e)


