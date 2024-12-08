a=int(input())
mi=a
ma=a
k=0
while a!=0:
    if a%7!=0:
        k+=1
        if a<mi:
            mi=a
        if a>ma:
            ma=a
    a=int(input())
if mi%7==0:
    mi=ma
if ma%7==0:
    ma=mi
if k!=0:
    print('Минимальное:', mi)
    print('Максимальное:', ma)
else:
    print('Нет')