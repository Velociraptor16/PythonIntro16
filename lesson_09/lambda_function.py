from random import randint


def func():
    pass


# lambda param1, param2, param3: expression
# a = lambda x, y: x + y
# a(4, 6)
# b = (lambda x, y: x + y)(5, 7)


a = lambda x, y: x + y
print(type(a), a)
print(a(4, 5))

b = (lambda x, y: x + y)(5, 7)
print(type(b), b)

# map, filter
# map(func, iterable_obj)

temp = [23, 56.8, 102.45, 91, 2, -9]


# def far(tmp):
#     return round(((9.0 / 5) * tmp) + 32, 2)


# def cles(tmp):
#     return round((5.0 / 9) * (tmp - 32), 2)


# lst = []
# for t in temp:
#     lst.append(far(t))
# print(lst)

# lst1 = list(map(far, temp))
# print(lst1)
# lst2 = list(map(cles, lst1))
# print(lst2)

lst3 = list(map(lambda tmp: round(((9.0 / 5) * tmp) + 32, 2), temp))
print(lst3)
lst4 = list(map(lambda tmp: round((5.0 / 9) * (tmp - 32), 2), lst3))
print(lst4)

lst0 = [randint(10, 99) for _ in range(10)]
lst1 = [randint(10, 99) for _ in range(12)]
lst2 = [randint(10, 99) for _ in range(11)]

print(len(lst0), len(lst1), len(lst2))

lst5 = list(map(lambda a, b, c: (a + b) * c, lst0, lst1, lst2))
print(lst5)

# filter(func, iterable_obj)
lst6 = [randint(10, 99) for _ in range(25)]
print(lst6)

lst7 = []
for el in lst6:
    if el % 2 != 0:
        lst7.append(el)
print(lst7)

lst8 = tuple(filter(lambda q: not q % 2, lst6))
print(lst8, type(lst8))

# zip(iter1, iter2, ... iterN)

lst9 = [randint(10, 99) for _ in range(15)]
lst10 = [randint(10, 99) for _ in range(18)]
lst11 = [randint(10, 99) for _ in range(20)]

z1 = tuple(zip(lst9, lst10, lst11))
print(type(z1), z1)

