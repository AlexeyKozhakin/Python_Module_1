alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v' , 'w', 'x', 'y', 'z']

inv_alphabet = alphabet[::-1]


message = input()

out_message = ''
for letter in message:
    if letter.lower() in alphabet:
        i = alphabet.index(letter.lower())
        out_message += inv_alphabet[i]
    else:
        out_message += letter

print(out_message)