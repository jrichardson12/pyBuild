"""
    Author: John Richardson
    Date: 7/9/2019
"""


def createFile(path, nameOfFile, fileList):
    try:
        file = open(path + nameOfFile, 'w')
        fileList.append(file)
    except OSError:
        print("Creation of the file %s failed" % nameOfFile)
    else:
        print("Successfully created the file %s%s " %
              (path, nameOfFile))
    return file, fileList
