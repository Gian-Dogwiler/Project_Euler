archive = []
totalSum = 0

for number in range(1000):
    if number % 3 == 0:
        archive.append(number)
    elif number % 5 == 0:
        archive.append(number)

for number in archive:
    totalSum += number

print(archive)
print('Total Sum: ', str(totalSum))
