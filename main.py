from bank_account import manage_bank_account
from file_manager import create_folder, delete_folder


def main():
    print("Welcome to the File Manager")
    print("*" * 27)
    print("Please pick your desired action from the menu below: ")
    print("""
        1. Create a folder.
        2. Delete (file/folder).
        3. Copy (file/folder).
        4. Check the files in the working directory.
        5. Display folders only.
        6. Display files only.
        7. Check OS type.
        8. Credits.
        9. Play the Victory game.
        10. Check you bank account status.
        11. Change working directory.
        12. Quit.
    """)

    while True:
        user_choice = int(input("Choose menu item to continue: "))
        if user_choice in range(1, 13):
            if user_choice == 10:
                manage_bank_account()
            elif user_choice == 1:
                f_name = input("Enter the folder name: ")
                create_folder(f_name)
            elif user_choice == 2:
                delete_folder()
            elif user_choice == 12:
                print("Good bye!")
                break
        else:
            print("Please enter a valid option between 1-12")


if __name__ == '__main__':
    main()
