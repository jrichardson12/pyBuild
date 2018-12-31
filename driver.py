import sys
import os
import subprocess
import getpass
import os.path
import includes.dependency
import includes.installer
import includes.mainFile
import includes.readme
import includes.gitignore


def createFile(path, name_of_file, file_list):
    try:
        file = open(path + name_of_file, 'w')
        file_list.append(file)
    except OSError:
        print("Creation of the file %s failed" % name_of_file)
    else:
        print("Successfully created the file %s%s " %
              (path, name_of_file))
    return file, file_list


def createVenv(path, project_venv):
    os.chdir(path)
    subprocess.call('virtualenv ' + project_venv, shell=True)
    return True


def createGit(path, project_name, github_user_name):
    os.chdir(path)
    subprocess.call("git init", shell=True)
    subprocess.call("git add README.md", shell=True)
    subprocess.call("git add " + project_name + ".py", shell=True)
    subprocess.call("git add .gitignore", shell=True)
    subprocess.call("git add README.md", shell=True)
    subprocess.call('git commit -m "first commit"', shell=True)
    subprocess.call("git remote add origin git@github.com:" +
                    github_user_name + "/" + project_name + ".git", shell=True)
    subprocess.call("git push -u origin master", shell=True)


def createDir(path, name_of_dir):
    has_passed = False
    try:
        if sys.platform == 'win32':
            os.mkdir(path + '\\' + name_of_dir)
        else:
            os.mkdir(path + '/' + name_of_dir)
    except OSError:
        print("Creation of the directory %s failed" % name_of_dir)
        has_passed = False
    else:
        print("Successfully created the directory %s%s " %
              (path, name_of_dir))
        has_passed = True
    return has_passed


def main():
    print(sys.platform)
    print(sys.version)
    path = ""
    user = getpass.getuser()
    project_name = ""
    project_venv = ""
    project_main_file = ""
    github_user_name = ""
    file_list = []
    # ------------------------------------------------------------------------|
    # Project Name Check -----------------------------------------------------|
    # ------------------------------------------------------------------------|
    number_of_tries = 3
    while number_of_tries > 0:
        project_name = input("Please enter a project name: ")
        github_user_name = input("Please Enter a GitHub user name: ")
        if len(project_name) >= 2:
            project_venv = project_name + "venv"
            project_main_file = project_name + ".py"
            break
        else:
            print("Please enter a file name with 2 or more characters")
            number_of_tries -= 1
            print("Number of Tries left: %s" % number_of_tries)
            if number_of_tries == 0:
                print('File name is not long enough')
                sys.exit(0)
    # End Project Name Check -------------------------------------------------|
    assert sys.version_info >= (3, 5)  # Check Python Version
    # ------------------------------------------------------------------------|
    # Create Files needed for each OS                                         |
    # ------------------------------------------------------------------------|
    if sys.platform == 'linux':
        print('Linux Box')
    # Create new Win File ----------------------------------------------------|
    elif sys.platform == 'win32':
        path = ('C:\\Users\\' +
                user +
                '\\Documents\\projects\\')
        try:
            if os.path.isdir(path):
                if os.path.isdir(path + "\\" + project_name):
                    print('Project Already Exists')
                else:
                    os.mkdir(path + "\\" + project_name)
            else:
                os.makedirs(path + "\\" + project_name)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s%s " %
                  (path, project_name))
        path = path + project_name + "\\"
        createDir(path, "log")
        createDir(path, "python")
        createDir(path, "includes")
        driver_file = createFile(path, project_main_file, file_list)
        gitignore_file = createFile(path, '.gitignore', file_list)
        # installer_file = createFile(path, "installer.exe", file_list)
        dependency_file = createFile(path, "dependency.py", file_list)
        readme_file = createFile(path, "README.md", file_list)
        dependency_file[0].write(includes.dependency.dependency_file())
        driver_file[0].write(includes.mainFile.driver_file())
        readme_file[0].write(includes.readme.readme_file())
        gitignore_file[0].write(includes.gitignore.gitignore_file())
        # installer_file[0].write(includes.installer.winInstaller())
        createGit(path, project_name, github_user_name)
        createVenv(path, project_venv)
    # End Win ----------------------------------------------------------------|
    elif sys.platform == 'cygwin':
        print('Cygwin Box')
    elif sys.platform == 'darwin':
        print('MAC box')
    else:
        print('unable to detect OS')
        sys.exit(0)
    for file in file_list:
        file.close()


if __name__ == '__main__':
    main()
    # os.system('cls')
