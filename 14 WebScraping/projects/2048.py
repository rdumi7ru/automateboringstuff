#!/usr/bin/python3
# 2048 is a simple game where you combine tiles by 
# sliding them up, down, left, or right with the arrow keys.
# You can actually get a fairly high score be repeatedly
# sliding in a up, right, down, and left pattern over 
# and overagain. 
# I use here https://gabrielecirulli.github.io/2048/

import time, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmElem = browser.find_element_by_tag_name('html')
while True:
    htmElem.send_keys(Keys.UP)
    time.sleep(1)
    htmElem.send_keys(Keys.RIGHT)
    time.sleep(1)
    htmElem.send_keys(Keys.DOWN)
    time.sleep(1)
    htmElem.send_keys(Keys .LEFT)
    time.sleep(1)
    if browser.find_element_by_class_name("game-message").is_displayed():
        sys.exit()
