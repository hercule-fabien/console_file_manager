import os
import sys


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
    keep_asking = True
    while keep_asking:
        f_name = input("Enter the folder/file name to delete: ")
        if os.path.exists(f_name):
            os.rmdir(f_name)
            print("Folder/file deleted")
        else:
            print("This folder doesn't exist")

        choice = input("Delete another? (y/n): ")
        if choice.lower() == "n":
            keep_asking = False
