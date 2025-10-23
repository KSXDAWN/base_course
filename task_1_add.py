import math

print("ax^2 + bx + c = 0:")

a = int(input('Введите коэффициент а: '))

b = int(input('Введите коэффициент b: '))

c = int(input('Введите коэффициент c: '))

D = b ** 2 - 4 * a * c
print('Дискриминант равен: ')

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("Корней нет")