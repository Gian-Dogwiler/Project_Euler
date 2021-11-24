import math

abundant_nums = []
sum_set = []
nums_set = [i for i in range(28124)]
total_sum = 0

for i in range (9,28124):
    divisors_array = []
    divisors_sum = 0
    half_num = math.ceil(i/2)
    for j in range(half_num+2):
        if i % (j+1) == 0:
            divisors_array.append(j+1)
    for divisor in divisors_array:
        divisors_sum += divisor
    if divisors_sum > i:
        abundant_nums.append(i)

for i in abundant_nums:
    for j in abundant_nums:
        sum = i+j
        if sum <= 28123:
            sum_set.append(sum)

nums_set = set(nums_set)
sum_set = set(sum_set)

no_sum_set = nums_set.difference(sum_set)
for num in no_sum_set:
    total_sum += num

print(total_sum)
