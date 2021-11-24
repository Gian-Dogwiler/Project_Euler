total_sum = 0
curr_row = 0
curr_col = 0
path_hist = []
triangle_array = [
[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,47,65],
[19,1,23,75,3,34],
[88,2,77,73,7,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
]

def getNextNums(arr_row: int, arr_col: int):
    next_row_ind = arr_row + 1
    next_num_ind = [arr_col, arr_col + 1]
    return next_row_ind, next_num_ind

for i in range(14):
    total_sum += triangle_array[curr_row][curr_col]
    path_hist.append(triangle_array[curr_row][curr_col])
    
    next_row, next_inds = getNextNums(curr_row, curr_col)
    if triangle_array[next_row][next_inds[0]] >= triangle_array[next_row][next_inds[1]]:
        curr_col = next_inds[0]
    else:
        curr_col = next_inds[1]
    curr_row = next_row

print(total_sum)
print(path_hist)
