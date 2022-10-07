import os
import shutil
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
            print("Папка с таким именем уже существует.")
            folder_name = input("Выберите другое имя: ")
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print("Папка создана успешно")
            break


def delete_folder():
    """
    Deletes a folder or a file of user choice
    :return: None
    """
    keep_asking = True
    while keep_asking:
        f_name = input("Введите имя папки/файла для удаления: ")
        if os.path.isdir(f_name):
            if os.path.exists(f_name):
                os.rmdir(f_name)
                print("Папка удалена")
            else:
                print("Такой папки не существует")
        elif os.path.isfile(f_name):
            if os.path.exists(f_name):
                os.remove(f_name)
                print("Файл удален")
            else:
                print("Такой файл не существует")
        else:
            print("Не понял вас, попробуйте другое имя")

        choice = input("Удалить еще? (y/n): ")
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
            f_name = input("Введите имя создаваемого файла: ")
            if not os.path.exists(f_name):
                open(f_name, 'a').close()
                print("Файл создан успешно")
                break
            else:
                print("Такой файл существует")

            keep_asking = choice("Попробовать другое имя")
        create_another = choice("Создать еще файл")


def copy_file():
    keep_asking = True
    copy_another = True
    while copy_another:
        while keep_asking:
            f_name = input("Какую папку или файл вы хотите скопировать?_ ")
            copy_name = input("Как назовем копию?_ ")
            if os.path.exists(f_name):
                if not os.path.exists(copy_name):
                    if os.path.isfile(f_name):
                        shutil.copy(f_name, copy_name)
                        print("Файл скопирован")
                        break
                    elif os.path.isdir(f_name):
                        shutil.copytree(f_name, copy_name)
                        print("Успех! Папка скопирована!")
                        break
                else:
                    print("Такое имя существует")
            else:
                print("Папка или файл с таким именем уже существует")
            keep_asking = choice("Попробовать другое имя")

        copy_another = choice("Скопировать еще")


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


def change_cwd():
    print("""
    Пример ввода пути: test_folder_1,
                       test_folder_1/test_folder_2,
                       и т.д.
    Чтобы подняться на уровень выше: ../,
                                     ../..,
                                     и т.д.
    """)
    new_path = input("Введите путь к папке: ")
    try:
        os.chdir(new_path)
    except:
        print("Неверно указан путь")
    else:
        print("Новая рабочая директория: ", os.getcwd())
