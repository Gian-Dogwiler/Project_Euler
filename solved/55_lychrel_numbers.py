import math

lychrel_counter = 0
limit = 10000

def checkPalindrome(num: str):
    is_palindrome = True
    half_len = math.ceil(len(num)/2)
    for i in range(0,half_len):
        if num[i] != num[-(i+1)]:
            is_palindrome = False
            break
    return is_palindrome

for num in range (0,limit):
    counter = 0
    num_str = str(num)
    found = False

    while not found:
        if counter > 49:
            break
        reverse = ''
        for i in range(1,len(num_str)+1):
            reverse += num_str[-i]
        num_str = str(int(num_str) + int(reverse))
        if checkPalindrome(num_str):
            found = True
            lychrel_counter += 1
        counter += 1

print(limit-lychrel_counter)