curr_num = 0
found = False

def checkNum(num: int):
    dig_arr = []
    for digit in str(num):
        dig_arr.append(digit)
    return dig_arr

while not found:
    curr_num += 1
    is_same = True
    dig_arr = checkNum(curr_num)
    for i in range(2,7):
        if set(dig_arr) != set(checkNum(i*curr_num)):
            is_same = False
    if is_same:
        print('found: ', str(curr_num))
        found = True