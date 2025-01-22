import calculator
import game
import keyboard_train
import calc_average
import order_list
import weather
import wiki
import translat


print("Привет! Я чат-бот Алекс! Добро пожаловать!")
menu = """Меню:
1 - калькулятор
2 - игра угадай число
3 - клавиатурный тренажер
4 - подсчет успеваемости
5 - определение порядка демонстрации проектов
6 - погода
7 - википедия
8 - переводчик
9 - меню
0 - завершить"""
print(menu)

choice = input("Номер действия: ")

while choice != "0":
    if choice == "1":
        calculator.calculator()
    elif choice == "2":
        game.guess_number()
    elif choice == "3":
        keyboard_train.keyboard_training()
    elif choice == "4":
        calc_average.calc_average(input("Имя: "))
    elif choice == "5":
        order_list.set_order()
    elif choice == "6":
        print(weather.get_weather(input("Город: ")))
    elif choice == "7":
        print(wiki.get_wiki(input("Статья: ")))
    elif choice == "8":
        print(translat.translate(input("Слово для перевода: ")))
    elif choice == "9":
        print(menu)
    else:
        print("Действие не найдено!")
    choice = input("Номер действия: ")

print("Хорошего дня! До скорых встреч!")
