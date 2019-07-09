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
githubUserName = ""
fileList = []
# ------------------------------------------------------------------------|
# Project Name Check                                                      |
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
assert sys.version_info >= (3, 5)  # Check Python Version
# ------------------------------------------------------------------------|
# Create and Check Path                                                   |
# ------------------------------------------------------------------------|
slash = pyBuild.correctSlash()
path = pyBuild.createPath(user)
checkPath = pyBuild.checkPath(path, projectName, slash)
if checkPath:
    path = pyBuild.changePath(path, projectName, slash)
else:
    sys.exit(0)
pyBuild.createDir(path, projectName, slash)
pyBuild.createDir(path, 'test', slash)
# ------------------------------------------------------------------------|
# Create Files                                                            |
# ------------------------------------------------------------------------|
mainFile = pyBuild.createFile(path, '__main__.py', fileList)
setupFile = pyBuild.createFile(path, 'setup.py', fileList)
gitignoreFile = pyBuild.createFile(path, '.gitignore', fileList)
readmeFile = pyBuild.createFile(path, "README.md", fileList)
initFile = pyBuild.createFile(path + projectName + slash,
                              "__init__.py",
                              fileList)
# ------------------------------------------------------------------------|
# Write Files                                                             |
# ------------------------------------------------------------------------|
mainFile[0].write(pyBuild.writeMain(projectName))
setupFile[0].write(pyBuild.writeHeader())
gitignoreFile[0].write(pyBuild.writeGitIgnore())
initFile[0].write(pyBuild.writeHeader())
pyBuild.createGit(path, projectName, githubUserName)
pyBuild.createVenv(path, projectVenv)
# ------------------------------------------------------------------------|
# Close all Created Files                                                 |
# ------------------------------------------------------------------------|
for file in fileList:
    file.close()
