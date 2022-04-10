"""
while <condition>:
    operator1
    operator2
    operator3
    ...
    operatorN
operatorM
"""

# bool -> True, False
# 0, 0.0, '', "", [], (), {} - False

i = 1
# print(i**2)
# i += 1
# print(i**2)
# i += 1
# print(i**2)
# i += 1
# print(i**2)
# i += 1

# while i <= 10:
#     print(i ** 2)
#     i += 1

# num = int(input('Please enter a number: '))
# cnt = 0
# while num != 0:
#     # x = num % 10
#     cnt += 1
#     num //= 10
# print('length: ' + str(cnt))

# num = int(input('Please enter a number: '))
# cnt = 0
# while True:
#     cnt += 1
#     num //= 10
#     if num == 0:
#         break
#
# print('length: ' + str(cnt))

# num = int(input('Please enter a number: '))
# while num != 0:
#     x = num % 10
#     num //= 10
#     if x % 2 != 0:
#         continue
#     print(x)

# else
i = 1
while i < 10:
    print(i, end=' ')
    i += 1
else:
    print('else')

i = 1
while i < 10:
    print(i, end=' ')
    i += 1
    if i == 5:
        break
else:
    print('else')





