#!/usr/bin/python

import os
import shutil

def selectiveCopy(folder, destFolder):
    # Move all .txt and .jpg to selectiveCopy2 folder
    folder = os.path.abspath(folder)
    destFolder = os.path.abspath(destFolder)

    # Walk the directory and search for files that ends with .txt and .jpg
    for folderName, subFolders, filenames in os.walk(folder):
        print('Searching for .txt and .jpg files in %s...' % (folderName))
        for filename in filenames:

            if filename.endswith('.jpg') and filenames.endswith('.txt'):
                print('Copying %s from %s to %s' % (filename, folder, destFolder))
                shutil.copy(os.path.join(folder, filename), destFolder)
                
if __name__ == '__main__':
    selectiveCopy('/home/razvan/python/selectiveCopy', '/home/razvan/python/selectiveCopy2')
