import math

counter = 9
squares_counter = 1
prime_counter = 3
found = False
prime_nums = [3]
twice_squares = [2]

def checkOddComposite(n: int):
    if n % 2 == 0:
        return False
    else:
        half_num = int(math.ceil(n)/2)
        for i in range(3,half_num+1):
            if n % i == 0:
                return True
        return False

def checkPrime(num: int):
    half_num = math.ceil(num/2)
    is_prime = True
    if num < 3 or num == 4:
        return False
    if num == 3:
        return True
    for i in range(1,half_num):
        if i != 1 and num % i == 0:
            is_prime = False
            break
    return is_prime

def getTwiceSquared(num: int):
    value = 2 * (num**2)
    return value


while not found:

    is_found = False

    while prime_nums[-1] < counter:
        prime_counter += 1
        if checkPrime(prime_counter):
            prime_nums.append(prime_counter)
    
    while twice_squares[-1] < counter:
        squares_counter += 1
        new_squared = getTwiceSquared(squares_counter)
        twice_squares.append(new_squared)
    
    for prime in prime_nums:
        for squares in twice_squares:
            if prime + squares == counter:
                is_found = True
                break
    
    if not is_found:
        found = True
        print(counter)

    counter += 1
    while not checkOddComposite(counter):
        counter += 1