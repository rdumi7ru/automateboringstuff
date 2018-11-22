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
        print(os.path.basename + ' folder, does not exist.')

    zip_file = os.path.join(dir, 'files.zip')
    backup(dir, zip_file)
    print('Destination ZIP file: %s' % (zip_file))

def backup(dir, zip_file):
    with ZipFile(zip_file, 'w') as zip:
        for dirName, subDirs, files in os.walk(dir):
            # Adding files in zip archive
            for file in files:
                if file.endswith('.txt') or file.endswith('.jpg'):
                    zip.write(os.path.join(dirName, file))
        zip.close()

if __name__ == '__main__':
    main(dir)
