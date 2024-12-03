a=int(input())
b1=a//500
b2=a%500//100
b3=a%100//50
b4=a%50//10
print("Следует сдать: ")
print(b1, "купюр по 500")
print(b2, "купюр по 100")
print(b3, "купюр по 50")
print(b4, "купюр по 10")

c1=int(input())
c2=int(input())
c3=int(input())
proverka=(c1!=c2) and (c3!=c1) and (c2!=c3)
print(proverka)