from random import randint

# line search
lst = [randint(10, 99) for _ in range(25)]
print(lst)
key = int(input('Please enter a value: '))

for el in lst:
    if el == key:
        print('Yes')
        break
else:
    print('No')


# binary search
def binary_search(ar, key_value, left=0, right=None):
    if right is None:
        right = len(ar)

    middle = (left + right) // 2
    while ar[middle] != key_value and left <= right:
        if ar[middle] < key_value:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    return (True, middle) if not (left > right) else (False, middle+1)


lst.sort()
print(lst)
res = binary_search(lst, key)
if not res[0]:
    print('Key not found')
    lst.insert(res[1], key)
    print(lst)
else:
    print(f'Found value {key} - index {res[1]}')
