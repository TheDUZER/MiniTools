"""
Place this file in a directory, makes adjustments
to the commented code, and run it to check
file names in that directory for specified patterns
and rename them as desired.
"""

import os, sys, re

for files in os.listdir(sys.path[0]):
    try:
        #Replace REGEX below with a string or regular expression to check.
        if re.match#(REGEX, files):
            #replace NEW_FILE_NAME below with desired file name.
            os.rename#(files, NEW_FILE_NAME)
        #Repeat the IF statement above as ELIF statements as desired for
        #additional parameters.
        else:
            continue
    except:
        print(f'ERROR: Script encountered an error while processing:\n\t{files}')
print('DONE')
