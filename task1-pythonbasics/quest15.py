mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("The Original Matrix is : ")
for row in mat:
    print(row)

mat = [list(row)[::-1] for row in zip(*mat)]

print("\nRotated Matrix :")
for row in mat:
    print(row)
