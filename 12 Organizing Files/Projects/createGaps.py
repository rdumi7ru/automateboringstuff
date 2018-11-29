#!/usr/bin/python3
# Creates files with numbering gaps such as
# spam001.txt, spam003.txt, spam005.txt
# for fillingGaps.py program

import os, sys

def create(path):
    if os.path.exists(path):
        print('Folder %s exists.\nChangeing directory to %s.' % (path, path))
        print('Proceeding with file creation.\n')
        os.chdir(path)
    else:
        print('Folder %s does not exist, exiting...')
        sys.exit()

    pre = 'spam'
    ext = '.txt'

    for i in range(2, 12, 2):
        num = str(i)
        numJust = num.rjust(3, '0')
        files = pre + numJust + ext
        file = open(files, 'w')
        print('File %s was created.' % (files))
        file.close()

if __name__ == '__main__':
    create('/home/razvan/python/makedirs')

# Also I can use:
# for i in 001 002 004 005 006 009; do touch ${dir}/spam$i.txt ; echo $i > ${dir}/spam$i.txt; done
# for i in 011 012 014 025 026 319; do touch ${dir}/spam$i.txt ; echo $i > ${dir}/spam$i.txt; done
