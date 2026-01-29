matrix = []
for i in range(9):
    matrix.append(list(map(int, input().split())))
maxval = matrix[0][0]
maxindex = [0, 0]
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] > maxval:
            maxval = matrix[row][col]
            maxindex = [row, col]

print(maxval)
print(maxindex[0] + 1, maxindex[1] + 1)