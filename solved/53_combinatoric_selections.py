curr_n = 0
counter = 0

def getFactorial(p: int):
    p_counter = p
    p_fact = 1
    if p == 0 or p == 1:
        return 1
    while p_counter != 1:
        p_fact *= p_counter
        p_counter -= 1
    return p_fact

for n in range(0,101):
    for r in range(0,101):
        if r < n:
            nominator = getFactorial(n)
            r_fact = getFactorial(r)
            diff = n-r
            diff_fact = getFactorial(diff)
            denominator = diff_fact*r_fact
            binomial = nominator/denominator
            if binomial > 1000000:
                counter += 1

print(counter)