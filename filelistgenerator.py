"""
Place this file in a directory and
run it to generate a list of all
other file names in that directory.
"""

import sys, os

filename_list = os.listdir(sys.path[0])

with open(os.path.join(sys.path[0], 'filelist.csv'), 'a') as newfile:
    for x in filename_list:
        if x == "filelistgenerator.py":
            pass
        else:
            newfile.writelines(x + '\n')
            
