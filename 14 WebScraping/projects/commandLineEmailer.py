#!/usr/bin/python3
# commandLineEmailer.py takes an email address and 
# a sting of text from the command line and then
# using selenium to log into the gmail and send 
# an email.

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# 
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of %s program' % (sys.argv[0]))

if len(sys.argv) != 3:
    logging.debug(sys.argv[0] + 'aspects 2 arguments, you only provided' + ' ' + str(len(sys.argv)))
    logging.debug('This program will now exit')
    sys.exit()
else:
    email = sys.argv[1]
    message = sys.argv[2]
    password = 'your_password'

logging.debug('The email address is "%s" and the message is "%s"' % (email, message))

# Select Firefox driver, and create the structure. 
browser = webdriver.Firefox()
browser.get('https://mail.google.com/mail')
uElem = browser.find_element_by_id('identifierId').send_keys(email)
nElem = browser.find_element_by_id('identifierNext').click()
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
pElem = browser.find_element_by_xpath("//*[@name='password']").send_keys(password)
fElem = browser.find_element_by_id('passwordNext').click()
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "T-I.J-J5-Ji.T-I-KE.L3")))
cElem = browser.find_element_by_css_selector('.T-I.J-J5-Ji.T-I-KE.L3').click()



logging.debug('End of program')
