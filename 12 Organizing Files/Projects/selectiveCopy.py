#!/usr/bin/python

import os
import shutil

def selectiveCopy(folder):
    # Move all .txt and .jpg to selectiveCopy2 folder
    folder = os.path.abspath(folder)

    # Walk the directory and search for files that ends with .txt and .jpg
    for folderName, subFolders, filenames in os.walk(folder):
        print('Searching for .txt and .jpg files in %s...' % (folderName))
        for filename in filenames:
            if filename.endswith('.jpg') and filenames.endswith('.txt'):
                shutil.copy(os.path.join(folder, filename),'/home/razvan/python/selectiveCopy2')
                
