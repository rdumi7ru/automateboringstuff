#!/usr/bin/python3
# Deletes files that are larger than 500MB
# Asks for your confirmation

import os, sys, bytesConvertor
from send2trash import send2trash

def dele(dir):
    dir = '/home/dmr/python/OrganisingFiles/deleteUnneededFiles'
    if os.path.exists(dir):
        print('Folder %s in path %s exists.' % (os.path.basename(dir), os.path.dirname(dir)))
    else:
        print('Folder %s or path %s does not exist!!!' % (os.path.basename(dir), os.path.dirname(dir)))
        sys.exit()
    
    # Walk thru directories
    for dirName, subDirs, filenames in os.walk(dir):
        print('Searching for files larger than 500MB')
        for filename in filenames:
            # file = os.path.join(dir, filename)
            size = bytesConvertor.btm(os.path.getsize(filename))
            reply = input('Delete filename: %s? [y/[n]]' % (filename))
            if filename >= 500 and reply == ('y|Y|yes|Yes'):
                print('Deleting file: %s' % (filename))
                send2trash(filename)
            else:
                print('File: %s, will not be deleted' % (filename))
                continue

if __name__ == '__main__':
    dele(dir)
