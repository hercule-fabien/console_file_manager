from utils import display_statistics, play_again, days, months
import random

famous_people = {
    "Александр Пушкин": "26.05.1799",
    "Лев Толстой": "28.08.1828",
    "Гвидо ван Россум": "31.01.1956",
    "Алан Тьюринг": "23.06.1912",
    "Дмитрий Менделеев": "27.01.1834",
    "Абрам Иоффе": "17.10.1880",
    "Альберт Эйнштейн": "14.03.1879",
    "Нильс Бор": "07.10.1885",
    "Михаил Ломоносов": "08.11.1711",
    "Александр Попов": "04.03.1859",
}

"""Getting random list of 5 names from the dictionary famous_people
By default random.sample gets keys from the dictionary, so no need to use famous_people.keys()"""
# Тестовое рабочее задание


def victory_game():
    random_people = random.sample(sorted(famous_people), 5)

    wrong = 0  # счетчик ошибок/wrong answers counter
    correct = 0  # счетчик верных ответов/correct answers counter
    keep_playing = True  # Flag for the while loop to continue the game or not

    while keep_playing:
        while (wrong + correct) < len(random_people):
            # Looping through the list of random_people
            for person in random_people:
                print(f"Какая дата рождения у {person}?")
                answer = input("Ваш ответ (в формате dd.mm.yyyy): ")
                # Getting the person's birth date from the dictionary
                # using the person's name as a key
                # and saving into 3 variables
                day, month, year = famous_people[person].split('.')

                if famous_people[person] == answer:
                    correct += 1
                    print("Верный ответ")
                else:
                    wrong += 1
                    print("Вы ошиблись")
                    print(f"Верный ответ: {days[day]} {months[month]} {year}")

            # Функции вынесены в файл utils.py
            display_statistics(wrong, correct)
            keep_playing = play_again()

            if keep_playing:
                wrong = 0
                correct = 0
