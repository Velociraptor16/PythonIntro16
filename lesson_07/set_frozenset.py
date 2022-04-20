from random import randint

# s = {}
# print(type(s), s)
s = set()
print(type(s), s)
s = set('Process finished with exit code 0')
print(s)

# len()
# s.clear()
s.add('er')
print(s)
s.discard('oW')
print(s)
# s.remove('oW')
# print(s)
# s = set()
value = s.pop()
print(value)
print(s)

# from random import randint
# import time
# s1 = set(randint(10, 99) for _ in range(20))
# time.sleep(5)
# s2 = set(randint(10, 99) for _ in range(20))

s1 = {13, 25, 33, 34, 41, 48, 50, 52, 61, 62, 70, 74, 76, 86, 93, 94, 95, 96, 97}
s2 = {10, 16, 21, 22, 23, 25, 27, 34, 43, 48, 54, 56, 70, 72, 75, 81, 87, 90, 98}
print(s1, 'len =', len(s1))
print(s2, 'len =', len(s2))
# A | B                 A.union(B)
# A |= B                A.update(B)
s3 = s1 | s2
print(s3, 'len =', len(s3))

# A & B                 A.intersection(B)
# A &= B                A.intersection_update(B)
s3 = s1 & s2
print(s3)

# A - B                 A.difference(B)
# A -= B                A.difference_update(b)
s3 = s1 - s2
print(s3)

# A ^ B                 A.symmetric_difference(B)
# A ^= B                A.symmetric_difference_update(B)
s3 = s1 ^ s2
print(s3)

s4 = s1 - s2
s5 = s2 - s1
s6 = s4 | s5
print(s6)
l1 = list(s3)
l1.sort()
l2 = list(s6)
l2.sort()
print(l1)
print(l2)

print('-' * 160)
lst = [randint(10, 20) for _ in range(30)]
print(lst)

lst1 = []
for value in lst:
    if value not in lst1:
        lst1.append(value)
print(lst1)

lst2 = list(set(lst))
print(lst2)

for element in s3:
    print(element, end=' ')
print()

fs = frozenset()
print(type(fs), fs)
fs = frozenset('Process finished with exit code 0')
print(fs)
