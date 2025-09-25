s = input("Enter a string: ")
s1 = list(s)
l = len(s1)
for i in range(0, l - 1):
    pos = i
    small = s1[i]
    for j in range(i + 1, l):
        if (s1[j] < small):
            pos = j
            small = s1[j]
    s1[pos] = s1[i]
    s1[i] = small

for i in s1:
    print(i, end="")



