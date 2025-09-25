s = input("Enter a string: ")
n = int(input("Enter the division value: "))
l = len(s)
l1 = []
c = 0
if (l % n == 0 and l > n):
    for i in range(0, l, n):
        l1.append(s[i:i + n])
        c = c + 1

    flag = 1
    for i in range(c - 1):
        if (l1[i] != l1[i + 1]):
            flag = 0
            break
    if (flag == 1):
        for i in range(c):
            print(l1[i], end=" ")
    else:
        print("Sequence cannot be the same")


else:
    print("Division not possible")
