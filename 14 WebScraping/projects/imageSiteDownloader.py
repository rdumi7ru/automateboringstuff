#!/usr/bin/python3
# imageSiteDownloader.py downloads images from flickr.com

import requests, bs4, os, logging, json

# Set up logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of the program')
# Check if the path exists
home = '/home/dmr/python/webscraping/unsplash'
work = '/home/razvan/python/WebScraping/Projects'

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
pageNum = 1
while pageNum < 100:
    res = requests.get(url + pageNum)
    try:
        res.raise_for_status()
    except Exception as exc:
       print('There was a problem %s' % (exc))
    jD = json.loads(res.text)
    for i in range(0, 20):
        name = jD['results'][i]['description']
        if name == None:
            continue
        name = name = name = jD['results'][i]['description'] + '.png'
#        img = jD['results'][i]['raw']
        img = requests.get(jD['results'][i]['urls']['raw'])
        imageFile = open(name, 'wb')
        for chunk in img.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
#        with open(name, 'wb') as writeFile:
#            json.dump(img, writeFile)
    pageNum += 1
logging.debug('The page is %s' % (res))
