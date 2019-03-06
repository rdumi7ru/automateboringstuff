#!/usr/bin/python3
# imageSiteDownloader.py downloads images from flickr.com

import requests, bs4, os, logging, json

# Set up logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of the program')
# Check if the path exists
home = '/home/dmr/python/webscraping/unsplash'
work = '/home/razvan/python/WebScraping/Projects/imageSiteDownloader'

if os.path.exists(home):
    os.chdir(home)
    logging.debug('Changed the directory to %s' % (home))
elif os.path.exists(work):
    os.chdir(work)
    logging.debug('Changed the directory to %s' % (work))

# Get user input of what it needs to search
userInput = input('Please Enter a Category: ')
prefixUrl = 'https://unsplash.com/napi/search/photos?query='
ext = '&xp=&per_page=20&page='
url = (prefixUrl + userInput + ext)
numPage = input('Please enter the number of pages you want to download.\nThere are 20 images on page: ')
pageNum = 1
while pageNum <= int(numPage):
    res = requests.get(url + str(pageNum))
    try:
        res.raise_for_status()
    except Exception as exc:
       print('There was a problem %s' % (exc))
    jD = json.loads(res.text)
    for i in range(0, 20):
        name = jD['results'][i]['description']
        if name == None:
            continue
        name = '_'.join(name.split()) + '.jpg'
        logging.debug('Downloading %s' % (name))
        img = requests.get(jD['results'][i]['urls']['raw'])
        imageFile = open(name, 'wb')
        for chunk in img.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    pageNum += 1
