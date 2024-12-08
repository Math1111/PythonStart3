a=int(input())
mi=a
ma=a
while a!=0:
    if a<mi:
        mi=a
    if a>ma:
        ma=a
    a=int(input())
print('Минимальное:', mi)
print('Максимальное:', ma)