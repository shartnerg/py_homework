n= int(input("Vvedite dlinu shokolandi (skolko dolek): "))
m= int(input("Vvedite shirinu shokolandi (skolko dolek): "))
k= int(input("Skolko dolek vy hotite otlomit'?: "))
if k%n==0 or k%m==0:
    print("yes")
else:
    print("no")