# price = input('How much did you pay? ')
# price = float(price)
# if price >= 1.00:
#     tax = 0.07
# else:
#     tax = 0
# print (f'Tax rate is: {tax}')

# country = input('What country are you from? ')
# if country.lower() == 'canada':
#     print('You must like hockey!')
# else:
#     print('You are not from Canada.')

country = input('What country do you live in? ')
tax = 0.0

if country.lower() == 'canada':
    province = input('What province do you live in? ')
    province = province.lower()
    if province == 'alberta':
        tax = 0.05
    elif province == 'british columbia':
        tax = 0.12
    elif province == 'manitoba':
        tax = 0.13
    # elif province == 'new brunswick' or province == 'newfoundland and labrador' or province == 'nova scotia' or province == 'prince edward island':
    elif province in ('new brunswick', 'newfoundland and labrador', 'nova scotia', 'prince edward island'):
        tax = 0.15
    elif province == 'ontario':
        tax = 0.13
    elif province == 'quebec':
        tax = 0.14975
    elif province == 'saskatchewan':
        tax = 0.11

print(f'Tax rate is: {tax}')