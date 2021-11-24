import math

prime_sum = 0
prime_array = [0,2]
from_num = 2

while(prime_array[-1] < 2000000):

    from_num += 1
    if from_num % 10000 == 0:
        print(from_num)
    num_half = int(math.ceil(from_num / 2))
    is_prime = True

    for i in range(num_half):
        if from_num % (i + 1) == 0 and i != 0:
            is_prime = False
            break

    if is_prime:
        prime_array.append(from_num)

for prime_num in prime_array[0:-1]:
    prime_sum += prime_num

print(prime_sum)