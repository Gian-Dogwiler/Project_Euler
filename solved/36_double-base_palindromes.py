total_sum = 0

def checkPalindrome(n: int):
    n_str = str(n)
    palindrome = ''
    for char in range(1,len(n_str)+1):
        palindrome += n_str[-char]
    if palindrome == n_str:
        return True
    else:
        return False

def getBinaryNum(n: int):
    return bin(n)


for i in range(1,1000000):
    if checkPalindrome(i):
        binary_num = getBinaryNum(i)[2:]
        print(binary_num)
        if checkPalindrome(binary_num):
            total_sum += i

print(total_sum)
