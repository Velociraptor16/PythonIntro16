#              0   1   2   3   4
#              H   E   L   L   O
#             -5  -4  -3  -2  -1

s = '/PycharmProjects/PythonIntro16'
print(s[0])

for ch in s:
    print(ch, end=', ')
print()

for idx in range(len(s)):       # 0 - len(s)-1
    print(s[idx], end=' ')
print()

print(s[-30])

for idx in range(len(s)-1, -1, -1):       # 0 - len(s)-1
    print(s[idx], end='')
print()

for idx in range(-1, -(len(s)+1), -1):    # 0 - len(s)-1
    print(s[idx], end='')
print()


# str[start: stop: step]
# str[start: stop]          step = 1
# str[start:]               step = 1, stop = len(str)
# str[: stop]               step = 1, start = 0
# str[:: step]              start = 0, stop = len(str)
# str[: stop: step]         start = 0
# str[:]                    start = 0, stop = len(str), step = 1


s1 = 'PythonIntro16'
print(s1[6: 11])
print(s1[6:])
print(s1[: 6])
print(s1[:: 2])
print(s1[: 6: 2])
print(s1[:])
print(s1[::-1])

print(s1[6])
# s1[6] = 'T'
print(s1[6: 3948674938653498567394])
print(s1[-3825638496329463946: 6])

s2 = 'Process finishced with exit cede 0'
# len(str)
print(len(s2))

# str.find(sub_string, start, stop)
# str.rfind(sub_string, start, stop)
print(s2.find('i'))
print(s2.find('i', 10))
print(s2.find('i', 12))
print(s2.find('i', 19))
print(s2.find('i', 25))

# str.replace(old, new, count)
print(s2.replace('ce', 'DB8645369'))

# str.count(sub_string, start, stop)
print(s2.count('ce'))

# str.capitalize()
s3 = 'proceSs fiNIshced with EXit cEde 0'
print(s3.capitalize())

# str.title()
print(s3.title())

# str.lower()
# str.upper()
print(s3.lower())
print(s3.upper())

# str.strip(sub_string)
# str.rstrip(sub_string)
# str.lstrip(sub_string)
s4 = '      finished            '
s5 = 'rtrtrtfinishedhghghghg'
print("'" + s4 + "'")
print("'" + s4.strip() + "'")

print("'" + s5 + "'")
print("'" + s5.strip('rthg') + "'")
s6 = '     process finishced with exit cede 0           '
print("'" + s6 + "'")
print("'" + s6.strip() + "'")

# str.split(sub_string)
s7 = 'Process finished with exit code 0'
print(s7.split())
print(s7.split('i'))

# 'sub_string'.join(list)
