import os
import shutil
import sys
import platform


def choice(question):
    result = input(question + "? (y/n): ")
    if result.lower() == "n":
        return False
    return True


def create_folder(folder_name):
    """
    Takes a string as a folder name and creates a folder in the current directory
    :param folder_name: str
    :return: None
    """
    while True:
        if os.path.exists(folder_name):
            print("The folder with this name already exists.")
            folder_name = input("Please enter the other name: ")
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print("Folder was created")
            break


def delete_folder():
    """
    Deletes a folder or a file of user choice
    :return: None
    """
    keep_asking = True
    while keep_asking:
        f_name = input("Enter the folder/file name to delete: ")
        if os.path.isdir(f_name):
            if os.path.exists(f_name):
                os.rmdir(f_name)
                print("Folder deleted")
            else:
                print("This folder doesn't exist")
        elif os.path.isfile(f_name):
            if os.path.exists(f_name):
                os.remove(f_name)
                print("The file deleted")
            else:
                print("This file doesn't exist")
        else:
            print("This doesn't exist, try another")

        choice = input("Delete another? (y/n): ")
        if choice.lower() == "n":
            keep_asking = False


# Opted out this function as os.mknod requires root privileges on
# MacOS, therefore may not work for some users
# def create_file():
#     f_name = input("Enter the file name to create: ")
#     if not os.path.exists(f_name):
#         os.mknod(f_name)
#         print("The file created")
#     else:
#         print("The file already exists")


def create_file():
    keep_asking = True
    create_another = True
    while create_another:
        while keep_asking:
            f_name = input("Enter the file name to create: ")
            if not os.path.exists(f_name):
                open(f_name, 'a').close()
                print("The file created")
                break
            else:
                print("The file already exists")

            keep_asking = choice("Try another name")
        create_another = choice("Create another file")


def copy_file():
    keep_asking = True
    copy_another = True
    while copy_another:
        while keep_asking:
            f_name = input("Enter the folder/file name to copy: ")
            copy_name = input("Enter the name for copy: ")
            if os.path.exists(f_name):
                if not os.path.exists(copy_name):
                    if os.path.isfile(f_name):
                        shutil.copy(f_name, copy_name)
                        print("The file copied")
                        break
                    elif os.path.isdir(f_name):
                        shutil.copytree(f_name, copy_name)
                        print("Success!")
                        break
                else:
                    print("The name already exists")
            else:
                print("The file with this name doesn't exist")
            keep_asking = choice("Try another name")

        copy_another = choice("Copy another file")


def show_dir_content():
    """
    Returns list of working directory content
    :return: list
    """
    return os.listdir(os.getcwd())


def show_dir_only():
    dirs = []
    for item in os.listdir(os.getcwd()):
        if os.path.isdir(item):
            dirs.append(item)
    return dirs


def show_file_only():
    files = []
    for item in os.listdir(os.getcwd()):
        if os.path.isfile(item):
            files.append(item)
    return files


def show_os_info():
    print(platform.platform())
    print("System name: ", platform.system())
    print("Release: ", platform.release())
    print("Version: ", platform.version())