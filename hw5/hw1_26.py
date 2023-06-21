def vozvedenie(a, b):
    if b==0:
        return 1
    else:
        return a*vozvedenie(a, b-1)
    

a = int(input('Введите число: '))
b = int(input('Введите степень: '))

result = vozvedenie(a, b)
print(f'Результат: {result}')