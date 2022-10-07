from bank_account import manage_bank_account
from file_manager import *


def main():
    print("Welcome to the File Manager")
    print("*" * 27)
    print("Please pick your desired action from the menu below: ")
    print("""
        1. Create a folder.
        2. Create a file.
        3. Delete (file/folder).
        4. Copy (file/folder).
        5. Check the files in the working directory.
        6. Display folders only.
        7. Display files only.
        8. Check OS type.
        9. Show credits.
        10. Play the Victory game.
        11. Check you bank account status.
        12. Change working directory.
        13. Quit.
    """)

    while True:
        user_choice = int(input("Choose menu item to continue: "))
        if user_choice in range(1, 14):
            if user_choice == 1:
                f_name = input("Enter the folder name: ")
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
                pass
            elif user_choice == 9:
                pass
            elif user_choice == 10:
                pass
            elif user_choice == 11:
                manage_bank_account()
            elif user_choice == 12:
                pass
            elif user_choice == 13:
                print("Good bye!")
                break
        else:
            print("Please enter a valid option between 1-13")


if __name__ == '__main__':
    main()
