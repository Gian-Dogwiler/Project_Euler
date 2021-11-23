a = 0
b = 0
c = 0
sum_abc = 1000

def checkTheorem(a,b,c):
    
    a_sqrd = a**2
    b_sqrd = b**2
    c_sqrd = c**2
    param_array = [a_sqrd,b_sqrd,c_sqrd]
    param_array.sort()

    if (param_array[0] + param_array[1] == param_array[2]):
        if getProduct(a,b,c) == 0:
            return False
        else:
            return True
    else:
        return False

def getProduct(a,b,c):
    return a*b*c

for i in range(1001):
    a = i
    for j in range(1001-a):
        b = j
        c = 1000 - a - b
        is_found = checkTheorem(a,b,c)
        if is_found:
            print(getProduct(a,b,c))
            break
