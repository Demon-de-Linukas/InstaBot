import time
import selenium
import csv
import logging
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions as exceptionsln
from src import cypter as cp
from selenium.webdriver.chrome.options import Options




dictionary = ['Wow!!', 'Nice post!', 'Great post!', 'Really nice!','Interesting!',
              'Great!!', 'coool!','Like it!', 'Yooo', 'Marvelous Post!', 'Keep going',
              'Great work!', 'Best piece', 'I like it!','great photo!', 'Sehr gut!', 'Schön!',
              'Ich mag es!','Yeah~~~', 'Woah~~', 'Perfect!', 'Gorgeous!', 'Excellent!', 'bravo.',
              'brilliant~', 'Impressive!', 'nice going!','good ', 'good picture!', 'good photo!', 'nice picture!', '~~~~', 'great shot!', 'Nice shot!'
              , 'good one!', 'Nice one!', 'Impressive shot!', 'Brilliant one!', 'best shot!']

tagdic = ['sightseeing', 'travel', 'travelgram','moutain','river','sunset','sunrise','forest','naturephotography','nature','architecture',
          'buildings','photography','photograph','photoshop','arizona','sonyalpha',
          'canon','vacation','greece','bestplacestogo','reflection','blogger']

keydict = ['linukas','jjk','king','yin']


def initlog(userName):
    today = datetime.date.today()
    logadress='logs/%s/'%today
    try:
        os.mkdir(logadress)
    except (FileExistsError,FileNotFoundError) as e:
        print(e)
    # create logger with 'spam_application'
    logger = logging.getLogger('spam_application_'+userName)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('%sinstalog_%s.log'%(logadress,userName))
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


def getpostersname(arti):
    title = arti.find_element_by_css_selector("[class ^= 'FPmhX notranslate nJAzx']")
    return title.get_attribute('title')


def execute_times(driver, times):
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    print('scrolllllllll')
    time.sleep(5)


def login(username, password,headless,linux):
    options = Options()
    options.add_argument('window-size=1200x600')
    options.add_argument('--lang=zh-CN')
    options.add_argument('--dns-prefetch-disable')
    if headless:
        options.add_argument('headless')
    if linux:
        browser = webdriver.Chrome(chrome_options=options, executable_path='/usr/lib/chromium-browser/chromedriver')
    else:
        browser = webdriver.Chrome(chrome_options=options)
    browser.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
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
        ActionChains(driver).double_click(comment).perform()
        text = arti.find_element_by_css_selector("[class ^= 'Ypffh']")
        text.send_keys(commentstr)
        text.send_keys(Keys.ENTER)
        print('Comment left: '+commentstr)
    except (selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.InvalidElementStateException) as ee:
        print(ee)
        

def textcomment_explore(driver, commentstr, logger):
    try:
        comment = driver.find_element_by_css_selector("[class ^= 'glyphsSpriteComment']")
        zan = driver.find_element_by_css_selector("[class ^= 'glyphsSpriteHeart']")
        if 'outline' in (zan.get_attribute('class')):
            name = getpostersname(driver)
            if len(name) < 8:
                commentstr = commentstr + ' @' + name
            ActionChains(driver).double_click(comment).perform()
            text = driver.find_element_by_css_selector("[class ^= 'Ypffh']")
            text.send_keys(commentstr)
            time.sleep(2)
            text.send_keys(Keys.ENTER)
            logger.info('-->Comment left: '+commentstr)
    except selenium.common.exceptions.NoSuchElementException as ee:
        print(ee)


def close_post(driver):
    cll = driver.find_element_by_css_selector("[class ^= 'ckWGn']")
    ActionChains(driver).double_click(cll).perform()



def likepost(browser, logger):
    """Likes the browser opened image"""
    # check action availability
    like_xpath = "//article/div/section/span/button/span[@aria-label='赞']"
    unlike_xpath = "//section/span/button/span[@aria-label='取消赞']"
    try:
        like_elem = browser.find_elements_by_xpath(like_xpath)
        if len(like_elem) == 1:
                # sleep real quick right before clicking the element
                time.sleep(2)
                ActionChains(browser).double_click(like_elem[0]).perform()
                # check now we have unlike instead of like
                liked_elem = browser.find_elements_by_xpath(unlike_xpath)

                if len(liked_elem) == 1:
                    logger.info('--> Image Liked!')
                    # get the post-like delay time to sleep
                    time.sleep(2)
                    return True

                else:
                    # if like not seceded wait for 2 min
                    logger.info('--> Image was not able to get Liked! maybe blocked ?')
                    time.sleep(2)

        else:
            liked_elem = browser.find_elements_by_xpath(unlike_xpath)
            if len(liked_elem) == 1:
                logger.info('--> Image already liked!')
                return False

        logger.info('--> Invalid Like Element!')

        return False
    except (selenium.common.exceptions.NoSuchElementException,
             selenium.common.exceptions.StaleElementReferenceException) as ee:
        logger.error(ee)
        return False


def fffk_notify(browser):
    browser.find_element_by_css_selector("[class^='aOOlW   HoLwm']").click()


########################################################################################################################
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