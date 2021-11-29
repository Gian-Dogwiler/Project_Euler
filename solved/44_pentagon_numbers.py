found = False
pent_nums = []

def getPentagonNum(n: int):
    pentagon_num = (n*((3*n)-1))/2
    return int(pentagon_num)

def getAbsDiff(n1: int, n2: int):
    diff = n2 - n1
    if diff < 0:
        diff *= -1
    return int(diff)

for n in range(1,5000):
    pent_nums.append(getPentagonNum(n))

smallest_diff = getAbsDiff(pent_nums[0], pent_nums[-1])

for pent1 in pent_nums:
    for pent2 in pent_nums:
        if pent1 == pent2:
            continue
        diff = int(getAbsDiff(pent1, pent2))
        if diff < smallest_diff:
            sum = pent1 + pent2
            if sum in pent_nums:
                if diff in pent_nums:
                    print(pent1,' ',pent2)
                    smallest_diff = diff

print(smallest_diff)
