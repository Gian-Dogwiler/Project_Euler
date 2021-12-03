import math
from itertools import permutations

prime_arr = []

def getPermutations(primes_arr: list):
    permutations_arr = permutations(primes_arr)
    permutations_arr = list(permutations_arr)
    return permutations_arr


def checkPrimeNumber(prime_num: int):
    if prime_num < 2 or prime_num == 4:
        return False
    if prime_num == 2 or prime_num == 3:
        return True
    half_num = math.ceil(math.sqrt(prime_num))
    is_prime = True
    for num in range(2,half_num):
        if prime_num % num == 0:
            is_prime = False
            break
    return is_prime

for num in range(1,10001):
    if checkPrimeNumber(num):
        prime_arr.append(num)

for prime in prime_arr:
    conc_arr = [str(prime)]
    for prime2 in prime_arr:
        conc_arr.append(str(prime2))
        print(conc_arr)
        all_perms = getPermutations(conc_arr)
        to_check_arr = []
        for perm in all_perms:
            to_check = ''
            for digit in perm:
                to_check += str(digit)
            if not checkPrimeNumber(int(to_check)):
                conc_arr.pop(-1)
                break

    if len(conc_arr) == 4:
        print(conc_arr)
        _ = input()
    else:
        print('nope', str(prime))

