array = []

for i in range(3):
    number = int(input(f'Число {i + 1}: '))
    array.append(number)
print(array)
 
new_number = int(input('Новое число: '))
position = int(input('Позиция (0-3): '))

array.insert(position, new_number)

print(array)