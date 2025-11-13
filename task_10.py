import math
N = int(input('N = '))
M = int(input('M = '))

trigonometry_array = []

for i in range(N):
    A = []
    for j in range(M):
        k = math.sin(N * i + M * j + 1)
        if k < 0:
            A.append(0)
        else:
            A.append(k)
    trigonometry_array.append(A)
print('Тригонометрический массив: ')
for A in trigonometry_array:
    print(A)
    
