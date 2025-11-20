def my_func(a, b):
    x = 3 * a - b
    return x


# tmp = my_func()


def my_func(a = 1, b = 0):
    x = 3 * a - b
    return x


print(my_func())
print(my_func(3, 4))
print(my_func(3))
print(my_func(b=3))
print(my_func(b=3, a=9))


def my_func(a, b=0):
    x = 3 * a - b
    return x


	
# def my_func(a=0, b):
#     x = 3 * a - b
#     return x


# Оператор запаковки в кортеж
def my_func(*args):
    x = 3 * (args[0] - args[1]) / len(args)
    return x


print (my_func(3, 4))
print (my_func(3, 4, 8))


# Оператор запаковки в словарь
def my_func(**kwrgs):
    x = 3 * kwrgs['obj_1'] - kwrgs['obj_2']
    return x


print(my_func(obj_1=3, obj_2=4))
print(my_func(obj_1=3, obj_2=4, obj_3=8))


def final_func(a:float, b: int=1, c = 4, *arg, **kw):
    print(f'nuck figgers {a} + {b} + {c} - {arg} / {kw}')


final_func(1)
final_func(1, 4)
final_func(1, 4, 6)
final_func(1, 4, 6, 'fsdf', 4, 8)
final_func(1, f = 5, h = 'Good')
final_func('pdospfsdp')







