A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

A_t = []
for i in range(len(A[0])):
    new_row = []
    for row in A:
        new_row.append(row[i])
    A_t.append(new_row)
    
print(A_t)
