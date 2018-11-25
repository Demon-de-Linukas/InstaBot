from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys #引入keys类操作
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions as exceptionsln
from selenium.common.exceptions import StaleElementReferenceException
from SeleniumTest.src import cypter as cp

import time
import selenium
import csv
import random


dictionary = ['Wow!!', 'Nice post!', 'Great post!', 'Really nice!','Interesting!',
              'Great!!', 'coool!','Like it!', 'Yooo', 'Marvelous Post!', 'Keep going',
              'Great work!', 'Best piece', 'I like it!','great photo!', 'Sehr gut!', 'Schön!',
              'Ich mag es!','Yeah~~~', 'Woah~~', 'Perfect!', 'Gorgeous!', 'Excellent!', 'bravo.',
              'brilliant~', 'Impressive!', 'nice going!','good ', 'good picture!', 'good photo!', 'nice picture!', '~~~~', 'great shot!', 'Nice shot!'
              , 'good one!', 'Nice one!', 'Impressive shot!', 'Brilliant one!', 'best shot!']

def addoptions():
    addoptions = webdriver.ChromeOptions()
    addoptions.add_argument('headless')
    addoptions.add_argument('window-size=1200x600')
    return addoptions

def getpostersname(arti):
    title = arti.find_element_by_css_selector("[class ^= 'FPmhX notranslate nJAzx']")
    return title.get_attribute('title')


def execute_times(driver, times):
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    print('scrolllllllll')
    #driver.execute_script("window.scrollTo(0, -(document.body.scrollHeight));")
    time.sleep(5)


def login(username, password,headless):
    options = addoptions()
    if headless:
        browser = webdriver.Chrome(chrome_options=options)
    else:
        browser = webdriver.Chrome()
    browser.get("https://www.instagram.com/accounts/login/")
    usernameBox = browser.find_element_by_name('username')
    passwordBox = browser.find_element_by_name('password')
    usernameBox.send_keys(username)
    passwordBox.send_keys(password)
    browser.find_element_by_css_selector("[type ^= 'submit']").click()
    time.sleep(5)
    return browser


def textcomment_followed(driver, commentstr, arti):
    try:
        comment = arti.find_element_by_css_selector("[class ^= 'glyphsSpriteComment']")
        name = getpostersname(arti)
        #commentstr = commentstr + ' ' + name
        ActionChains(driver).double_click(comment).perform()
        text = arti.find_element_by_css_selector("[class ^= 'Ypffh']")
        #text = driver.find_element_by_tag_name('textarea')
        text.send_keys(commentstr)
        text.send_keys(Keys.ENTER)
        print('Comment left: '+commentstr)
    except (selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.InvalidElementStateException) as ee:
        print(ee)
        

def textcomment_explore(driver, commentstr):

    try:
        comment = driver.find_element_by_css_selector("[class ^= 'glyphsSpriteComment']")
        zan = driver.find_element_by_css_selector("[class ^= 'glyphsSpriteHeart']")
        if 'outline' in (zan.get_attribute('class')):
            name = getpostersname(driver)
            if len(name) < 8:
                commentstr = commentstr + ' @' + name
            ActionChains(driver).double_click(comment).perform()
            text = driver.find_element_by_css_selector("[class ^= 'Ypffh']")
           # text = driver.find_element_by_tag_name('textarea')
            text.send_keys(commentstr)
            time.sleep(2)
            text.send_keys(Keys.ENTER)
            print('Comment left: '+commentstr)
    except selenium.common.exceptions.NoSuchElementException as ee:
        print(ee)


def close_post(driver):
    cll = driver.find_element_by_css_selector("[class ^= 'ckWGn']")
    ActionChains(driver).double_click(cll).perform()


def likepost(driver):
    try:
        zan = driver.find_element_by_css_selector("[class ^= 'glyphsSpriteHeart']")
        if 'outline' in (zan.get_attribute('class')):
            ActionChains(driver).double_click(zan).perform()
            time.sleep(1)
            print('Post liked')
            return False
        else:
            print('Already Liked')
            return True
    except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.StaleElementReferenceException) as ee:
        print(ee)


def fffk_notify(browser):
    browser.find_element_by_css_selector("[class^='aOOlW   HoLwm']").click()

################################################
def get_following_list(browser):
    for link in browser.find_elements_by_xpath("//*[@href]"):
        print(link.get_attribute('href'))
        if link.get_attribute('href') == 'https://www.instagram.com/linukas_z/following/':
            link.click()
            print(link.get_attribute('href'))


def generate_list(size):
    result_list = []
    for i in range(size):
        result_list.append(i)
    return result_list


def getUserData(fpath,key):
    with open(fpath, 'rt', encoding='utf-8') as myFile:
        reader = csv.DictReader(myFile)
        for row in reader:
            if row['key'] == key:
                return deCode(row['username']), deCode(row['password'])


def newUserData(fpath, username=None, password=None,key=None):
    if username==None and password==None:
        key = input('Key name:\n')
        username = input('Username:\n')
        password = input('Pass word:\n')
    cusername = enCode(username)
    cpassword = enCode(password)
    with open(fpath, "a+") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([key,cusername,cpassword])

def enCode(code):
    return cp.enCode(code)


def deCode(code):
    return cp.deCode(code)