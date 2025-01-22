from random import shuffle


def set_order():
    participants = input("Список участников: ").split()
    shuffle(participants)
    for i in range(len(participants)):
        print(i + 1, "-", participants[i])


if __name__ == "__main__":
    set_order()

