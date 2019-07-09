"""
    Author: John Richardson
    Date: 7/9/2019
"""


import os


def checkPath(path, projectName, slash):
    hasPassed = False
    # Create new Win File ----------------------------------------------------|
    try:
        if os.path.isdir(path):
            if os.path.isdir(path + slash + projectName):
                print('Project Already Exists')
            else:
                # creates just the projectName folder
                os.mkdir(path + slash + projectName)
                hasPassed = True
        else:
            # creates folders to project name
            os.makedirs(path + slash + projectName)
            hasPassed = True
    except OSError:
        print("Creation of the directory %s failed" % path)
    if hasPassed:
        print("Successfully created the directory %s%s " %
              (path, projectName))
    return hasPassed
