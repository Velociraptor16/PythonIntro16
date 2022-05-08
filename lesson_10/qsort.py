from random import randint


def qsort(ar, first_idx, last_idx):
    if first_idx >= last_idx:
        return

    i, j = first_idx, last_idx
    middle = ar[(first_idx + last_idx) // 2]
    while i <= j:
        while ar[i] < middle:
            i += 1
        while ar[j] > middle:
            j -= 1

        if i <= j:
            ar[i], ar[j] = ar[j], ar[i]
            i, j = i + 1, j - 1

    qsort(ar, first_idx, j)
    qsort(ar, i, last_idx)


lst = [randint(10, 99) for _ in range(45)]
print(lst)
qsort(lst, 0, len(lst)-1)
print(lst)
