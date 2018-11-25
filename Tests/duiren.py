
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions as exceptionsln
from SeleniumTest.src import utility as ut


import time
import random
import string
import selenium

subject = ['u','you','this','here is a bastard','u bastard']
describe = ['fucking', 'f**cking stuipid', 'suipidl','lying','cheap','no good','rotten','floor flushing','snake licking','dirt eating',
            'inbred','over-stuffed','ignorant','blood-sucking','ass kissing','brainless','dickless','heartless','bug-eyed','worm-deaded sack of monkey']
object = ['shit','son of bitch','slut','shit-glutton','buzzard','greedy moth','bastard','sucker','fucker','pig','greasy creature']

path = ''
keyword = ''
username,passw = ut.getUserData(path,keyword)
process = True
while True:
    print('Starting...')
    print('Waiting for login')
    browser = ut.login(username=username, password=passw, headless=False)
    print('Succed!')
    start = time.time()
    adres = 'https://www.instagram.com/realdonaldtrump'
    while process:
        browser.get(adres)
        time.sleep(5)
        warning = 0
        for i in range(10):
            ut.execute_times(browser, int(5*random.random()))
            print('Page: '+str(i))
            articles = browser.find_elements_by_css_selector("[class ^='Nnq7C weEfm']")
            for column in articles:
               try :
                   posts = column.find_elements_by_css_selector("[class ^= 'v1Nh3 kIKUG  _bz0w']")
                   for i in range(len(posts)):
                       post = posts[i]
                       ActionChains(browser).double_click(post).perform()
                       time.sleep(2)
                       word = random.choice(subject)+' '+random.choice(describe) + ' ' + random.choice(object)
                       ut.textcomment_explore(browser, word)
                       if browser.current_url != adres:
                           browser.back()
                       time.sleep(5)

               except selenium.common.exceptions.StaleElementReferenceException as e:
                   print(e)
            ut.execute_times(browser, 5)
            end = time.time()
            if (end - start) / 60 / 60 > 1.5:
                browser.close()
                break

        process = False
        print('Close browser now.')
    print('Sleeping......')
    time.sleep(7200)
    print('Get up!!!!! Go on!')
    process = True



