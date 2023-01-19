password = str(input('Enter your password: '))

passdict = {
    'i' : '1',
    'a' : '@',
    'm' : 'M',
    'B' : '8',
    's' : '$',
}

for key, value in passdict.items():
    password = password.replace(key, value)
print(f'{password}!')