import datetime


def writeMain(projectName):
    text = """\"""
     author: John Richardson
       date: """ + str(datetime.date.today()) + """
    version: 0.1
\"""

import os

import """ + projectName + """

"""
    return text


def writeGitIgnore():
    text = """.pyc"""
    return text


def writeHeader():
    text = """\"""
     author: John Richardson
       date: """ + str(datetime.date.today()) + """
    version: 0.1
\"""
"""
    return text
