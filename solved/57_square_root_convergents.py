from fractions import Fraction

counter = 0
start_num = 1
iter_val = 1/2
prev_fraction = Fraction(iter_val)

def checkFraction(fraction: str):
    is_fulfilled = False
    
    div_array = fraction.split('/')
    nominator_len = len(div_array[0])
    denominator_len = len(div_array[1])

    if nominator_len > denominator_len:
        is_fulfilled = True
    return is_fulfilled

for iter in range(1000):
    val = start_num + iter_val
    fraction = str(Fraction(val))
    if checkFraction(fraction):
        counter += 1
    iter_val = 1 / (2 + prev_fraction)
    prev_fraction = iter_val

print(counter)