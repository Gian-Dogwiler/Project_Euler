from itertools import permutations

sum_with_property = 0
digits = [0,1,2,3,4,5,6,7,8,9]
all_permutations = permutations(digits)
prime_nums = [2,3,5,7,11,13,17]

def checkProperties(num: str):
    for i in range(1,8):
        seq = int(num[i] + num[i+1] + num[i+2])
        if seq % prime_nums[i-1] != 0:
            return False
    return True


for perm in all_permutations:
    num_str = ''
    for dig in perm:
        num_str += str(dig)
    if checkProperties(num_str):
        sum_with_property += int(num_str)

print(sum_with_property)