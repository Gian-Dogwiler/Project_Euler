import math

a_val = 0
b_val = 0
longest_seq_len = 0
highest_prod = 0

def quadratic_formula(x: int, a: int,b: int):
    value = (x*x) + (a*x) + b
    return value

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

for a in range(-999,1000):
    print(a)
    for b in range(-1000,1001):
        counter = 0
        done = False
        while not done:
            new_val = quadratic_formula(counter,a,b)
            if checkPrimeNumber(new_val):
                counter += 1
            else:
                done = True
        if longest_seq_len < counter:
            longest_seq_len = counter
            a_val = a
            b_val = b
            print(longest_seq_len, ' ', a_val, ' ', b_val)

highest_prod = a_val * b_val
print(highest_prod)
