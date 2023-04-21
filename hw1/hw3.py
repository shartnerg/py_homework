n= int(input("Vvedite nomer bileta (6 cifr): "))
if n/100000>=1 and n/100000<10:
    a=n//1000
    a=a//100+((a//10)%10)+a%10
    b=n%1000
    b=b//100+((b//10)%10)+b%10
    if a==b:
        print("yes")
    else:
        print("no")
else:
    print("Error, bilet dolzhen sostoyat iz 6 cifr")
