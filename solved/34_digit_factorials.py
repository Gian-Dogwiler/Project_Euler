# the upper range is limited to 2540160 since = 8*9!

total_sum = 0

def getFactorial(n: int):
    counter = n
    if n == 0:
        return 1
    while counter >= 2:
        n = n*(counter-1)
        counter -= 1
    return n

for i in range(3,2903041):
    sum = 0
    for char in str(i):
        sum += getFactorial(int(char))
    if sum == i:
        total_sum += i
        print(i)
    
print(total_sum)