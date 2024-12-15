n=int(input())
k=1
sch=0
kv=0
for i in range(n):
    kv=k**2
    sch+=kv
    k+=1
print(sch)

