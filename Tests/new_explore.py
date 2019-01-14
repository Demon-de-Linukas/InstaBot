from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions as exceptionsln
from src import utility as ut


import time
import random
import string
import selenium

tagdic = ut.tagdic
dictionary = ut.dictionary
path = 'D:\Workspace/loginData.csv'
keyword = 'linukas'
username,passw = ut.getUserData(path,keyword)
process = True
while True:
    print('Starting...')
    print('Waiting for login')
    browser = ut.login(username=username, password=passw, headless=False)
    print('Succed!')
    start = time.time()
    while process:
        adres = 'https://www.instagram.com/explore/tags/' + random.choice(tagdic)
        browser.get(adres)
        time.sleep(5)
        warning = 0
        liked = 0
        n=0
        for n in range(10):
            for i in range(99):
                try:
                   posts = browser.find_elements_by_css_selector("[class ^= 'v1Nh3 kIKUG']")
                   number = len(posts) - int(5 * random.random())
                   if len(posts) <= i:
                       break
                   post = posts[i]
                   ActionChains(browser).double_click(post).perform()
                   time.sleep(2)
                   if 10*random.random()+1 < 6 and warning <= 20:
                       word = random.choice(dictionary)
                       ut.textcomment_explore(browser, word)
                       warning = warning + 1
                   else:
                       warning = warning + 2
                   if ut.likepost(browser):
                       liked +=1
                   if browser.current_url != adres:
                       browser.back()
                   if warning > 36:
                       warning = 0
                except (exceptionsln.TimeoutException, selenium.common.exceptions.StaleElementReferenceException,
                    selenium.common.exceptions.InvalidElementStateException,
                    selenium.common.exceptions.NoSuchElementException) as e:
                   print(e)
                if liked >= 50:
                    n=1000
                    break
                    print('Refreshing....')
            ut.execute_times(browser, 1)

        else:
            ut.execute_times(browser, 1)
            end = time.time()
            if (end - start) / 60 / 60 > 1.5:
                browser.close()
                process = False
                print('Close browser now.')
                break
    else:
        print('Sleeping......')
        time.sleep(3500)
        print('Get up!!!!! Go on!')
        process = True



