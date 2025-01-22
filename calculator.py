def add(num_1, num_2):
    """Сложение (+)"""
    return f"{num_1} + {num_2} = {num_1 + num_2}"


def sub(num_1, num_2):
    """Вычитание (-)"""

    return f"{num_1} - {num_2} = {num_1 - num_2}"


def mul(num_1, num_2):
    """Умножение (*)"""
    return f"{num_1} * {num_2} = {num_1 * num_2}"


def div(num_1, num_2):
    """Деление (/)"""
    if num_2 == 0:  # Проверка деления на ноль
        return "На ноль делить нельзя!"
    else:
        return f"{num_1} / {num_2} = {num_1 / num_2}"


def calculator():
    operation = input("+, -, *, / (0 - завершить): ")
    while operation != "0":
        num_1 = float(input("Первое число: "))
        num_2 = float(input("Второе число: "))
        if operation == "+":
            print(add(num_1, num_2))
        elif operation == "-":
            print(sub(num_1, num_2))
        elif operation == "*":
            print(mul(num_1, num_2))
        elif operation == "/":
            print(div(num_1, num_2))
        else:
            print("Неизвестная операция")
        operation = input("+, -, *, / (0 - завершить): ")


if __name__ == "__main__":
    calculator()
