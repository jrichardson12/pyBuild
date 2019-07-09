"""
    Author: John Richardson
    Date: 7/9/2019
"""


import sys


def correctSlash():
    slashDictionary = {
        'win': '\\',
        'linux': '/',
    }
    slash = '/'
    # Create new Win File ----------------------------------------------------|
    if sys.platform == 'win32':
        slash = slashDictionary['win']
    else:
        slash = slashDictionary['linux']
    return slash
