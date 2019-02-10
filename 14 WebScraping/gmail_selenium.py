#!/usr/bin/python3
# gmail_selenium.py tests gmail login

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('https://mail.google.com/mail')
uElem = browser.find_element_by_id('identifierId').send_keys('dumitru.rm')
nEelem = browser.find_element_by_id('identifierNext').click()

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
pElem = browser.find_element_by_xpath("//*[@name='password']").send_keys('your_password')

fElem = browser.find_element_by_id('passwordNext').click()
