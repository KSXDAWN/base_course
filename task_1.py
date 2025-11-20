def f(my_func):
    sum_alimenti = 0
    for alimenti in my_func:
        sum_alimenti += alimenti
    return sum_alimenti / len(my_func)

A = [1, 2 , 4, 5, 6, 7, 8]
result = f(A)
print(f'Среднее арифметическое: {result}')