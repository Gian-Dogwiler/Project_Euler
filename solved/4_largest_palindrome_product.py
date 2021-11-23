num_one = 0
num_two = 0
highest_num = 0

def checkPalindrome(num):
    number_str = str(num)
    is_palindrome = True
    counter = 0
    for index in range(len(number_str) - 1):
        if number_str[index] != number_str[-(index + 1)]:
            is_palindrome = False
    return is_palindrome

for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        if checkPalindrome(product):
            if product > highest_num:
                highest_num = product

print(highest_num)
