def sum(a, b):
    if b==0:
        return a
    if a==0:
        return b
    else:
        return a+sum(1, b-1)
    



a = int(input('Введите число a: '))
b = int(input('Введите чисто b: '))

result = sum(a, b)
print(f'Результат: {result}')