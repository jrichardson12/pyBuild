"""
    Author: John Richardson
    Date: 7/9/2019
"""


import os
import sys


def createDir(path, nameOfDir):
    has_passed = False
    try:
        if sys.platform == 'win32':
            os.mkdir(path + '\\' + nameOfDir)
        else:
            os.mkdir(path + '/' + nameOfDir)
    except OSError:
        print("Creation of the directory %s failed" % nameOfDir)
        has_passed = False
    else:
        print("Successfully created the directory %s%s " %
              (path, nameOfDir))
        has_passed = True
    return has_passed
