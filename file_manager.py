import os
import sys


def create_folder(folder_name):
    """
    Takes a string as a folder name and creates a folder in the current directory
    :param folder_name: str
    :return: None
    """
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

