n=int(input())
k=1
sch=0
for i in range(n):
    if k%2==0:
        sch+=k
    k+=1
print(sch)