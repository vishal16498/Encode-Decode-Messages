alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']*2

def cipher_code(text, shift_value, num):
    final_word = ""
    if num == 1:
        shift_value *= -1
    for each in text:
        if each in alphabet:
            index_position = alphabet.index(each)
            new_position = index_position + shift_value
            new_alpha = alphabet[new_position]
            final_word += new_alpha
        else:
            final_word += each
    if num == 1:
        print(f"The decoded word is {final_word}")
    else:
        print(f"The encoded word is {final_word}")



continue_ = True

while continue_:
    type_of_coding = int(input("Enter 1 for encode or 2 for decode: "))
    if type_of_coding == 1:
        user_input = input("Type your message to be encoded: ").lower()
        shift = int(input("Enter the number shift for encoding: "))
    else:
        user_input = input("Type your message to be decoded: ").lower()
        shift = int(input("Enter the number shift for decoding: "))
    shift = shift % 26

    cipher_code(num=type_of_coding, text=user_input, shift_value=shift)

    play_again = input("Do you want to continue Yes/No: ").lower()
    if play_again == "no":
        continue_ = False
        print("Cheers")
