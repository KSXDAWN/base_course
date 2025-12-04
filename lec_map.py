def is_devide_by_three(a):
    print(a%3 == 0)

nums = [25, 52, 64, 86, -41]
result = list(map(is_devide_by_three, nums))
print(result)


def my_func(a, b):
    return a * b

num1 = [4, 76, 64, 23, 30]
num2 = [1, 2, 3, 534, 19]

nums_multiply = list(map(my_func, num1, num2))
print(nums_multiply)