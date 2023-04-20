a= int(input("Vvedite trehznachnoe chislo: "))
if a/100>=1 and a/100<10:
    print(int(a/100+((a/10)%10)+a%10))
else:
    print("Eto ne trehznachnoe chislo")