x = int(input("Введите год: "))

if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print(f"Год {x} — високосный.")
else:
    print(f"Год {x} — не високосный.")