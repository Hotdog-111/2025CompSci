# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
IN_FILE = "Q04_INPUT.TXT"
COMMA = ","
LF = "\n"

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
theFile = ""
data = []
total = 0.0
subtotal = 0.0
record = ""
fields = []

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# =====> Complete the line to open the file for reading
theFile = open("Q04_INPUT.txt", "r")

# =====> Complete the line to read every line from the file
for line in theFile:

    # =====> Complete the line to remove the line feed
    record = line.strip()

    # =====> Complete the line to separate the record into fields
    fields = record.split(",")

    # =====> Complete the line to display the flavour, the number
    #        in stock, and the cost of each item
    print (fields[0], fields[1], fields[2])

    # =====> Complete the line to calculate the total value
    #        of this item in stock
    subtotal = float(fields[1]) * float(fields[2])

    # =====> Complete the line to calculate the total value
    #        of all items in stock
    total = total + subtotal

# =====> Complete the line to display the variable total
#        formatted with a field width of 6 and a precision of 2
print("Total {:<6.2f}".format(total))


# =====> Complete the line to close the opened file
theFile.close()

