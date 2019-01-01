
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions as exceptionsln
from src import utility as ut


import time
import random
import selenium

path = 'D:\Workspace/loginData.csv'
keyword = 'jjk'
dictionary=ut.dictionary
username, passw = ut.getUserData(path,keyword)

process = True
while True:
    print('Starting...')
    print('Waiting for login')
    browser = ut.login(username=username, password=passw,headless=False)
    print('Succed!')
    start = time.time()
    while process:
        browser.get('https://www.instagram.com/explore/')
        time.sleep(5)
        warning = 0
        for i in range(10):
            print('Page: '+str(i))
            articles = browser.find_elements_by_css_selector("[class ^='Nnq7C weEfm']")
            for column in articles:
               try :
                   posts = column.find_elements_by_css_selector("[class ^= 'v1Nh3 kIKUG  _bz0w']")
                   for i in range(len(posts)):
                       post = posts[i]
                       ActionChains(browser).double_click(post).perform()
                       time.sleep(2)
                       if 10*random.random()+1 < 6 and warning <= 10:
                           check = 10*random.random()
                           if check <3:
                                word = random.choice(dictionary) + ' @linukas_z'
                           elif 3<check<6:
                                word = random.choice(dictionary)
                           else:
                               word = '@linukas_z'
                           ut.textcomment_explore(browser, word)
                           warning = warning + 1
                       else:
                           warning = warning + 2
                       ut.likepost(browser)
                       if browser.current_url != 'https://www.instagram.com/explore/':
                           browser.back()
                       #closse = browser.find_element_by_xpath('/html/body/div[3]/div/button')
                       #ActionChains(browser).double_click(closse).perform()
                       if warning > 26:
                           warning = 0
               except (exceptionsln.TimeoutException, selenium.common.exceptions.StaleElementReferenceException,
                    selenium.common.exceptions.InvalidElementStateException,
                    selenium.common.exceptions.NoSuchElementException) as e:
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



