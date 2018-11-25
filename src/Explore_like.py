from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions as exceptionsln
from SeleniumTest.src import utility as ut

import time
import random
import string
import selenium



dictionary=ut.dictionary
path = 'loginData.csv'
keyword = 'linukas'
username,passw = ut.getUserData(path,keyword)
tagdic = ['sightseeing', 'travel', 'travelgram','moutain','river','sunset','sunrise','forest','naturephotography','nature','architecture',
          'buildings','photography','photograph','photoshop']
process = True
like_time=0
while True:
    print('Starting...')
    print('Waiting for login')
    browser = ut.login(username, passw,False)
    print('Succed!')
    start = time.time()
    while process:
        #browser.get('https://www.instagram.com/explore/')
        adress = 'https://www.instagram.com/explore/tags/' + random.choice(tagdic)
        print(adress)
        browser.get(adress)
        print('Explore page...')
        time.sleep(5)
        warning = 0
        i = 0
        for n in range(20):
            while i < 999:
                try:
                    posts = browser.find_elements_by_css_selector("[class ^= 'v1Nh3 kIKUG']")
                    number = len(posts) - int(5*random.random())
                    if i >= len(posts) :
                        ut.execute_times(browser,1)
                        posts = browser.find_elements_by_css_selector("[class ^= 'v1Nh3 kIKUG']")
                        i = 0
                    post = posts[i]
                    ActionChains(browser).double_click(post).perform()
                    time.sleep(2)
                    status = False
                    if 10*random.random() < 5 and warning <= 10:
                        word = random.choice(dictionary)
                        ut.textcomment_explore(browser, word)
                        warning = warning + 1
                    else:
                        warning = warning + 2
                    if 10*random.random() < 7:
                        status = ut.likepost(browser)
                        like_time +=1
                    if browser.current_url !=adress:
                        browser.back()
                    if status:
                        i=i+9
                    if warning > 26:
                        warning = 0
                except selenium.common.exceptions.StaleElementReferenceException as e:
                    print(e)
                time.sleep(10)
                i += 1
            ut.execute_times(browser,1)
            n += 1
        end = time.time()
        if (end - start)/60/60 > 2 or like_time > 800:
            browser.close()
            process = False
            print('Close browser now.')
    print('Sleeping......')
    time.sleep(7200)
    print('Get up!!!!! Go on!')
    process = True
    if like_time > 800:
        print('Finished!!')
        break
