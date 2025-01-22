def calc_average(name):
    amount = 0
    total = 0
    grade = int(input("Оценка (0 - стоп): "))
    while grade != 0:
        amount += 1
        total += grade
        grade = int(input("Оценка (0 - стоп):"))
    average = total / amount
    print(f"{name} - средний балл: {average}")
    # return average

if __name__ == "__main__":
    name = input("Имя: ")
    calc_average(name)

