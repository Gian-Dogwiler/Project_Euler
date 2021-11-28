num_possibilities = 1 # for 1 * 2 pounds

for two_pence in range(0,101):
    for five_pence in range(0,41):
        for ten_pence in range(0,21):
            for twenty_pence in range(0,11):
                for fifty_pence in range(0,5):
                    for one_pound in range(0,3):
                        sum =  (two_pence*2) + (five_pence*5) + (ten_pence*10) + (twenty_pence*20) + (fifty_pence*50) + (one_pound*100)
                        if sum <= 200: # you can always fill up with one-pences (makes program run 200 times faster)
                            num_possibilities += 1

print(num_possibilities)