# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
numYears = 0 #
theYear = 1900

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

numYears = int(input("How many years do you want? ")) ##

for count in range(numYears):#
    theYear = int(input("Enter a year: "))#

    if (theYear % 400 == 0) and (theYear % 100 == 0):#
        print(theYear, "is a leap year")
    elif (theYear % 4 == 0) and (theYear % 100 != 0):#
        print (theYear, "is a leap year")
    else:#
        print (theYear, "is not a leap year")#

print("Goodbye")##
