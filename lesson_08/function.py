from random import randint

# lst = [randint(10, 99) for _ in range(20)]
#
# for element in lst:
#     print(f"[{element}] + ", end='')
# print()
#
# lst1 = [el ** 2 for el in lst]
#
# for element in lst1:
#     print(f"[{element}] + ", end='')
# print()
#
# lst2 = [el // 3 for el in lst1]
#
# for element in lst2:
#     print(f"[{element}] + ", end='')
# print()

"""
def function_name(param1, param2, param3):
    operator1
    operator2

    return param        # None
"""

r = print()
print(r)


def print_list(my_list):
    for element in my_list:
        print(f"[{element}] * ", end='')
    print()


lst = [randint(10, 99) for _ in range(20)]

print_list(lst)

lst1 = [el ** 2 for el in lst]

print_list(lst1)

lst2 = [el // 3 for el in lst1]

print_list(lst2)


def func1():
    print('Hello World!')


def my_sum(my_list):
    res = 0
    for element in my_list:
        res += element

    return res


result = my_sum(lst)
print(result)


def multi_calculation(my_list):
    sum_of_elements = 0
    multi_of_elements = 1
    pow_of_elements = 0
    for element in my_list:
        sum_of_elements += element
        multi_of_elements *= element
        pow_of_elements += element ** 2

    return sum_of_elements, multi_of_elements, pow_of_elements


result = multi_calculation(lst)
print(type(result), result)
a, b, c = multi_calculation(lst)
print(a, b, c)
