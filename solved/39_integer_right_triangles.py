import math

highest_solutions = 0

def getCValue(a: int, b: int):
    c_sqrd = a**2 + b**2
    c = math.sqrt(c_sqrd)
    return c

for p in range(1,1001):
    solutions_counter = 0
    print(p)
    for a in range(1,p):
        for b in range(1,p):
            c = getCValue(a,b)
            if a+b+c == p:
                solutions_counter += 1
                print(' ',a,' ',b,' ',c)
    if solutions_counter > highest_solutions:
        highest_solutions = solutions_counter
        print('woeifk', highest_solutions)
print(highest_solutions)