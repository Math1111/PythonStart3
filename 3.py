n=int(input())
s=0
for i in range(n):
    x=int(input())
    if x%3==0 and x%10==2:
        s+=1
print(s)