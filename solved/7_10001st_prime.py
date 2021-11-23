import math

prime_num_array = []
from_num = 1

while len(prime_num_array) != 10001:
    
    from_num += 1
    num_half = math.ceil(from_num / 2)
    is_prime = True
    
    for i in range(num_half):
        if from_num % (i + 1) == 0 and i != 0 and i != from_num:
            is_prime = False
            break

    if is_prime:
        prime_num_array.append(from_num)

print(prime_num_array[-1])
