#!/usr/bin/python3
# Finds all the files with a given prefix, such as spam001.txt
# spam002.txt and so on, and locates any gaps in the numbering
# such as if there is a spam001.txt and spam003.txt but no spam002.txt

import os, re, shutil, sys

def gaps(dir):
    dir = '/home/razvan/python/12OrganisingFiles/fillingGaps'
    if os.path.exists(dir):
        print('Folder {0} exists.'.format(os.path.basename(dir)))
        print('Changeing to {0} folder.'.format(dir))
        os.chdir(dir)
    else:
        print('Folder {0} does not exist, exiting...'.format(dir))
        sys.exit()

    regex = re.compile(r'^(spam)(\d+)(.txt)')

    lst = []

    for file in os.listdir(dir):
        num = regex.search(file).group(2)
        lst.append( (int(num.lstrip('0')), file, len(num)) )

    lst = sorted(lst)
    for index in range(len(lst)):
        padding = lst[index][2]
        num = str(int(index) + 1)
        padded_num = num.rjust(padding, '0')
        src = os.path.join(dir, lst[index][1])
        dst = os.path.join(regex.sub(r'\g<1>%s\g<3>' % (padded_num), lst[index][1]))
        shutil.move(src, dst)

if __name__ == '__main__':
    gaps(dir)
