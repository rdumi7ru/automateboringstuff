#!/usr/bin/python3

import os, sys

try:
    os.chdir('home/razvan')
except Exception as exc:
    print('An error occurred: %s\nThe program will exit' % (exc))

    sys.exit()

print('Hello')
