x=int(input())
summa=0
krf=0
while x!=0:
    summa+=x
    if abs(x)%5==0 and abs(x)%2==0:
        krf+=1
    x=int(input())
print(summa)
print(krf)