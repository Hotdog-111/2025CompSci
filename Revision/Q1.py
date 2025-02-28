# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
import time

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
colours = ["Red", "Red and Amber", "Green", "Amber"]
cycles = 0
waitTime = 1                # One second

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

while (cycles < 3):         # Three times around
    print ("Cycle " + str (cycles))

    # Show all the lights in sequence
    for index in range (len (colours)):
        print (colours[index])
        print ("...")
        time.sleep (waitTime)

    cycles = cycles + 1

print ("Finished")

# -------------------------------------------------------------------
# =====> Type your answers here in the right-hand column
# Left                                          # Right
# -------------------------------------------------------------------
# Name of a library used in this program        # time
# Name of an array used in this program         # colours
# Line number of a variable initialisation      # 10
# Line number of a repetition                   # 17
# Name of a data type conversion function
#     used in this program                      #str()
# Name of a built-in subprogram used
#     on line 21                                # len()
# An arithmetic operator used
#     in this program                           # +


