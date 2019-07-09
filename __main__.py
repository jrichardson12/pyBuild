"""
    Author: John Richardson
    Date: 7/9/2019
"""

import sys
import getpass

import pyBuild

print(sys.platform)
print(sys.version)
slash = ''
path = ""
user = getpass.getuser()
projectName = ""
projectVenv = ""
projectMainFile = ""
githubUserName = ""
fileList = []
# ------------------------------------------------------------------------|
# Project Name Check -----------------------------------------------------|
# ------------------------------------------------------------------------|
numberOfTries = 3
while numberOfTries > 0:
    projectName = input("Please enter a project name: ")
    githubUserName = input("Please Enter a GitHub user name: ")
    if len(projectName) >= 2:
        projectVenv = projectName + "venv"
        projectMainFile = projectName + ".py"
        break
    else:
        print("Please enter a file name with 2 or more characters")
        numberOfTries -= 1
        print("Number of Tries left: %s" % numberOfTries)
        if numberOfTries == 0:
            print('File name is not long enough')
            sys.exit(0)
# End Project Name Check -------------------------------------------------|
assert sys.version_info >= (3, 5)  # Check Python Version
# ------------------------------------------------------------------------|
# Create and Check Path---------------------------------------------------|
# ------------------------------------------------------------------------|
slash = pyBuild.correctSlash()
path = pyBuild.createPath(user)
checkPath = pyBuild.checkPath(path, projectName, slash)
if checkPath:
    path = pyBuild.changePath(path, projectName, slash)
else:
    sys.exit(0)
print(path)
pyBuild.createDir(path, projectName, slash)
pyBuild.createDir(path, 'test', slash)
# ------------------------------------------------------------------------|
# Create Files needed for each OS                                         |
# ------------------------------------------------------------------------|
if sys.platform == 'linux':
    print('Linux Box')
# Create new Win File ----------------------------------------------------|
elif sys.platform == 'win32':
    print('Win32 Box')
elif sys.platform == 'cygwin':
    print('Cygwin Box')
elif sys.platform == 'darwin':
    print('MAC box')
else:
    print('unable to detect OS')
    sys.exit(0)
for file in fileList:
    file.close()
