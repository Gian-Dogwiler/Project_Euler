import math

num = 10000

def getPrimeNumbers(max_val):
    
    prime_nums = []
    
    for i in range(max_val):
        half_num = int(math.ceil(i / 2))
        is_prime = True
        for j in range(half_num):
            if i % (j + 1) == 0 and j != 1:
                is_prime = False
        if is_prime:
            prime_nums.append(i)
    return prime_nums

def getPrimeFactors(number):

    prime_array = getPrimeNumbers(number)
    print(prime_array)

getPrimeFactors(num)
