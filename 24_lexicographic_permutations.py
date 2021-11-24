# permutations for 0********* = 9!
nums_array = [0,1,2,3,4,5,6,7,8,9]
final_num = 0
rest = 1000000

nine_fact = 9*8*7*6*5*4*3*2
eight_fact = 8*7*6*5*4*3*2
seven_fact = 7*6*5*4*3*2
six_fact = 6*5*4*3*2
five_fact = 5*4*3*2
four_fact = 4*3*2
three_fact = 3*2
two_fact = 2

first_num = nums_array[(rest // nine_fact)]
nums_array.pop(nums_array.index(first_num))
rest = rest-((rest // nine_fact)*nine_fact)

second_num = nums_array[(rest//eight_fact)]
nums_array.pop(nums_array.index(second_num))
rest = rest-((rest//eight_fact)*eight_fact)

third_num = nums_array[(rest//seven_fact)]
nums_array.pop(nums_array.index(third_num))
rest = rest-((rest//seven_fact)*seven_fact)

fourth_num = nums_array[(rest//six_fact)]
nums_array.pop(nums_array.index(fourth_num))
rest = rest-((rest//six_fact)*six_fact)

fivth_num = nums_array[(rest//five_fact)]
nums_array.pop(nums_array.index(fivth_num))
rest = rest-((rest//five_fact)*five_fact)

sixth_num = nums_array[(rest//four_fact)]
nums_array.pop(nums_array.index(sixth_num))
rest = rest-((rest//four_fact)*four_fact)

seventh_num = nums_array[(rest//three_fact)]
nums_array.pop(nums_array.index(seventh_num))
rest = rest-((rest//three_fact)*three_fact)

eighth_num = nums_array[(rest//two_fact)]
nums_array.pop(nums_array.index(eighth_num))
rest = rest-((rest//two_fact)*two_fact)

permutation = str(first_num) + str(second_num) + str(third_num) + str(fourth_num) + str(fivth_num) + str(sixth_num) + str(seventh_num) + str(eighth_num) + str(nums_array[0]) + str(nums_array[1])
print(permutation)