from copy import deepcopy

lst = []
print(type(lst), lst)
lst = list()
print(type(lst), lst)
lst = list('Process finished with exit code 0')
print(type(lst), lst)
lst = [1, 2, 3, 4]
print(type(lst), lst)
lst = [1, 'Test', True, [6, 'y'], 4.5]
print(type(lst), lst)

print(lst[1])
lst[1] = 123
print(type(lst), lst)
print(lst[3][1])

print(lst[1: 4])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

print(l1 * 3)
print([0] * 10)

lst = list('Process finished with exit code 0')
# len(list)
print(len(lst))

# A in list
# A not in list
print('i' in lst)
print('M' in lst)
print('i' not in lst)
print('M' not in lst)

if 'i' in lst:
    print('exists')
else:
    print('not exists')

# min(list)
# max(list)
# sum(list)

lst = [3, 5, 2, 7, -3, 9, -5, 0.3, 5, 2.456, 1, 4, 6, 3]
print(min(lst))
print(max(lst))
print(sum(lst))

s = 'Process finished with exit code 0'
print(min(s))
print(max(s))
# print(sum(s))

# list.index(value, start, stop)
print(lst.index(-5))
# print(lst.index(22))

# list.count(value)
print(lst.count(3))
print(lst.count(30))

# list.append(value)
lst.append(456)
print(lst)

# list.pop()
x = lst.pop()
print(x)
print(lst)

# list.pop(index)
x = lst.pop(5)
print(x)
print(lst)

# list.insert(index, value)
lst.insert(5, 88)
print(lst)

# list.clear()
# lst.clear()
print(lst)

# [1, 2, 3, 4, 5, 6] = [1, 2, 3] + [4, 5, 6]
# list.extend(list2)
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)
print(l2)

# list.remove(value)
l1.remove(4)
print(l1)

# del list[index]
del l1[2]
print(l1)
# del l1

# list.revers()
l1.reverse()
print(l1)
print(l1[:: -1])
print(l1)

# split(), join()
s = 'Process finished with exit code 0'
lst = s.split()
print(lst)
s1 = ' -> '.join(lst)
print(s1)

lst1 = [1, 2, 3, 4]
print(lst1)
lst2 = lst1
print(lst2)
lst1[2] = 88
print(lst1)
print(lst2)
print(id(lst1), id(lst2))

lst3 = lst1.copy()
print(lst3)
lst1[3] = 99
print(lst1, lst2, lst3)
print(id(lst1), id(lst3))

lst4 = [[1, 2, 3], 4, 5, 6]
lst5 = lst4.copy()
print(lst4)
print(lst5)
print(id(lst4), id(lst5))

lst4[2] = 55
print(lst4)
print(lst5)
lst4[0][1] = 88
print(lst4)
print(lst5)
print(id(lst4[0]), id(lst5[0]))

lst6 = deepcopy(lst4)
print(id(lst4), id(lst6))
print(id(lst4[0]), id(lst6[0]))
lst4[0][2] = 99
print(lst4)
print(lst6)
