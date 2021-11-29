d = [1,10,100,1000,10000,100000,1000000]
dig_array = []
counter = 1
mult = 1

while len(dig_array) < 1000000:
    counter_str = str(counter)
    for char in counter_str:
        dig_array.append(char)
    counter += 1

for ind in d:
    mult *= int(dig_array[ind-1])
print(mult)