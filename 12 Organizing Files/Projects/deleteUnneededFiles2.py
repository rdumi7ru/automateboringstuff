#!/usr/bin/python3
# Deletes files that are larger than 500MB
# Asks for your confirmation

import os
import sys
import bytesConvertor
from send2trash import send2trash
from pprint import pprint

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
        