#!/usr/local/bin/python3.6

import os
os.chdir('/home/razvan/python')

for filename in os.listdir():
	if filename.endswith('.txt'):
		#os.unlink(filename)
		print(filename)
