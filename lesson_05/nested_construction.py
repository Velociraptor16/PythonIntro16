rows = 11
cols = 11

for i in range(rows):           # 10
    print(i, end='\t')
    for _ in range(cols):       # 6
        print('*  ', end='')
    print()
print()

print('\t0  1  2  3  4  5  6  7  8  9 10')
for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if i == 0 or j == 0 or i == rows-1 or j == cols-1 or i == j or i == cols-1-j or rows // 2 == i or cols // 2 == j:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()
