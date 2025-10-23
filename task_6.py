from random import randint
n = int(input('Введите размер таблицы: '))

A = []
m1 = 0
m2 = 9 ** 9
i1 = i2 = j1 = j2 = 0
for i in range(n):
    A.append([0]*n)
for i in range(n):
    for j in range(n):
        A[i][j] = randint(1, 100)
        if A[i][j] > m1:
            m1 = A[i][j]
            i1 = i; j1 = j
        if A[i][j] < m2:
            m2 = A[i][j]
            i2 = i; j2 = j
for i in A:
    print(*i)
