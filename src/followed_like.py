from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions as exceptionsln
from selenium.common.exceptions import StaleElementReferenceException
from src import utility as ut


import time
import random
import selenium



###############################################################################################################
dictionary = ut.dictionary

dictionary=ut.dictionary
path = 'loginData.csv'
keyword = 'linukas'
username,passw = ut.getUserData(path,keyword)
print('Wait for login...')
browser = ut.login(username, passw,False)
print('Succed!!')
ut.fffk_notify(browser)
warning = 0
time.sleep(5)
for n in range(1,150):
    i = 0
    print('Page '+str(n))
    time.sleep(2)
    articles = browser.find_elements_by_css_selector("[class ^='_8Rm4L M9sTE']")
    time.sleep(2)
    if len(articles) != 0:
        for i in range(len(articles)):
            time.sleep(1)
            try:
                article = articles[i]
                browser.execute_script("arguments[0].scrollIntoView();", article)
                ########Like the Posts###################
                zan = article.find_element_by_css_selector("[class ^= 'glyphsSpriteHeart']")
                if 'outline' in (zan.get_attribute('class')):
                    # if bo.find_elements_by_css_selector("[class='glyphsSpriteHeart__outline__24__grey_9 Szr5J']"):
                    ActionChains(browser).double_click(zan).perform()
                    print('Like it!!')
                    time.sleep(1)
                else:
                    print('Already liked!')
        ######## Comment the Posts###############
                if 10*random.random() < 6 and warning <= 5:
                    word = random.choice(dictionary)
                    #textcomment(browser, word, article)
                    warning = warning + 1
                else:
                    warning = warning + 2
            except (exceptionsln.TimeoutException, selenium.common.exceptions.StaleElementReferenceException,
                    selenium.common.exceptions.InvalidElementStateException,
                    selenium.common.exceptions.NoSuchElementException) as ee:
                print (ee)
            if warning > 26:
                warning = 0
        time.sleep(2)
    else:
        time.sleep(2)
    ut.execute_times(browser,0)

