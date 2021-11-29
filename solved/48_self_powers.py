sum = 0

for i in range(1,1001):
    num = i
    for j in range(2,i+1):
        num = num * i
        if len(str(num)) > 10:
            num_str = str(num)
            num_10 = num_str[-11:]
            num = int(num_10)
    sum += num

final_num = str(sum)[-10:]
print(final_num)