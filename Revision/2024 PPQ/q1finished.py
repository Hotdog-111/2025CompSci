# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
rainbow = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]
waveTable = [380, 425, 450, 492, 577, 597, 622]
found = False
index = 0
wavelength = 123
colour = ""

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# User chooses a colour index
index = int (input ("Enter an index: "))
if (index < 0):
    print ("Indexes cannot be zero")
elif (index > 6):
    print ("Indexes cannot be more than six")
else:
    colour = rainbow[index]
    print (str (colour))

# User chooses a colour based on wavelength
wavelength = int (input ("Enter a wavelength "))
if ((wavelength < 380) or (wavelength > 622)):
    print ("Invalid wavelength")
else:
    index = 0
    # Look for a wavelength less than or equal to user's choice
    while (not found):
        if (wavelength == waveTable[index]):
            found = True
            print (rainbow[index])
        elif (waveTable[index] >= wavelength):
            found = True
            print (rainbow[index - 1])
        else:
            index = index + 1


