def create_list_of_numbers() -> list:
    """
    Asks user to specify the number of elements and creates a list of numbers
    :return: list
    """
    list_of_numbers = []
    num_elements = int(input("Enter the number of elements: "))
    for element in range(num_elements):
        list_of_numbers.append(input(f"Enter {element + 1} element: "))

    return list_of_numbers


def count_percent(num, total_num) -> int:
    """
    Считает процент от общего числа
    :param num: число которое необходимо отобразить в процентах
    :param total_num: общее число (всего)
    :return: integer
    """
    return int(num * 100 / total_num)


def display_statistics(wrong, correct) -> None:
    """
    Выводит на экран статистику по игре
    :param wrong: количество неправильных ответов
    :param correct: количество правильных ответов
    :return: None
    """
    total_count = wrong + correct
    print(f"Правильных ответов: {correct}")
    print(f"Количество ошибок: {wrong}")
    print(f"Процент правильных ответов: {count_percent(correct, total_count)}")
    print(f"Процент неправильных ответов: {count_percent(wrong, total_count)}")


def play_again() -> bool:
    """
    Реализует логику завершения, либо продолжения игры
    :return: True or False
    """
    print("Сыграть еще раз?")
    answer = input("Введите 'да' или 'нет': ")
    while not answer.lower() in ['да', 'нет']:
        print("Неверный ввод, попробуйте еще раз ... ")
        answer = input("Введите 'да' или 'нет': ")
    if answer.lower() == 'нет':
        return False
    return True


days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одинадцатое',
    '12': 'двенадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадцатое',
    '21': 'двадцать первое',
    '22': 'двадцать второе',
    '23': 'двадцать третье',
    '24': 'двадцать четвертое',
    '25': 'двадцать пятое',
    '26': 'двадцать шестое',
    '27': 'двадцать седьмое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '30': 'тридцатое',
    '31': 'тридцать первое',
}

months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря',
}