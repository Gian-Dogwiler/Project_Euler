triangle_nums = [1]
pentagonal_nums = [1]
hexagonal_nums = [1]
found = False
counter = 0
n_triangle, n_pentagonal, n_hexagonal = 1,1,1

def getTriangleNum(n: int):
    triangle_num = (n*(n+1))/2
    return triangle_num

def getPentagonalNum(n: int):
    pentagonal_num = (n*((3*n)-1))/2
    return pentagonal_num

def getHexagonalNum(n: int):
    hexagonal_num = n*((2*n)-1)
    return hexagonal_num

while not found:
    n_triangle += 1
    triangle_num = getTriangleNum(n_triangle)
    triangle_nums.append(triangle_num)

    while pentagonal_nums[-1] < triangle_nums[-1]:
        n_pentagonal += 1
        pentagonal_num = getPentagonalNum(n_pentagonal)
        pentagonal_nums.append(pentagonal_num)
    
    if triangle_nums[-1] in pentagonal_nums:

        while hexagonal_nums[-1] < triangle_nums[-1]:
            n_hexagonal += 1
            hexagonal_num = getHexagonalNum(n_hexagonal)
            hexagonal_nums.append(hexagonal_num)
        
        if triangle_nums[-1] in hexagonal_nums:
            counter += 1
            if counter == 2:
                found = True
                print(triangle_nums[-1])

