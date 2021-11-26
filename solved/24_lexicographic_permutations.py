nums_set: set = {0,1,2,3,4,5,6,7,8,9}
final_num = 0
curr_perm= 123456789
perm_number = 1

def checkPermNumber(n):
    str_n = ''
    n_set = {}
    n_set = set(n_set)
    if len(str(n)) == 9:
        str_n = '0' + str(n)
    else:
        str_n += str(n)
    for char in str_n:
        n_set.add(int(char))
    return set(nums_set) == set(n_set)
    

while perm_number != 1000:
    curr_perm += 1
    if checkPermNumber(curr_perm):
        print(perm_number)
        perm_number += 1
        print(curr_perm)

final_num = curr_perm
print(final_num)