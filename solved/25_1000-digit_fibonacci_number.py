fib_array = [1,1]
while len(str(fib_array[-1])) != 1000:
    new_fib = fib_array[-1] + fib_array[-2]
    fib_array.append(new_fib)

print(fib_array)
print(len(fib_array))