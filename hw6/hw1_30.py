first_item = int(input('Введите первый элемент прогрессии: '))
difference = int(input('Введите разность прогрессии: '))
size = int(input('Введите размер прогрессии: '))
n=first_item
my_list = []
my_list.append(n)
while n!=size:
    n=n+difference
    my_list.append(n)
print(my_list)
