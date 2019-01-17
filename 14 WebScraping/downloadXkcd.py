#!/usr/bin/python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com'             # starting url
os.chdir('home/dmr/python')
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find image.')
    else:
        comicUrl = 'http:' + 
    # TODO: Download the image.
    # TODO: Save the image to ./xkcd
    # TODO: Get the Prev button's url.

print('Done.')
