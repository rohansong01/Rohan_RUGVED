
n = int(input("Enter the size of the matrix (n x n): "))
matrix = []

print("Enter the matrix elements row by row:")
for i in range(n):
    row = []
    for j in range(n):
        value = int(input(f"Enter element at position ({ i +1},{ j +1}): "))
        row.append(value)
    matrix.append(row)


rotated = []
for i in range(n):
    new_row = []
    for j in range(n):
        new_row.append(matrix[n - j - 1][i])
    rotated.append(new_row)

print("\nMatrix after 90° clockwise rotation:")
for row in rotated:
    print(row)



print("\nSpiral order of rotated matrix:")
top = 0
bottom = n - 1
left = 0
right = n - 1

while top <= bottom and left <= right:

    for i in range(left, right + 1):
        print(rotated[top][i], end=" ")
    top += 1


    for i in range(top, bottom + 1):
        print(rotated[i][right], end=" ")
    right -= 1


    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(rotated[bottom][i], end=" ")
        bottom -= 1


    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(rotated[i][left], end=" ")
        left += 1