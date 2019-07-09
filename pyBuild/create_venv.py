"""
    Author: John Richardson
    Date: 7/9/2019
"""


import os
import subprocess


def createVenv(path, projectVenv):
    os.chdir(path)
    subprocess.call('virtualenv ' + projectVenv, shell=True)
    return True
