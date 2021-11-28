import numpy as np

w,h = 21,21
matrix = [[0 for i in range(w)] for j in range(h)]
for i in range(21):
    matrix[20][i] = 1
    matrix[i][0] = 1
for i in range(20):
    for j in range(20):
        matrix[19-i][1+j] = matrix[20-i][1+j] + matrix[19-i][j]

for i in range(20):
    matrix[19-i][20] = matrix[20-i][20] + matrix[19-i][19]

print(np.array(matrix))
print('Number of possible paths: ' + str(matrix[0][20]))