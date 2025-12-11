import time


for i in range(10):
    print(f'i: {i}')
    time.sleep(1)
    for j in range(10):
        print(f'\t j: {j}')
        time.sleep(1)