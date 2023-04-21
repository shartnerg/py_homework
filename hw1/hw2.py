s= int(input("Vvedite obshee kolichestvo zhuravlikov(kratnoe 6): "))
if s>3 and s%3==0:
    k = int((s/3)*2)
    sp = int((s/3)/2)
    print(s, "->",sp, k, sp)
else:
    print("Chislo ne kratno 6")