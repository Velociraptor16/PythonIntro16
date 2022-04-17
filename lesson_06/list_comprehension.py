from random import randint

# lst = []
# for _ in range(20):
#     lst.append(randint(10, 99))
# print(lst)

# lst_s = []
# for el in lst:
#     lst_s.append(str(el))
# print(lst_s)

# list = [expression_1 expression_2 expression_3]

lst = [randint(10, 99) for _ in range(20)]
print(lst)

s = ' + '.join([str(el) for el in lst]) + ' = ' + str(sum(lst))
print(s)

x = 52
if x % 2 == 0:
    print('чет')
else:
    print('нечет')

s1 = 'чет' if x % 2 == 0 else 'нечет'
print('чет' if x % 2 == 0 else 'нечет')

lst_e = [el for el in lst if el % 2 != 0]
print(lst_e)
