s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение: "))

x = 1
y = s - x

while x*y != p and x < s:
    x += 1
    y = s - x

if x*y == p:
    print(f"x = {x}, y = {y}")
else:
    print("Невозможно найти такие числа")
