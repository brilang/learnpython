from datetime import datetime, timedelta

current_time = datetime.now()
print('Today is: ' + str(current_time))

one_day = timedelta(days=1)
tomorrow = current_time + one_day
print('Tomorrow is: ' + str(tomorrow))

print(f'Year: {current_time.year}')
print(f'Month: {current_time.month}')
print(f'Day: {current_time.day}')

birthday = input('Enter your birthday (YYYY-MM-DD): ')
birthday_date = datetime.strptime(birthday, '%Y-%m-%d')
print(f'Your birthday is: {birthday_date}')