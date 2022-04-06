"""
if <condition>:
    operator1
    operator2
"""

a = 6

if a < 5:
    print('a < 5')
print('end')

"""
if <condition>:
    operator1
else:
    operator2
"""
b = 4
c = 0
# b / c
if c == 0:
    print('c = 0')
else:
    print(b / c)
print('end')

"""
if <condition1>:
    operator1
elif <condition2>:
    operator2
elif <condition3>
    operator3
else:
    operator4
"""
x = 5
if x > 0:
    print('positive')
else:
    if x < 0:
        print('negative')
    else:
        print('zero')

if x > 0:
    print('positive')
elif x < 0:
    print('negative')
else:
    print('zero')

# q Є (1, 35)
q = -4
if q >= 1:
    if q <= 35:
        print('q in range(1, 35)')
    else:
        print('no')
else:
    print('no')

if q >= 1 and q <= 35:
    print('q in range(1, 35)')
else:
    print('no')

if 1 <= q <= 35:          # 1 <= q <= 35
    print('q in range(1, 35)')
else:
    print('no')

if q in range(1, 36):
    print('q in range(1, 35)')
else:
    print('no')
