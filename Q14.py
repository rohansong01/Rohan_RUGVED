
n = int(input("Enter the number of elements: "))
arr = []


for i in range(n):
    num = int(input("Enter element " + str(i+1) + ": "))
    arr.append(num)


found = False
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            print("First repeating element is:", arr[i],"found at index: ",i)
            found = True
            break
    if found:
        break


if not found:
    print("No repeating elements")