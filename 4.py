k=0
min_value = float('inf')
max_value = float('-inf')

while True:
    num = int(input())

    if num == 0:
        break

    if num % 7 != 0:
        k=0
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

if k==0:
    print(f"Минимум: {min_value}, Максимум: {max_value}")
else:
    print("нет")