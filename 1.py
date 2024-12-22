n=int(input())
k=0
yn=0
for i in range(n):
    x=int(input())
    if x<5:
        k+=1
    if x==10:
        yn+=1
print(k)
if yn==0:
    print('NO')
else:
    print('YES')

