account = {
    "account_value": 0,
    "purchase_history": {},
}


def account_refill():
    amount = float(input("На какую сумму пополнить счет? "))
    return amount


def purchase(account_value):
    purchase_sum = float(input("Введите сумму покупки: "))
    if purchase_sum > account_value:
        print("*" * 10)
        print("Не достаточно средств, пополните счет.")
        print("*" * 10)
    else:
        purchase_item = input("Что вы хотите купить? ")
        money_left = account_value - purchase_sum
        account["purchase_history"][purchase_item] = purchase_sum
        account['account_value'] = money_left
        print(f"Вы купили {purchase_item}")
        print(f"На счету осталось {account['account_value']} денег")


def purchase_history():
    for key, value in account["purchase_history"].items():
        print(f"Вы купили {key} на сумму {value}")


def manage_bank_account():
    print("Welcome to bank account management!")
    print("Please pick a menu number below: ")
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            account['account_value'] = account_refill()
            print(
                f"Счет успешно пополнен. На вашем счету {account['account_value']} денег")
        elif choice == '2':
            purchase(account['account_value'])
        elif choice == '3':
            purchase_history()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')