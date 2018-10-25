#!/usr/bin/python3.4

import os

for folderName, subFolders, filenames in os.walk('/home/razvan/python/delicious'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subFolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()
