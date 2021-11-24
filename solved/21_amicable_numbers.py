amic_num_arr = []
amic_num_sum = 0

def getDivisors(sum: int, to_num: int):
    curr_num = sum-2
    div_arr = []
    div_sum = 0
    for j in range(curr_num):
        if j != 0 and sum % j == 0:
            div_arr.append(j)
    for el in div_arr:
        div_sum += el
    return div_sum

for i in range(2,10000):
    div_arr = []
    div_sum = 0
    curr_num = i-2
    for j in range(curr_num):
        if j != 0 and i % j == 0:
            div_arr.append(j)
    for el in div_arr:
        div_sum += el

    if getDivisors(div_sum, i) == i and i != div_sum:
        amic_num_arr.append(i)
        amic_num_arr.append(div_sum)
amic_num_set = set(amic_num_arr)
print(amic_num_set)
for num in amic_num_set:
    amic_num_sum += num

print(amic_num_sum)