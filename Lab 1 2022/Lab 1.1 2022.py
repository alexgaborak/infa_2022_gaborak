a = [int(i) for i in input().split()]
x = int(a[0])
y = int(a[1])
r = int(a[2])

if x**2 + y**2 <= r**2:
    print("YES")
else:
    print("NO")
