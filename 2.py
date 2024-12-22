n=int(input())
mi=30000
for i in range(n):
    x=int(input())
    if x%10==4 and x<mi:
        mi=x
print(mi)