"""
    Author: John Richardson
    Date: 7/9/2019
"""


import os
import sys


def createPath(user):
    # TODO: Add path selection
    if sys.platform == 'linux':
        path = ('/home/' + user + '/projects/')
        # TODO: Add Linux path
    # Create new Win File ----------------------------------------------------|
    elif sys.platform == 'win32':
        path = ('C:\\Users\\' +
                user +
                '\\Documents\\projects\\')
    elif sys.platform == 'cygwin':
        print('Cygwin Path')
        # TODO: Add Cygwin Path
    elif sys.platform == 'darwin':
        print('MAC Path')
        # TODO: Add Mac Path
    else:
        print('unable to detect OS')
        sys.exit(0)
    return path


def changePath(path, projectName, slash):
    path = path + projectName + slash
    return path


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
