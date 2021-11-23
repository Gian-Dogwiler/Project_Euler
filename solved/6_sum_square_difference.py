sum_natural = 0
sum_squared = 0
squared_sum = 0

for i in range(101):
    sum_natural += i
    sum_squared += i**2
    print(i)

squared_sum = sum_natural ** 2

difference = squared_sum - sum_squared
print(difference)
