names_file = open('../files/p022_names.txt','r')
names_file = names_file.read()
names_str = str(names_file)
names_str = names_str.replace(',',' ')
names_str = names_str.replace('"','')
names_arr = names_str.split()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
total_score = 0
sorted_names = sorted(names_arr)

for name in names_arr:
    score = 0
    for char in name:
        char = char.lower()
        score += alphabet.index(char) + 1
    score = score * (sorted_names.index(name) + 1)
    total_score += score

print(total_score)