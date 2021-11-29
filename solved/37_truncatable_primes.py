import math

counter = 10
primes_arr = []
total_sum = 0

def checkPrime(n: int):
    if n == 1 or n == 4:
        return False
    half_num = math.ceil(n/2)
    is_prime = True
    for i in range(2,half_num):
        if n % i == 0:
            is_prime = False
            break
    return is_prime

def truncateNum(n: int):
    is_truncatable = True
    num_str = str(n)
    for i in range(1,len(num_str)):
        num_to_check = num_str[1:]
        if not checkPrime(int(num_to_check)):
            is_truncatable = False
            break
        num_str = num_to_check
    num_str = str(n)
    for i in range(1,len(num_str)):
        num_to_check = num_str[:-1]
        if not checkPrime(int(num_to_check)):
            is_truncatable = False
            break
        num_str = num_to_check
    return is_truncatable

while len(primes_arr) != 11:
    is_prime = checkPrime(counter)
    if is_prime:
        if truncateNum(counter):
            primes_arr.append(counter)
            print(len(primes_arr), ' ', primes_arr[-1])
    counter += 1

for trunc_prime in primes_arr:
    total_sum += trunc_prime

print(total_sum)