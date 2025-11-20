rows = 4
cols = 3

array1 = []
array2 = []
array3 = []

for i in range(rows):
    row = []
    for j in range(cols):
        num = int(input(f'Введите элемент [{i}] [{j}]: '))
        row.append(num)
    array1.append(row)

for i in range(rows):
    a = []
    for j in range(cols):
        num = int(input(f'Введите элемент [{i}] [{j}]: '))
        row.append(num)
    array1.append(row)

for i in range(rows):
    a = []
    for j in range(cols):
        max_num = max(array1[i][j], array2[i][j])
        row.append(max_num)
    array3.append(row)

for row in array1:
    print(row)

for row in array2:
    print(row)

for row in array3:
    print(row)



