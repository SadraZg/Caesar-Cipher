alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cipherText = input("Enter your cipher text to decrypt\n").lower()


def decrypt(shift):
    plain = ""
    for letter in cipherText:

        if letter == " ":
            plain += " "
        else:
            ind = alphabet.index(letter)
            ind -= shift
            if ind < 0:
                ind += 26
            plain += alphabet[ind]
    return plain.upper()


operation = input("Do you know the key? Enter 1 for YES, 0 for No.\n")

if operation == "1":

    shiftValue = int(input("Enter the cipher key(shift value)\n"))
    if not 0 < shiftValue < 25:
        print("The key must be a number between 0 and 25!")
        raise ValueError

    plainText = decrypt(shiftValue)
    print(plainText)

elif operation == "0":

    for i in range(26):
        candid = decrypt(i)
        print("KEY=", i, " ---> ", candid)

else:
    print("You should enter either 1 or 0!")
    raise ValueError
