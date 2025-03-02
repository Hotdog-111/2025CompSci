# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
MILE_KILOMETRE = 1.6093         # One mile = 1.6093 kilometre
INCH_CENTIMETRE = 2.54          # One inch = 2.54 centimetres

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
myChoice = -9
miles = 0.0
kilometres = 0.0
inches = 0.0
centimetres = 0.0

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------

# =====> Choose the correct subprogram definition header
def showMenu ():
#def showMenu (kilometres):
#def showMenu (pMiles):
#def showMenu (pMiles, pKilometres):

    print ("==============================")
    print ("1 - Miles to kilometres")
    print ("2 - Inches to centimetres")
    print ("9 - Exit")

def getMenuChoice ():
    choiceStr = ""
    # =====> Add a line to create a local variable named choiceStr
    #        and set it to an empty string

    choiceInt = 0
    # =====> Add a line to create a local variable named choiceInt
    #        and set it to 0


    error = True

    # =====> Choose the correct line to display the menu
    #choiceStr = showMenu()
    showMenu ()
    #showMenu (choiceInt)
    #choiceInt = showMenu(choiceStr)

    while (error):
        # =====> Complete the line to take a string input
        choiceStr = str(input("Enter an option: "))

        # =====> Choose the correct line to validate the input
        if (not choiceStr.isdigit()):
        #if (choiceStr.isalnum()):
        #if (choiceStr.isalpha()):
        #if ("{:<8.2f}".format(choiceStr):
            error = True
        else:
            choiceInt = int (choiceStr)

            # =====> Choose the correct line to check the menu option
            #if ((choiceInt != 1) or (choiceInt != 2) or (choiceInt != 9)):
            #if ((choiceInt == 1) or (choiceInt == 2) or (choiceInt == 9)):
            if ((choiceInt != 1) and (choiceInt != 2) and (choiceInt != 9)):
            #if ((choiceInt == 1) and (choiceInt == 2) and (choiceInt == 9)):
                error = True
            else:
                error = False

        if (error):
            print ("Enter an option from the menu")


    return (choiceInt)

def milesToKilometres (pMiles):
    km = 0.0

    # =====> Choose the correct line to calculate kilometres
    #km = MILES_KILOMETRE / pMiles
    km = pMiles * MILE_KILOMETRE
    #km = MILES_KILOMETRE + pMiles
    #km = pMiles / MILE_KILOMETRE

    km = round (km, 4)

    # =====> Add a line to return the variable km to the caller
    return km

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

while (myChoice != 9):

    # =====> Choose the correct line to use a subprogram to get
    #        the user's menu option choice
    #getMenuChoice ()
    #getMenuChoice (miles)
    #kilometres = getMenuChoice (miles)
    myChoice = getMenuChoice ()

    # =====> Choose the correct line to direct the menu choice
    if (myChoice == 1):
    #if (myChoice == -9):
    #if (myChoice == 2):
    #if (myChoice == 9):
        print ("Going to change miles to kilometres")

        # =====> Complete the line to take a real number input
        #        and store it in the variable miles
        miles = float(input("Enter the number of miles: "))

        # =====> Choose the correct line to call the subprogram
        #milesToKilometres (miles)
        #milesToKilometres (kilometres)
        kilometres = milesToKilometres (miles)
        #miles = milesToKilometres (kilometres)

        # =====> Choose the line to display the correct output
        #print (miles + " miles is " + kilometres + " kilometres")
        #print (miles,  "kilometres", kilometres, "miles")
        print (str (miles) + " miles is " + str (kilometres) + " kilometres")
        #print (int (miles) + " miles is " + int (kilometres) + " kilometres")

    # =====> Choose the correct line to direct the menu choice
    #elif (myChoice == 1):
    #elif (myChoice == 9):
    #else:
    elif (myChoice == 2):
        print ("Going to change inches to centimetres (Not implemented yet)")

print ("Goodbye")

