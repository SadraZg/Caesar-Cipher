alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

plainText = input("Enter your message to get encrypted\n")
shift_value = int(input("Enter your cipher key (It should be a number between 0 and 25)\n"))

if not 0 < shift_value < 25:
    print("You should enter a number between 0 and 25")
    raise ValueError


def encrypt(shift):

    cipherText = ""
    for letter in plainText.lower():

        if letter == " ":
            cipherText += " "

        else:
            ind = alphabet.index(letter)
            if ind + shift < 25:
                ind += shift
            else:
                ind += shift - 26
            cipherText += alphabet[ind]

    print(cipherText.upper())


encrypt(shift_value)
