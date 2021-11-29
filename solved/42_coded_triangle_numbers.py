triangle_numbers = []
total_triangle_nums = 0

words_file = open('../files/p042_words.txt','r')
words_file = words_file.read()
words_file = str(words_file)
words_file = words_file.replace(',',' ')
words_file = words_file.replace('"','')
words_arr = words_file.split()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def getTriangleNum(n: int):
    triangle_num = (0.5 * (n ** 2)) + (0.5 * n)
    return triangle_num

for i in range(1,1001):
    triangle_numbers.append(getTriangleNum(i))

for word in words_arr:
    sum = 0
    for char in word:
        sum += alphabet.index((char.lower())) + 1
    if float(sum) in triangle_numbers:
        total_triangle_nums += 1

print(total_triangle_nums)