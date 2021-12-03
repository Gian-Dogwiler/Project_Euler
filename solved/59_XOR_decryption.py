ascii_file = open('files/p059_cipher.txt','r')
ascii_file = ascii_file.read()
ascii_file = str(ascii_file)
ascii_file = ascii_file.replace(',',' ')
ascii_arr = ascii_file.split()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text_len = len(ascii_arr)
password_iteration = int(text_len / 3) # 485
sum = 0

for char1 in alphabet:
    for char2 in alphabet:
        for char3 in alphabet:

            pass_counter = 0
            password = [ord(char1),ord(char2),ord(char3)]
            decrypted_arr = []
            text = ''
            
            for char in ascii_arr:
                decrypted = int(char) ^ int(password[pass_counter])
                decrypted_arr.append(decrypted)
                pass_counter += 1
                if pass_counter == 3:
                    pass_counter = 0
            
            for ascii in decrypted_arr:
                char = chr(ascii)
                text += char
            
            print(text)
            if ' the ' in text:
                right_decryption = input('is this the right text? [y/n]: ')
                if right_decryption == 'y':
                    for num in decrypted_arr:
                        sum += num
                    print('Total sum: ', str(sum))

print(sum)