#!/usr/bin/python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile
import os

def backupToZip(folder):
    os.chdir('/home/razvan/python/zip_project')
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)    # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files allready exists.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number)
