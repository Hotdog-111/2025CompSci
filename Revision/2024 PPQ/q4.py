# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
import math
from sys import orig_argv
from wsgiref.validate import check_status

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
CHEESE_PER_ADULT = 40       # Grams
CHEESE_PER_CHILD = 30       # Grams
MIN_CHEESE = 500            # 500 grams in a pack

ROLLS_PER_ADULT = 1.5       # Count
ROLLS_PER_CHILD = 0.5       # Count
MIN_ROLLS = 24              # Count of rolls in a pack

CRISPS_PER_ADULT = 0.75     # Of a bag
CRISPS_PER_CHILD = 0.33     # Of a bag

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------

# =====> Write your code here
children = int(input())
adults = int(input())

def crisps():
    partialBagsOfCrisps = (adults * CRISPS_PER_ADULT) + (children * CRISPS_PER_CHILD)

    print(partialBagsOfCrisps)

    bagsOfCrisps = math.ceil(partialBagsOfCrisps)

    print(bagsOfCrisps)

def cheese():
    partialCheese = (adults * CHEESE_PER_ADULT) + (children * CHEESE_PER_CHILD)


    if partialCheese <= MIN_CHEESE:
        print('order one pack of cheese')
    else:
        cheese = math.ceil(partialCheese)
        packsOfCheese = math.ceil(cheese / 500)
        print(packsOfCheese)

def rolls():
    partialRolls = (adults * ROLLS_PER_ADULT) + (children * ROLLS_PER_CHILD)

    print(partialRolls)

    rolls = math.ceil(partialRolls)

    if rolls <= MIN_ROLLS:
        print('order one pack of rolls')
    else:
        packs = math.ceil(rolls / 24) * 24
        print(packs)
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Write your code here

crisps()
cheese()
rolls()


