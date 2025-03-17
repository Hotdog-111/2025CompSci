# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
plainText = ""
cipherText = ""
shift = 0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
plainText = input ("Enter a message: ")
shift = int (input ("Enter the shift: "))

for letter in plainText:

    # =====> Choose the correct line to check for alphabetic letters
    #if (letter.isalnum ()):
    #if (letter.islower ()):
    #if (letter.upper ()):
    if (letter.isalpha ()):

        value = ord (letter)
        value = value + shift

        # =====> Choose the correct line to check for upper case
        #if (letter.upper ()):
        #if (letter.isalpha ()):
        #if (letter.islower ()):
        if (letter.isupper ()):

            # =====> Choose the correct line to check if the letter is outside the alphabet
            if (value > ord ('Z')):
            #if (value >= ord ('Z')):
            #if (value < chr ('Z'')):
            #if (value < ord ('Z')):
                value = value - 26

            # =====> Choose the correct line to check if the letter is outside the alphabet
            #elif (value <= ord ('A')):
            #elif (value > chr ('A')):
            elif (value < ord ('A')):
            #elif (value > ord ('A')):

                value = value + 26

        # =====> Choose the correct line to check for lower case
        #elif (letter.lower ()):
        elif (letter.islower ()):
        #elif (letter.isupper ()):
        #elif (letter.isalpha ()):

            # =====> Choose the correct line to check if the letter is outside the alphabet
            #if (value >= chr ('z')):
            #if (value < ord ('z')):
            if (value > ord ('z')):
            #if (value <= chr ('z')):
                value = value - 26

            # =====> Choose the correct line to check if the letter is outside the alphabet
            elif (value < ord ('a')):
            #elif (value < chr ('z')):
            #elif (value != ord ('a')):
            #elif (value == chr ('z')):
                value = value + 26

        # =====> Choose the correct line to set the variable newLetter
        #newLetter = ord (value)
        newLetter = chr (value)
        #newLetter = ord (letter)
        #newLetter = chr (letter)

        # =====> Choose the correct line to create the encrypted string
        #cipherText = newLetter + cipherText
        #newLetter = cipherText + newLetter
        #newLetter = newLetter + cipherText
        cipherText = cipherText + newLetter

    else:
        # =====> Choose the correct line to create the encrypted string
        #cipherText = letter + cipherText
        cipherText = cipherText + letter
        #letter = cipherText + letter
        #letter = letter + cipherText

print ("Plain text: ", plainText)
print("Cipher text: ", cipherText)


