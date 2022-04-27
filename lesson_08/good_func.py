from random import randint

ROWS = 11


def gen_list():
    """
    Генератор списка

    :return: List
    """
    lst = [randint(10, 99) for _ in range(20)]

    return lst


def sum_elements(my_list):
    return sum(my_list)


def print_list(my_list):
    print(' - '.join(str(el) for el in my_list))


list_int = gen_list()
s = sum_elements(list_int)
print_list(list_int)
print(list_int, s)


def print_square():
    for _ in range(ROWS):
        for _ in range(ROWS):
            print('*  ', end='')
        print()
    print()


print_square()


def change_row():
    global ROWS
    ROWS = 12
    print(ROWS)


print(ROWS)
change_row()
print(ROWS)
