#!/usr/bin/python3
# imageSiteDownloader.py downloads images from flickr.com

import requests, bs4, os, logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of the program')
# Check if the path exists
home = '/home/dmr/python/WebScraping/Projects'
work = '/home/razvan/python/WebScraping/Projects'

if os.path.exists(home):
    os.chdir(home)
    logging.debug('Changed the directory to %s' % (home))
elif os.path.exists(work):
    os.chdir(work)
    logging.debug('Changed the directory to %s' % (work))

# Get user input of what it needs to search
userInput = input('Please Enter a Category: ')
url = ('https://flickr.com/search/?text=' + userInput)

res = requests.get(url)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem %s' % (exc))
logging.debug('The page is %s' % (res))

soap = bs4.BeautifulSoup(res.text)
