is_found = False
counter = 0

while not(is_found):
    
    counter += 1
    is_divisible = True
    
    for i in range(2,21):
        if counter % i != 0:
            is_divisible = False
            break

    if is_divisible:
        is_found = True

print(counter)
