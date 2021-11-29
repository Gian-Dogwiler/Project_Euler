import math
from itertools import permutations

def getPermutations(num: int):
    num_str = str(num)
    perms_arr = []
    perms = permutations(num_str)
    for perm in perms:
        permutation = ''
        for dig in perm:
            permutation += dig
        perms_arr.append(int(permutation))
    return perms_arr

def checkPrimeNumber(prime_num: int):
    if prime_num < 2:
        return False
    if prime_num == 2 or prime_num == 3:
        return True
    half_num = math.ceil(prime_num/2)
    is_prime = True
    for num in range(2,half_num):
        if prime_num % num == 0:
            is_prime = False
            break
    return is_prime

for i in range(1000,10000):
    if checkPrimeNumber(i):
        perms_set= set(sorted(getPermutations(i)))
        concatenation = str(i)
        hist = [i]
        for perm in perms_set:
            if checkPrimeNumber(perm):
                if perm - i == 3330 or perm - i == 6660:
                    concatenation += str(perm)
                    hist.append(perm)

        if len(set(hist)) == 3:
            hist = sorted(set(hist))
            print(concatenation)

