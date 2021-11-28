# multiplicants are surely limited to 9999 * 1 = 9999
total_sum = 0
digits_array = ['1','2','3','4','5','6','7','8','9']
prod_array = []

def checkPandigital(mult_one: int, mult_two: int):
    nums_array = []
    product = mult_one * mult_two
    num_str = str(product)+str(mult_one)+str(mult_two)
    if len(num_str) != 9:
        return False
    for digit in num_str:
        nums_array.append(digit)
    if set(digits_array) == set(nums_array):
        return True
    else:
        return False

for a in range(1,10000):
    for b in range(1,10000):
        if checkPandigital(a,b):
            print(a, ' ', b, ' ', a*b)
            is_pandigital = True
            for prod in prod_array:
                if prod == a*b:
                    is_pandigital = False
            if is_pandigital:
                prod_array.append(a*b)
                total_sum += (a*b)

print(total_sum)
print(prod_array)