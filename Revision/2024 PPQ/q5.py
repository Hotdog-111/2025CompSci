# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
import random

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
GET = 1
ADD = 2
SHOW = 3
EXIT = 4

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
pastaShapes = ["Bigoli", "Strozzapreti", "Trofie", "Gigli", "Chitarra",
               "Penne", "Orecchiette", "Tagliatelle", "Chonchiglie",
               "Fusilli"]

shape = ""
choice = 0

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# Get a menu item from the user
def getChoice ():
    # =====> Write your code here

    print ("1 - get a shape")
    print ("2 - add a shape")
    print ("3 - show the shapes")
    print ("4 - exit program")

    # =====> Write your code here
    choice = int(input())
    return choice

# Display all the shapes
def showShapes (pTable):
    for pasta in pTable:
        print (pasta)

# Get a random shape
def getShape (pTable):
    # =====> Write your code here
    index = random.randint(0,9)
    print(pTable[index])


# Add a shape
def addShape (pTable):
    # =====> Write your code here
    newShape = input()
    pTable.append(newShape)

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
end = False
choice = getChoice ()
# =====> Write your code here
while end == False:
    if choice == 1:
        getShape(pastaShapes)
        choice = getChoice()
    elif choice == 2:
        addShape(pastaShapes)
        choice = getChoice()
    elif choice == 3:
        showShapes(pastaShapes)
        choice = getChoice()
    elif choice == 4:
        exit()



