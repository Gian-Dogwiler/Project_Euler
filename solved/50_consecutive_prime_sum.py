import math

all_primes = []
highest_prime = 0
most_terms = 0

def checkPrimeNumber(prime_num: int):
    if prime_num < 2 or prime_num == 4:
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

for num in range(1,1000000):
    if checkPrimeNumber(num):
        all_primes.append(num)
    if num % 10000 == 0:
        print(num)

for ind1 in range(len(all_primes)-1):
    print(ind1)
    if ind1 >= 100:
        break
    sum = all_primes[ind1]
    ind = ind1
    terms = 1
    done = False
    while sum < 1000000 or done:
        ind += 1
        if ind >= len(all_primes)-1:
            done = True
            continue
        terms += 1
        sum += all_primes[ind]
        if sum in all_primes and terms > most_terms:
            highest_prime = sum
            most_terms = terms
            print(most_terms, ' ', highest_prime)
print(highest_prime, ' ',  most_terms)