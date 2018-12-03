#!/usr/bin/python
# Finds all the files with a given prefix, such as spam001.txt
# spam002.txt and so on, and locates any gaps in the numbering
# such as if there is a spam001.txt and spam003.txt but no spam002.txt

import os, re 

def gaps(dir):
    dir = '/home/razvan/python/12OrganisingFiles/fillingGaps'

    regex = re.compile(r'^(spam)(d+)(.txt)')

    lst = []

    for file in os.listdir(dir):
        num = regex.search(file).group(2)
        lst.append( (int(num.lstrip('0')), file, len(num)) )

    lst = sorted(lst)
    
    
