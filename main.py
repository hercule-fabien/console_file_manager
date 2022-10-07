from bank_account import manage_bank_account
from file_manager import *
from victory import victory_game


def main():
    print("Приветствую в программе File Manager")
    print("*" * 27)
    print("""
        1. Создать папку.
        2. Создать файл.
        3. Удалить (файл/папку).
        4. Копировать (файл/папку).
        5. Посмотреть содержимое рабочей директории.
        6. Отобразить только папки.
        7. Отобразить только файлы.
        8. Посмотреть информацию об ОС.
        9. Создатель программы.
        10. Играть в викторину.
        11. Мой банковский счет.
        12. Смена рабочей директории.
        13. Выход.
    """)

    while True:
        try:
            user_choice = int(input("Выберите действие из меню - введите число (1-13): "))
        except ValueError:
            print("Это не целое число!")
            print("Пожалуйста введите только целое число между 1-13")
        else:
            if user_choice in range(1, 14):
                if user_choice == 1:
                    f_name = input("Введите имя для папки: ")
                    create_folder(f_name)
                elif user_choice == 2:
                    create_file()
                elif user_choice == 3:
                    delete_folder()
                elif user_choice == 4:
                    copy_file()
                elif user_choice == 5:
                    for item in show_dir_content():
                        print("*", item)
                elif user_choice == 6:
                    for item in show_dir_only():
                        print("*", item)
                elif user_choice == 7:
                    for item in show_file_only():
                        print("*", item)
                elif user_choice == 8:
                    show_os_info()
                elif user_choice == 9:
                    print("Created by Vasily Glazkov")
                elif user_choice == 10:
                    victory_game()
                elif user_choice == 11:
                    manage_bank_account()
                elif user_choice == 12:
                    pass
                elif user_choice == 13:
                    print("Работа программы завершена! Хорошего дня!")
                    break
            else:
                print("Пожалуйста введите только число в диапазоне от 1 до 13")


if __name__ == '__main__':
    main()
