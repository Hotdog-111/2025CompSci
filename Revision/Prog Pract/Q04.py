# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
letterScores = [
    ['A', 1], ['B', 3], ['C', 3], ['D', 2], ['E', 1],
    ['F', 4], ['G', 2], ['H', 4], ['I', 1], ['J', 8],
    ['K', 5], ['L', 1], ['M', 3], ['N', 1], ['O', 1],
    ['P', 3], ['Q', 10], ['R', 1], ['S', 1], ['T', 1],
    ['U', 1], ['V', 4], ['W', 4], ['X', 8], ['Y', 4],
    ['Z', 10]
]

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
scoreLog = [] # stores the words and scores as a 2D list e.g. [['QUIZ',22],['TEST',4]]
totalScore = 0 # stores the total score over the course of the game

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
prompt = ''
# =====> Create a loop: keep accepting words until 'quit game' is entered
while 'quit game' not in prompt:
    # =====> Inside the loop, prompt user for the word
    prompt = input("Enter a word: ").strip()
    # =====> Stop when "quit game" is entered
    if 'quit game' == prompt: break
    # =====> Otherwise process the word
    else:
        # =====> Convert the word to uppercase
        prompt = prompt.upper()
        # =====> Initialise a score variable
        score = 0
        # =====> Loop through each letter of the word
        for letter in range(len(prompt)):
            # =====> Calculate the letter score from the letterScores 2D list
            score += letterScores[letter][1]
        # =====> Output the word and it's score
        print(prompt, score)
        # =====> Store [word, score] in scoreLog
        scoreLog.append([prompt, score])
        # =====> Update the total score
        totalScore += score

# =====> After the game ends:

# =====> Output the total score
print("Total score:", totalScore)

# =====> APPEND all game data to a file called "scrabbleLog.txt"
log = open("scrabbleLog.txt", "a")
# =====> Use a loop to write each record from scoreLog to the file
for record in scoreLog:
    # =====> Each line in the file should follow the format: WORD,score
    log.write(record[0] + "," + str(record[1]) + "\n")

# =====> Close the file
log.close()

