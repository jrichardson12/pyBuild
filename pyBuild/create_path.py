"""
    Author: John Richardson
    Date: 7/9/2019
"""

import sys


def createPath(user):
    # TODO: Add path selection
    if sys.platform == 'linux':
        print('Linux Path')
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


def changePath(path):
    pass
