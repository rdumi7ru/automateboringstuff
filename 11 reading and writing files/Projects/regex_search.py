#!/usr/bin/python3

import os
import re

directory = input('Enter a directory name:\n')

regex = input(('Enter the patern:\n'))
regexSearch = re.compile(regex, re.I)
result = regexSearch.findall()