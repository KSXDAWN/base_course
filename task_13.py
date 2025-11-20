m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

array = []

print("Введите элементы массива:")
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input(f"Введите элемент [{i+1}][{j+1}]: ")))
    array.append(row)

max_elements = [0] * n

for j in range(n):
    max = array[0][j]
    for i in range(1, m):
        if array[i][j] > max:
            max = array[i][j]
    max_elements[j] = max

print("Максимальные элементы каждого столбца:")
print(max_elements)