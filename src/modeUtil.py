import sys
sys.path.append('/home/pi/Instagram/')
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions as exceptionsln
from src import utility as ut


import time
import random
import selenium


def explore(username,passw,logger,linux,headless):
    tagdic = ut.tagdic
    print('Starting...')
    logger.info('Starting...')
    print('Waiting for login')
    browser = ut.login(username=username, password=passw, headless=headless,linux=linux)
    print('Succed!')
    logger.info('Succed! Start Exploring')
    start = time.time()
    while True:
        adres = 'https://www.instagram.com/explore/tags/' + random.choice(tagdic)
        browser.get(adres)
        time.sleep(5)
        warning = 0
        liked = 0
        warning,liked = operate_post(browser, adres, warning, liked, logger)
        end = time.time()
        if (end - start) / 60 / 60 > 1.5:
            browser.close()
            logger.info('--> Close browser now.')
            break
        if liked >= 50:
            print('Refreshing....')
            continue
        ut.execute_times(browser, 1)

    logger.info('Sleeping......')
    time.sleep(3500)
    logger.info('Get up!!!!! Go on!')


def operate_post(browser, adres, commentwarn,liked,logger):
    dictionary = ut.dictionary
    for n in range(10):
        try:
            posts = browser.find_elements_by_css_selector("[class ^= 'v1Nh3 kIKUG']")
            for post in posts:
                ActionChains(browser).double_click(post).perform()
                time.sleep(2)
                if 10 * random.random() + 1 < 6 and commentwarn <= 20:
                    word = random.choice(dictionary)
                    ut.textcomment_explore(browser, word, logger)
                    commentwarn = commentwarn + 1
                else:
                    commentwarn = commentwarn + 2
                if ut.likepost(browser, logger):
                    liked += 1
                if browser.current_url != adres:
                    browser.back()
                if commentwarn > 36:
                    commentwarn = 0
            ut.execute_times(browser, 1)
        except (exceptionsln.TimeoutException, selenium.common.exceptions.StaleElementReferenceException,
                selenium.common.exceptions.InvalidElementStateException,
                selenium.common.exceptions.NoSuchElementException) as e:
            logger.error(e)
    logger.info('-->%s posts are liked!'%liked)
    return commentwarn, liked