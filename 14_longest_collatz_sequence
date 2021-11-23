longest_seq = 0
longest_num = 0

def next_num(n: int):
    if n % 2 == 0:
        return (n/2)
    else:
        return (3*n+1)

for i in range (1,1000001):
    counter = 0
    start_num = i
    if i % 10000 == 0:
        print(i, longest_num)
    while start_num != 1:
        start_num = next_num(start_num)
        counter += 1
    if counter > longest_seq:
        longest_seq = counter
        longest_num = i

print(longest_num)
print(longest_seq)