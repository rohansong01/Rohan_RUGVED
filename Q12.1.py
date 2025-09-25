n = int(input("Enter the range: "))

for i in range(0, n, 1):
    for j in range(n - i, -1, -1):
        print(" ", end="")
    for j in range(0, i + 1, 1):
        print("*", end=" ")
    print("\n")
for i in range(n, -1, -1):

    for j in range(n - i, -1, -1):
        print(" ", end="")
    for j in range(0, i + 1, 1):
        print("*", end=" ")
    print("\n")