highest_sum = 0

for a in range(1,100):
    for b in range(1,100):
        num = a**b
        num_str = str(num)
        sum = 0
        for digit in num_str:
            sum += int(digit)
        if sum > highest_sum:
            highest_sum = sum

print(highest_sum)