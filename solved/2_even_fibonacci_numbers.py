fib_sequence = []
num_one, num_two = 1,2
total_sum = 0

fib_sequence.append(num_one)
fib_sequence.append(num_two)

while fib_sequence[-1] < 4000000:
    new_fib = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(new_fib)

for fib in fib_sequence:
    if fib % 2 == 0:
        total_sum += fib

print('Total Sum: ', str(total_sum))
