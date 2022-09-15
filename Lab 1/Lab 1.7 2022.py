a = [str(i) for i in input().split()]
result = []
for i in range(len(a)):
    if len(a[i]) > 3:
        result.append(a[i] + " ")
    else:
        result.append(" ")

print(*result, sep='')
