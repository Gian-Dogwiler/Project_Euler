start_value = 99
final_sum = 100
done = False
sum = 0

while not done:
    final_sum = final_sum * start_value
    start_value -= 1
    if start_value == 0:
        done = True

final_sum_str = str(final_sum)
for char in final_sum_str:
    sum += int(char)

print(sum)