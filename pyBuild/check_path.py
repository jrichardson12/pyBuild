import os


def checkPath(path, projectName):
    hasPassed = False
    try:
        if os.path.isdir(path):
            if os.path.isdir(path + "\\" + projectName):
                print('Project Already Exists')
            else:
                # creates just the projectName folder
                os.mkdir(path + "\\" + projectName)
                hasPassed = True
        else:
            # creates folders to project name
            os.makedirs(path + "\\" + projectName)
            hasPassed = True
    except OSError:
        print("Creation of the directory %s failed" % path)
    if hasPassed:
        print("Successfully created the directory %s%s " %
              (path, projectName))
    return hasPassed
