n = input("Enter a number: ")
flag = int(1)
length = len(n)
max = n[int((length - 1) / 2)]
for i in range(0, length):
    if (n[i] != n[length - i - 1]):
        flag = 0
        break
    if (max < n[i]):
        flag = 0
        break

if (flag):
    print(n + " is a Hill number")
else:
    print(n + " is not a Hill number")
