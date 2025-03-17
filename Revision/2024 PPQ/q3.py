# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
PURCHASE_TYPE_ITEM = 1
PURCHASE_TYPE_WEIGHT = 5

PRICE_PER_KILOGRAM = 3.45
PRICE_PER_ITEM = 1.23

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
weight = 0.0
count = 0
totalCost = 0.0

# =====> Create an integer variable named purchaseType and set it to 0
purchaseType = 0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
purchaseType = int (input ("Enter a purchase type (1 or 5) "))

# =====> Complete the line with the correct logical operator and the correct constant
if ((purchaseType != PURCHASE_TYPE_ITEM) and (purchaseType != PURCHASE_TYPE_WEIGHT)):
    print ("Invalid purchase type")

# =====> Complete the line with the correct constant
elif (purchaseType == PURCHASE_TYPE_WEIGHT):

    # =====> Complete the line to accept a real value for the weight in kilograms
    weight = float(input ("Enter weight in kilograms "))
    if (weight <= 0):
        print ("Invalid weight")
    else:
        # =====> Complete the line to calculate the total cost based on weight
        totalCost = weight * PRICE_PER_KILOGRAM
else:
    count = int (input ("Enter count of items "))
    # =====> Complete the line to check for a 0 or negative count of items
    if (count <= 0):
        print ("Invalid number of items")
    else:
        totalCost = count * PRICE_PER_ITEM

# =====> Complete the line with the correct relational operator
if (totalCost != 0.0):

    # =====> Add a line to display an informative message and the total cost
    print('Total cost is', totalCost)

