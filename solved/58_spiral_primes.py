import math

curr_num = 1
num_spirals = 1
percentage = 100.0
num_primes = 0

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

while percentage > 0.1:

    num_spirals += 1

    if num_spirals % 1000 == 0:
        print(num_spirals, ' ',percentage)
    
    num_elements = ((num_spirals - 1) * 2) * 4
    counter = 1
    counter_2 = 0
    for i in range(1,num_elements+1):
        curr_num += 1
        if counter == ((num_spirals - 1) * 2):
            counter += 1
            counter_2 += 1
            if checkPrimeNumber(curr_num) and counter_2 != 4:
                num_primes += 1
            counter = 0
        counter += 1

    
    percentage = (num_primes / ((num_spirals * 4) - 3))
    print(percentage)
print(percentage)
print((num_spirals*2)-1)