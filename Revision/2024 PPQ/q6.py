# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
cowTable = []

# =====> Write your code here
with open("Cows.txt", "r") as file: #opens file
    for line in file: #loop

        name, breed, tag = line.strip().split(",") # separates out each individual section via a comma

        tag = int(tag) # converts string to int

        key = breed[:2] + str(tag // 100) + name[:2] #sets the key that is used for the cow data

        record = (key, tag, name, breed) # creates the recoerd, ready to be stored in list

        cowTable.append(record) # adds it to the list
# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
def showTable (pTable):
    for cow in pTable:
        print (cow)

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here

showTable(cowTable)

