a = int(input())
b = int(input())
 
print(f"{a}{' не' if a % b != 0 else ''} делится на {b}")
print(f"Частное: {a // b}{f', остаток: {a % b}' if a % b != 0 else ''}")
