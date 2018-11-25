#!/usr/bin/python3
# Deletes files that are larger than 100MB
# It asks user to confirm

import os
import shutil
import sys
import send2trash
import bytesConvertor

def dele(dir):
    dir = '/home/dmr/python/deleteUnneededFiles'
    if os.path.exists(dir):
        print('folder %s exists.' % (dir))
    else:
        print('%s folder does not exist, exiting...' % (dir))
        sys.exit()
    for folderName, subFolders, filenames in os.walk(dir):
        print("Searching for files bigger that 500MB")
        for filename in filenames:
            file = os.path.join(dir, filename)
            size = bytesConvertor.btm(os.path.getsize(file))
            if size >= 500:
                print('Deleting %s file' % (filename))
                send2trash.send2trash(file)

if __name__ == '__main__':
    dele(dir)