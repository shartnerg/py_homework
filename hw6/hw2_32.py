min_range = int(input('Введите минимум диапазона: '))
max_range = int(input('Введите максимум диапазона: '))
user_number = int(input("Введите число: "))
my_list = []
my_list = list(range(min_range, max_range + 1))
print(my_list)
for index, value in enumerate(my_list):
        if value==user_number:
            print("Индекс элемента", user_number, ":", index)

