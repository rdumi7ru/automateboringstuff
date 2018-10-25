#!/usr/bin/python3.4

import os, shutil

for folderName, subFolders, filenames in os.walk('/home/razvan/python/delicious'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subFolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    for subfolder in subFolders:
        if 'fish' in subfolder:
            os.rmdir(subfolder)
    
    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.path.join(folderName, file), os.path.join(folderName, file + '.backup'))
