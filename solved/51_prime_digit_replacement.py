# 1: last digit can't be replaced since it would be divisible by 2,5,10... -> (family of at most 7)
import math
from itertools import permutations

found = False
curr_num = '100000'
curr_num_len = 4
last_dig_checks = [0,2,4,5,6,8]
perms_checked = []
perms = []

def checkPrimeNumber(prime_num: int):
    if prime_num < 2 or prime_num == 4:
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

def getResults(number: str):
    counter = 0
    hist = []
    for i in range(0,10):
        check_num = number.replace('i',str(i))
        if checkPrimeNumber(int(check_num)):
            counter += 1
            hist += check_num
    if counter >= 8:
        print(hist)
        _ = input('found:')
        return True

def getPerms():
    perms = []
    for i in range(1,len(str(curr_num))):
        first_perm = 'i'*i
        diff = len(str(curr_num)) - i
        first_perm += 'p'*diff
        perms_arr = permutations(first_perm)
        for perm in perms_arr:
            perms.append(perm)
            if perm[-1] == 'i':
                perms.remove(perm)
    perms = set(perms)
    return perms

def getLastDigit(number: str):
    nums_arr = []
    for j in [1,3,7,9]:
        new_num = number[:-1] + str(j)
        nums_arr.append(new_num)
    return nums_arr

while not found:

    perms = getPerms()

    final_arr = []

    for perm in perms:
        print(perm)
        perm_str = ''
        for digit in perm:
            perm_str += digit
        num_to_iterate = 5 - perm_str.count('i')

        if num_to_iterate == 0:
            final_arr = getLastDigit(perm_str)
            for number in final_arr:
                print(number)
                found = getResults(number)

        elif num_to_iterate == 1:
            for i1 in range(0,10):
                perm_copy = perm_str
                perm_copy = perm_copy.replace('p',str(i1))
                final_arr = getLastDigit(perm_copy)
                for number in final_arr:
                    print(number)
                    found = getResults(number)

        elif num_to_iterate == 2:
            for i1 in range(0,10):
                for i2 in range(0,10):
                    perm_copy = perm_str
                    perm_copy = perm_copy.replace('p',str(i1),1)
                    perm_copy = perm_copy.replace('p',str(i2),1)
                    final_arr = getLastDigit(perm_copy)
                    for number in final_arr:
                        print(number)
                        found = getResults(number)
        
        elif num_to_iterate == 3:
            for i1 in range(0,10):
                for i2 in range(0,10):
                    for i3 in range(0,10):
                        perm_copy = perm_str
                        perm_copy = perm_copy.replace('p',str(i1),1)
                        perm_copy = perm_copy.replace('p',str(i2),1)
                        perm_copy = perm_copy.replace('p',str(i3),1)
                        print(perm_copy)
                        
                        final_arr = getLastDigit(perm_copy)
                        for number in final_arr:
                            print(number)
                            found = getResults(number)
        
        elif num_to_iterate == 4:
            for i1 in range(0,10):
                for i2 in range(0,10):
                    for i3 in range(0,10):
                        for i4 in range(0,10):
                            perm_copy = perm_str
                            perm_copy = perm_copy.replace('p',str(i1),1)
                            perm_copy = perm_copy.replace('p',str(i2),1)
                            perm_copy = perm_copy.replace('p',str(i3),1)
                            print(perm_copy)
                        
                            final_arr = getLastDigit(perm_copy)
                            for number in final_arr:
                                print(number)
                                found = getResults(number)
    _ = input('not found')

print('found')