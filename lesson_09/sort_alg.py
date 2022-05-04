from random import randint


def bubble_sort(lst):
    cnt = 0
    for i in range(len(lst)-1):
        flag = True
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                flag = False
        cnt += 1
        if flag:
            break
    print(cnt)


def insertion_sort(lst):
    for i in range(len(lst)):
        tmp = lst[i]
        for j in range(i-1, -1, -1):
            if tmp >= lst[j]:
                break

            lst[j+1], lst[j] = lst[j], lst[j+1]

#                       i
#                      tmp
# [30, 72, 80, 81, 83, 77, 69]
#                   j


l1 = [randint(10, 99) for _ in range(25)]
l2 = l1.copy()
# l1 = [17, 22, 23, 24, 24, 27, 27, 31, 43, 42, 44, 48, 50, 50, 58, 59, 61, 62, 75, 79, 79, 87, 88, 90, 99]
print(l1)
bubble_sort(l1)
print(l1)

print(l2)
insertion_sort(l2)
print(l2)

#   [50, 51, 52, 52, 99, 58, 83, 49]
#             b  a      неустойчивый
#             a  b      устойчивый
