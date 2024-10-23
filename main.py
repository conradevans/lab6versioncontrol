def encode(password):
#Conrad Evans, Lab 6 - Group 50
    encode = list(password)
    encoded_password = ''
    for i in range(len(encode)):
        encode[i] = int(encode[i]) + 3
    for j in range(len(encode)):
        encoded_password += str(encode[j])
    return encoded_password


def decode(encoded_password):
    pass

def menu():
    print('\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit')

def main():
    while True:
        menu()
        menu_selection = int(input('\nPlease enter an option: '))
        if menu_selection == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        elif menu_selection == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
        elif menu_selection == 3:
            break

if __name__ == '__main__':
    main()

