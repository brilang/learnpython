from datetime import datetime
def printTime(task = ''):
    now = datetime.now()
    if task:
        print(f'{now} ← {task}')
    else:
        print(now)
    # print(now.strftime("%Y-%m-%d %H:%M:%S"))
def getInitial(name, forceUppercase = True):
    if forceUppercase:
        return name[0:1].upper()
    else:
        return name[0:1]

printTime()

name = 'Brian'
printTime('Name Assigned')

for x in range (0, 100):
    print (x)

printTime('Loop complete')

firstname = input('Enter your first name: ')
middlename = input('Enter your middle name: ')
lastname = input('Enter your last name: ')

print(f'Your initials are: {getInitial(firstname)}{getInitial(middlename)}{getInitial(lastname)}')
printTime('Initials printed')