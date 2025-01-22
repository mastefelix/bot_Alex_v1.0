from random import randint


def easy_level(win_number):
    user_number = int(input("Число: "))
    count = 1
    while win_number != user_number:
        if win_number > user_number:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
        count += 1
        user_number = int(input("Число: "))
    print(f"Ура!!! Ты отгадал с {count} попытки.")


def medium_level(win_number):
    for i in range(1, 4):
        user_number = int(input("Число: "))
        if win_number == user_number:
            print(f"Ура!!! Ты отгадал с {i} попытки.")
            break
        elif win_number > user_number:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
    else:
        print("Повезет в другой раз!")


def hard_level(win_number):
    user_number = int(input("Число: "))
    count = 1
    while win_number != user_number:
        print("Неверно!")
        count += 1
        user_number = int(input("Число: "))
    print(f"Ура!!! Ты отгадал с {count} попытки.")


def super_hard_level(win_number):
    for i in range(1, 4):
        user_number = int(input("Число: "))
        if win_number == user_number:
            print(f"Ура!!! Ты отгадал с {i} попытки.")
            break
        print("Неверно!")
    else:
        print("Повезет в другой раз!")

def guess_number():
    print("""Добро пожаловать в игру угадай число. Необходимо отгадать число от 1 до 10.
Выбери уровень сложности:
1 - легкий - неограниченное количество попыток с подказками
2 - средний - три попытки с подсказками
3 - сложный - неограниченное количество попыток без подсказок
4 - супер сложный - три попытки без подсказок
0 - выход""")
    level = input("Уровень сложности: ")
    while level != "0":
        win_number = randint(1, 10)

        if level == "1":
            easy_level(win_number)
        elif level == "2":
            medium_level(win_number)
        elif level == "3":
            hard_level(win_number)
        elif level == "4":
            super_hard_level(win_number)
        else:
            print("Неверный выбор!")
        level = input("Уровень сложности: ")


if __name__ == "__main__":
    guess_number()
