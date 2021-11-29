highest_num = 0
seq = {1,2,3,4,5,6,7,8,9}

for i in range(1,100000):
    concatenated_num = str(i)
    n = 2
    concatenated_arr = []
    while len(concatenated_num) < 9:
        next_num = str(i * n)
        concatenated_num += next_num
        n += 1
    if len(concatenated_num) != 9:
        continue
    else:
        for char in concatenated_num:
            concatenated_arr.append(int(char))
        if set(concatenated_arr) == set(seq):
            if int(concatenated_num) > highest_num:
                highest_num = int(concatenated_num)
                print(highest_num)
