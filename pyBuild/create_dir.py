"""
    Author: John Richardson
    Date: 7/9/2019
"""


import os


def createDir(path, nameOfDir, slash):
    hasPassed = False
    try:
        os.mkdir(path + slash + nameOfDir)
    except OSError:
        print("Creation of the directory %s failed" % nameOfDir)
        hasPassed = False
    else:
        print("Successfully created the directory %s%s " %
              (path, nameOfDir))
        hasPassed = True
    return hasPassed
