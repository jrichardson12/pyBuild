def createFile(path, nameOfFile, fileList):
    try:
        file = open(path + nameOfFile, 'w')
        fileList.append(file)
    except OSError:
        print("Creation of the file %s failed" % name_of_file)
    else:
        print("Successfully created the file %s%s " %
              (path, nameOfFile))
    return file, fileList
