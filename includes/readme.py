import datetime


def readme_file():
    text = """
===============================================================================|
author: John Richardson
date: """ + str(datetime.date.today()) + """
version: 1.0
===============================================================================|
dependency:
===============================================================================|
description:
===============================================================================|
"""
    return text
