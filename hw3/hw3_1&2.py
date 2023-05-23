import random

size = int(input('Введите размер списка: '))
my_list = [random.randint(0,10) for _ in range(size)]
print(my_list)

num = int(input('Введите искомое число: '))
count = 0
closest = my_list[0]  
min_diff = abs(closest - num)

for item in range(len(my_list)):
    if num == my_list[item]:
        count += 1
    else:
        diff = abs(my_list[item]) - abs(num)
        if abs(diff) < abs(min_diff):
            closest = my_list[item]
            min_diff = diff

if count > 0:
    print(f"Количество вхождений числа {num}: {count}")
else:
    print(f"Ближайшее число к {num}: {closest}")