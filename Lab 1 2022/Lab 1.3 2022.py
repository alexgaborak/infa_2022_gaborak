a = [str(i) for i in input().split()]

b = []
for i in range(len(a)):
    x = len(a[i])
    b.append(x)

print(min(b), max(b))

