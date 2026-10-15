from array import array

names = ['Brian', 'Alice', 'Jorge', 'Lisa']
scores = []
scores.append(90)
names.insert(0, 'Brad')
print (names)
print(names[1])
print(f'Names count: {len(names)}')
presenters = names[1:3]
print(f'Presenters: {presenters}')

scores = array('d')
scores.append(97)
scores.append(98)
print(scores)

person = {'name': 'Brian', 'age': 55, 'city': 'Abbotsford'}
person['gender'] = 'male'
print(person)
print (f'Name: {person["name"]}')