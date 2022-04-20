d = {'key1': 'value1', 'key2': 'value2'}
print(type(d), d)
d = {}
print(type(d), d)
d = dict()
print(type(d), d)

d = dict(
    [
        ('key1', 'value1'), ('key2', 'value2')
    ]
)
print(type(d), d)

d = dict(
    key1='value1',
    key2='value2',
    key3='value3',
    key4=45,
    key5=True,
    key6=4.5
)
print(type(d), d)
print(d['key4'])

d = {110: 'value', 145: 4.8, 225: False, 3: 0.1, 4: 34}
# print(d[0])

person = {}
print(person)
person['name'] = 'Petro'
print(person)
person['name'] = 'Bob'
print(person)
person[56] = True
print(person)
person[3] = None
print(person)
person['pets'] = {'Fido': 'dog', 'Sox': 'cat'}
person['children'] = ['Ralph', 'Bob', 'Betty']
print(person)
print(person['children'][1])
print(person['pets']['Fido'])
person[(1, 2, 3)] = 90
print(person)

# len(dict)
print(len(person))

# dict.clear()
# person.clear()
# print(person)

print(person['name'])
# dict.get(key, default_value)
print(person.get('name', 'Petro'))

# dict.keys()
# dict.values()
# dict.items()
print(list(person.keys()))
print(list(person.values()))
print(list(person.items()))
for key in person.keys():
    print(key, end='\t')
print()

for value in person.values():
    print(value, end='\t')
print()

for item in person.items():
    print(item, end='\t')
print()

for key, value in person.items():
    print(key, value)
print()

# dick.pop(key)
print(person.pop('name'))
print(person)

# dict.popitem()
print(person.popitem())
print(person)

# dict1.update(dict2)
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'e': 100, 'c': 200, 'd': 300}
print(d1)
print(d2)
d1.update(d2)
print(d1)
print(d2)

# fromkeys(list)
lst = [1, 2, 3, 4]
d = dict.fromkeys(lst)
print(d)
