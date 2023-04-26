CHISLO = 2
n = int(input('Введите предел: '))
stepen = 0
while CHISLO**stepen<=n:
    s=CHISLO**stepen
    print(s, end=" ")
    stepen+=1
