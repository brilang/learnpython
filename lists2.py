brian = {}
brian['first'] = 'Brian'
brian['last'] = 'Lang'

alice = {}
alice['first'] = 'Alice'
alice['last'] = 'Smith'

people = []
people.append(brian)
people.append(alice)
people.append({'first': 'Jorge', 'last': 'Jones'})
people.append({'first': 'Lisa', 'last': 'Simpson'})
print(people)