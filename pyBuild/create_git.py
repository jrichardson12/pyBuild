"""
    Author: John Richardson
    Date: 7/9/2019
"""


import os
import subprocess


def createGit(path, projectName, githubUserName):
    os.chdir(path)
    subprocess.call("git init", shell=True)
    subprocess.call("git add README.md", shell=True)
    subprocess.call("git add " + projectName + ".py", shell=True)
    subprocess.call("git add .gitignore", shell=True)
    subprocess.call("git add README.md", shell=True)
    subprocess.call('git commit -m "first commit"', shell=True)
    subprocess.call("git remote add origin git@github.com:" +
                    githubUserName + "/" + projectName + ".git", shell=True)
    subprocess.call("git push -u origin master", shell=True)
