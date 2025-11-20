array1 = [[0, 0], [0, 0]]
array2 = [[0, 0], [0, 0]]
array3 = [[0, 0], [0, 0]]
 
print('Заполним первый массив: ')

for i in range(2):
    for j in range(2):
        array1[i][j] = int(input(f'Числа для 1го массива [{i}][{j}]: '))

print('Заполним второй массив: ')
for i in range(2):
    for j in range(2):
        array2[i][j] = int(input(f'Числа для 2го массива [{i}][{j}]: '))

for i in range(2):
    for j in range(2):
        if array1[i][j] > array2[i][j]:
            array3[i][j] = array1[i][j]
        else:
            array3[i][j] = array2[i][j]

print('Первый массив: ', array1)
print('Второй массив: ', array2)
print('Третий массив: ', array3)

