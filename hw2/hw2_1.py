import random
coins = int(input("Введите количество монеток на столе: "))
side = 0
reshka_count = 0
gerb_count = 0
for i in range(coins):
    side = random.randint(0, 1)
    if side==1:
         print("Решка", end=" ")
    else:
         print("Герб", end= " ")
    if side==1:
        reshka_count+=1
gerb_count = coins-reshka_count
if gerb_count<reshka_count:
        print(f"\nПеревернуть нужно будет {gerb_count} раз(а)")
else:
    print(f"\nПеревернуть нужно будет {reshka_count} раз(а)")