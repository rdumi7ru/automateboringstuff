#!/usr/bin/python3
# mp3Downloader.py downloads mp3 files from https://libfm.com 
# it handles bulk and single downloads

import requests, os, bs4, json, re

s = open('/home/razvan/Documents/IBM/SmoothJazz.txt', 'r')
ss = s.read()
songs = re.split('\u200e|\n', ss)
list(filter(None, songs))
list(filter(lambda i: i != '', songs))
songs = list(filter(lambda i: i != '', songs))
listOfStr = ["hello", "at" , "test" , "this" , "here" , "now" ]
dictOfWords = { i : listOfStr[i] for i in range(0, len(listOfStr)) }
dictOfWords
dictOfWords = json.dumps(dictOfWords)
loadedDictOfWords = json.loads(dictOfWords)
loadedDictOfWords
a
a
