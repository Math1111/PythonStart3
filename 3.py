a=int(input())
mi=a
chisl1=1
chisl2=1
chisl3=0
k=0
while a!=0:
    while chisl2 <= a:
        chisl3 = chisl2
        chisl2 = chisl1 + chisl2
        chisl1 = chisl3
        if a == chisl2:
            k+=1
            if a<mi:
                mi=a
    a=int(input())
if k!=0:
    print('Минимальное:', mi)
else:
    print('Нет')