stihotvorenie = input('Введите стихотворение: ')
print("Вы ввели:", stihotvorenie)

split_stihotvorenie = stihotvorenie.split()
list_of_stihotvorenie = [word.lower() for word in split_stihotvorenie]
glasnye_bukvy = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

counts = [sum(1 for letter in word if letter in glasnye_bukvy) for word in list_of_stihotvorenie]

if all(count == counts[0] for count in counts):
    print("Парам пам-пам")
else:
    print("Пам парам")

