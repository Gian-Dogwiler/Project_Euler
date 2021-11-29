import math

counter = 0
seq = 0
found = False
primes_arr = [2,3,5]
primes_counter = 5
hist = []

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

while not found:

    counter += 1
    num = counter
    divisors = []
    divs_found = False

    while primes_arr[-1] < counter:
        primes_counter += 1
        if checkPrimeNumber(primes_counter):
            primes_arr.append(primes_counter)
    
    while not divs_found:
        div_found = False
        for prime in primes_arr:
            if num % prime == 0:
                num = num / prime
                divisors.append(prime)
                div_found = True

        if not div_found:
            break
        
        if num == 1:
            divs_found == True
            if len(set(divisors)) == 4:
                hist.append(counter)
                if ((counter-1) in hist and (counter-2) in hist and (counter-3) in hist):
                    print(counter-3)
                    found = True