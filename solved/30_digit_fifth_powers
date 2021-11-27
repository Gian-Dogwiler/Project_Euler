# 9^5 = 59049 -> 999999 is already out of reach
num_array = []
total_sum = 0

def getSum(n: int):
    n_str = str(n)
    sum = 0
    for char in n_str:
        digit = int(char)
        power_digit = digit ** 5
        sum += power_digit
    return sum

for num in range (2,1000000):
    if num == getSum(num):
         num_array.append(num)
    if num % 10000 == 0:
        print(num)

for num in num_array:
    total_sum += num

print(total_sum)