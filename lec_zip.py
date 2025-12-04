names = ['John', 'Pork', 'Maria', 'Richard']
ages = [12, 1234, 15, 45]
isTeenager = [True, False, True, False]

users = list(zip(names, ages, isTeenager))
print(users)

print('User ages: ', dict(zip(names, ages)))