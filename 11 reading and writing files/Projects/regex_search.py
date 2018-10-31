#!/usr/bin/python3

import os
import re

os.chdir('/home/razvan/python')
regex = input(('Enter the patern:\n'))
regexSearch = re.compile(regex, re.I)
directory = input('Enter a directory name:\n')
dir = os.path.abspath(directory)
if os.path.exists(dir) == True:
    print(dir + ' folder exists')
    allFiles = os.listdir(dir)
    results = []
    for file in allFiles:
        if file.endswith('.txt'):
            content = open(os.path.join(dir, file))
            holder = []
            for line in content.readlines():
                if regexSearch.search(line):
                    holder.append( 'MATCH: ' + line + '\n')
            holder = [file + '\n' + '*'*20 + '\n' + ''.join(holder)]
            holder += '\n'*2
            results.append(holder)
            content.close()
    for result in results:
        print(result)
else:
    print('Folder ' + os.path.basename(dir) + ' does not exist!')
# result = regexSearch.findall()
