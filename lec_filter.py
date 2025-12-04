names = ['John', 'Pork', 'Maria', 'Richard']
ages = [12, 1234, 15, 45]

def checker(user):
    name, age = user
    return age > 21


users = list(zip(names, ages))
canDrinkAlcohol = list(filter(checker, users))
print(canDrinkAlcohol)