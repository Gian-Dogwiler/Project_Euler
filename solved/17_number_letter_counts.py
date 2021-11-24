word_dict = {0: '', 1: 'one', 2: 'two', 3: 'three', 4:'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}
letters_sum = 0
for num in range(1,1001):
    len_nums = 0
    str_num = str(num)
    if len(str_num) == 4:
        len_nums = len(word_dict[1]) + len(word_dict[1000])
    elif len(str_num) == 3:
        if (int(str_num[1]+str_num[2])<20):
            len_nums += len(word_dict[(int(str_num[1]+str_num[2]))])
        else:
            len_nums += len(word_dict[int(str_num[2])])
            len_nums += len(word_dict[int(str_num[1])*10])
        len_nums += len(word_dict[int(str_num[0])]) + len(word_dict[100]) + len('and')
        if int(str_num) % 100 == 0:
            len_nums = len(word_dict[int(str_num[0])]) + len(word_dict[100])
    elif len(str_num) == 2:
        if (int(str_num[0]+str_num[1])<20):
            len_nums += len(word_dict[(int(str_num[0]+str_num[1]))])
        else:
            len_nums += len(word_dict[(int(str_num[1]))])
            len_nums += len(word_dict[int(str_num[0])*10])
    else:
        len_nums += len(word_dict[int(str_num[0])])
    
    letters_sum += len_nums

print(letters_sum)