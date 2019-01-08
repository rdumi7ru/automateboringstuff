#!/usr/bin/python3
# RomeoAndJuliet.py changes directory to /home/user/python/WebScraping
# it reads the text from https://automatetheboringstuff.com/files/rj.txt
# and write it to RomeoAndJuliet.txt file

import requests, os, sys

try:
    os.chdir('/home/razvan/python/WebScraping')
except Exception as exc:
    print('An Error occurred: \n%s\nThe program will exit.' % (exc))
    sys.exit() 

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

if res.status_code == requests.codes.ok:
    nr = int(len(res.text)) + 100
    playFile = open('RomeoAndJuliet', 'wb')
    for chunk in res.iter_content(nr):
        playFile.write(chunk)
    playFile.close()
