a, b = input().split()
a = int(a)
b= b[::-1]

total = 0
for i, num in enumerate(b):
    print(a * int(num))
    total += a * int(num) * (10**i)
print(total)