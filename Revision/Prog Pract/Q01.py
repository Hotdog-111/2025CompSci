# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
RESULTS_FILE = "spellingResults.txt"

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
record = []
minAverage = 10
maxAverage = 0
minStudent = ''
maxStudent = ''
# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
def highAverage(record):
    for _ in range(len(record)):
        if _ > maxAverage:
            maxAverage = _
        elif _ <= minAverage:
            minAverage = _

def average(record):
    for p in range(len(record)):
        sum = 0
        average = 0
        student = ''
        for l in range(len(record[p])):
            sum = record[p]
            average += sum / record[p][l]

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
results = open(RESULTS_FILE, 'r')

for i in results:
    studentResults = i.strip().split(',')
    for j in range(20):