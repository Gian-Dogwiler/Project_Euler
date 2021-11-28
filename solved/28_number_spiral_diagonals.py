curr_space = 2
total_sum = 1
counter = 1
num = 1

while curr_space != 1002:
    for _ in range(4):
        num += curr_space
        total_sum += num
    curr_space += 2

print(total_sum)

    