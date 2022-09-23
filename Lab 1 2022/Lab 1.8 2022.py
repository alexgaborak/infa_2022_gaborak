given = [int(i) for i in input().split()]
length = given[0]
shift = given[1]
arr = [int(i) for i in input().split()]
result = []
for i in range(len(arr)):
    realindex = -length + i + shift
    while realindex >= len(arr):
        realindex -= length
    result.append(arr[realindex])

print(*result)
