a=int(input())
mi=1000
ma=99
k=0
while a!=0:
    if 99<a<1000 and a%100==11:
        k+=1
        if a<mi:
            mi=a
        if a>ma:
            ma=a
    a=int(input())
if k!=0:
    print('Минимальное:', mi)
    print('Максимальное:', ma)
else:
    print('Нет')