# I was a bit lazy with this one, sorry ;)

total_sum = 75
highest_sum = 0
curr_ind = 0
hist = []
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

for i1 in range(2):
    total_sum += triangle_array[1][curr_ind + i1]
    curr_ind += i1
    for i2 in range(2):
        total_sum += triangle_array[2][curr_ind + i2]
        curr_ind += i2
        for i3 in range(2):
            total_sum += triangle_array[3][curr_ind + i3]
            curr_ind += i3
            for i4 in range(2):
                total_sum += triangle_array[4][curr_ind + i4]
                curr_ind += i4
                for i5 in range(2):
                    total_sum += triangle_array[5][curr_ind + i5]
                    curr_ind += i5
                    for i6 in range(2):
                        total_sum += triangle_array[6][curr_ind + i6]
                        curr_ind += i6
                        for i7 in range(2):
                            total_sum += triangle_array[7][curr_ind + i7]
                            curr_ind += i7
                            for i8 in range(2):
                                total_sum += triangle_array[8][curr_ind + i8]
                                curr_ind += i8
                                for i9 in range(2):
                                    total_sum += triangle_array[9][curr_ind + i9]
                                    curr_ind += i9
                                    for i10 in range(2):
                                        total_sum += triangle_array[10][curr_ind + i10]
                                        curr_ind += i10
                                        for i11 in range(2):
                                            total_sum += triangle_array[11][curr_ind + i11]
                                            curr_ind += i11
                                            for i12 in range(2):
                                                total_sum += triangle_array[12][curr_ind + i12]
                                                curr_ind += i12
                                                for i13 in range(2):
                                                    total_sum += triangle_array[13][curr_ind + i13]
                                                    curr_ind += i13
                                                    for i14 in range(2):
                                                        total_sum += triangle_array[14][curr_ind + i14]
                                                        curr_ind += i14
                                                        hist.append(total_sum)
                                                        if total_sum > highest_sum:
                                                            highest_sum = total_sum
                                                            print(highest_sum)
                                                        curr_ind -= i14
                                                        total_sum -= triangle_array[14][curr_ind + i14]
                                                    curr_ind -= i13
                                                    total_sum -= triangle_array[13][curr_ind + i13]
                                                curr_ind -= i12
                                                total_sum -= triangle_array[12][curr_ind + i12]
                                            curr_ind -= i11
                                            total_sum -= triangle_array[11][curr_ind + i11]
                                        curr_ind -= i10
                                        total_sum -= triangle_array[10][curr_ind + i10]
                                    curr_ind -= i9
                                    total_sum -= triangle_array[9][curr_ind + i9]
                                curr_ind -= i8
                                total_sum -= triangle_array[8][curr_ind + i8]
                            curr_ind -= i7
                            total_sum -= triangle_array[7][curr_ind + i7]
                        curr_ind -= i6
                        total_sum -= triangle_array[6][curr_ind + i6]
                    curr_ind -= i5
                    total_sum -= triangle_array[5][curr_ind + i5]
                curr_ind -= i4
                total_sum -= triangle_array[4][curr_ind + i4]
            curr_ind -= i3
            total_sum -= triangle_array[3][curr_ind + i3]
        curr_ind -= i2
        total_sum -= triangle_array[2][curr_ind + i2]
    curr_ind -= i1
    total_sum -= triangle_array[1][curr_ind + i1]

print(highest_sum)