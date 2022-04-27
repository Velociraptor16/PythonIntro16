def func(a, b):
    return a + b


print(func(3, 5))
print(func)

d = func
print(d(6, 7))


# s = {'werfew': 'ewtwerw'}
# list(s.keys())[0]


def dict_comp(a, b):
    if len(str(list(a.keys())[0])) == len(str(list(b.keys())[0])):
        return 0
    elif len(str(list(a.keys())[0])) > len(str(list(b.keys())[0])):
        return 1
    else:
        return -1


def comparator(my_list, comp_func):
    for i in range(len(my_list)-1):
        if comp_func(my_list[i], my_list[i+1]) == 0:
            print(f'{my_list[i]} == {my_list[i+1]}')
        elif comp_func(my_list[i], my_list[i+1]) == 1:
            print(f'{my_list[i]} > {my_list[i + 1]}')
        else:
            print(f'{my_list[i]} < {my_list[i + 1]}')


# lst = [2, 5, 3, 3, 4, 3, 3, 2, 1, 1]
# comparator(lst)
lst_dict = [{'type_12': 'lorry'}, {'model': 'IVECO'}, {'qwert': 3523}, {'length': 25.7}, {'weight': 8500.1}]
comparator(lst_dict, dict_comp)
