s = str(input())
big = 0
small = 0
for i in range(len(s)):
    if 64 < ord(s[i]) < 91:
        big += 1
    elif 96 < ord(s[i]) < 123:
        small += 1

print(big, small)
