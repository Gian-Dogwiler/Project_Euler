import math

highest_divisors = 0
counter = 0

def get_triangle_num(n: int):
    sum = 0
    for i in range(n):
        sum += i
    return sum

def get_divisors(triangle_num: int):
    half_num = math.ceil(triangle_num / 2)
    num_divisors = 0
    for i in range(half_num):
        if triangle_num % (i+1) == 0:
            num_divisors += 1
        elif (i == 2 or i == 3 or i == 4 or i == 5):
            break
    return num_divisors

while highest_divisors < 500:
    counter += 1
    triangle_num = get_triangle_num(counter)
    num_divisors = get_divisors(triangle_num)
    if highest_divisors < num_divisors:
        highest_divisors = num_divisors
        print(highest_divisors)
        if highest_divisors > 500:
            print(triangle_num)