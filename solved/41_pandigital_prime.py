# largest pandigital number = 987654321

import math

counter = 0
found = False
pand_arr = ['1','2','3','4','5','6','7','8','9']

def checkPandigital(num: int):
    num_str = str(num)
    dig_arr = []
    for char in num_str:
        dig_arr.append(char)
    n_len = len(dig_arr)
    arr_to_check = pand_arr[:n_len]
    if set(dig_arr) == set(arr_to_check):
        return True
    else:
        return False
    
def checkPrime(num: int):
    half_num = math.ceil(num/2)
    is_prime = True
    if num == 4:
        return False
    for i in range(1,half_num):
        if i != 1 and num % i == 0:
            is_prime = False
            break
    return is_prime
    

while not found:
    num = 987654321 - counter
    if checkPandigital(num):
        if checkPrime(num):
            found = True
            print(num)
    counter += 1
