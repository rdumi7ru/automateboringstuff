#!/usr/bin/python3

import os
import sys
import shutil
from zipfile import ZipFile

def main(dir):
    dir = '/home/razvan/python/selectiveCopy'
    if os.path.exists(dir):
        os.chdir(dir)
    else:
        print(os.path.basename(dir) + ' folder, does not exist.')
    zip_file = os.path.join(dir, 'files.zip')
    extension = '.txt'
    backup(dir, zip_file, extension)
    print('Adding files from %s to %s archive' % (os.path.basename(dir), zip_file))

def backup(dir, zip_file, extension):
    with ZipFile(zip_file, 'w') as zip:
        for dirName, subDirs, files in os.walk(dir):
            lst = [x for x in files if x.endswith(extension)]
            if len(lst) > 0:
                for file in lst:
                    zip.write(os.path.join(dirName, file))
        zip.close()

if __name__ == '__main__':
    main(dir)
