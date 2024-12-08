a=int(input())
mi=a
ma=a
k=0
while a!=0:
    if 99<a<1000 and a%100==11:
        k+=1
        if a<mi:
            mi=a
        if a>ma:
            ma=a
    a=int(input())
if 99>mi<1000 or mi%100!=11:
    mi=ma
if 99>ma<1000 or ma%100!=11:
    ma=mi
if k!=0:
    print('Минимальное:', mi)
    print('Максимальное:', ma)
else:
    print('Нет')