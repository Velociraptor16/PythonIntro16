s1 = 'PythonIntro16'
s2 = "Python\tIntro16\n"

# ASCII
# KOI-8R

# WIN-1251

code = 0x26bd
print(chr(code))
print(chr(9917))
print('\u26bd')     # \u - 2 bytes            \U - 4 bytes
print('\U0001f6a3')

print(ord('🚣'))
print(hex(ord('🚣')))

wave = '~'
boat = '\U0001F6A3'
seagull = '\u033C'
fish = '\U0001F41F'
penguin = '\U0001F427'
wale = '\U0001F40B'
octopus = '\U0001F419'

row = wave * 10 + boat + wave * 15 + '\n'
seagull_row = wave * 15 + seagull + wave * 12 + '\n'
fish_row = wave * 4 + fish + wave * 21 + '\n'
wale_row = wave * 10 + wale + wave * 15 + '\n'
penguin_row = wave * 7 + penguin + wave * 18 + '\n'
octopus_row = wave * 17 + octopus + wave * 8 + '\n'

sea = seagull_row + row + fish_row + wale_row + penguin_row + octopus_row
print(sea)

#              0   1   2   3   4
#              H   E   L   L   O
#             -5  -4  -3  -2  -1




















