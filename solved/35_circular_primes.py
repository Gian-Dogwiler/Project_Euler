import itertools
import math

primes_array = []
total_sum = 0

def checkPrime(num: int):
    half_num = math.ceil(num/2)
    is_prime = True
    if num == 4:
        return False
    for i in range(1,half_num):
        if i != 1 and num % i == 0:
            is_prime = False
            break
    return is_prime

def getPermutations(num: int):
    num_str = str(num)
    if len(num_str) == 1:
        return [num_str]
    elif len(num_str) == 2:
        return [num_str, str(num_str[1]+num_str[0])]
    else:
        new_num = num_str
        perms = []
        for i in range(len(num_str)):
            new_num = new_num[1:] + new_num[0]
            perms.append(new_num)
        return perms

for num in range(2,1000001):
    if checkPrime(num):
        permutations = getPermutations(num)
        is_circular = True
        for perm in permutations:
            if not checkPrime(int(perm)):
                is_circular = False
                break
        if is_circular:
            primes_array.append(num)
            print(num)
            print(permutations)

print(primes_array)
print(len(primes_array))