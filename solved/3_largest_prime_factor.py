import math

prime_nums_array = [2,3]
divisors_array = []
num = 600851475143
done = False

def getNextPrime(starting_number: int):
    num_found = False
    from_num = starting_number
    while not num_found:
        from_num += 1
        half_num = math.ceil(from_num/2)
        is_prime = True
        for i in range(1,half_num):
            if i != 1 and from_num % i == 0:
                is_prime = False
        if is_prime:
            prime_nums_array.append(int(from_num))
            num_found = True

while not done:
    succ = False
    for prime in prime_nums_array:
        if num % prime == 0:
            succ = True
            num = num / prime
            divisors_array.append(int(prime))
            print(num)

    if num == 1:
        done = True

    if not succ:
        getNextPrime(prime_nums_array[-1])

print(prime_nums_array)