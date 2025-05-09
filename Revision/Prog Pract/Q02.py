# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
goalsScored = []
winPercentage = []
teams = []
FILE = 'sportsdata.txt'
total_goals = 0
total_percentge = 0

hiGoals = 0
hiGoalsTeam = ''

hiWinPerc = 0.0
hiWinPercTeam = ''

hiComp = 0.0
hiCompTeam = ''

formatting = ('{:<20s} | {:^12} | {:>16}')
number_formatting = ('{:<20s} | {:^12} | {:>11.1f}')
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
sportsdata = open(FILE, 'r')

for line in sportsdata:
    tempTeam = line.strip().split(',')
    teams.append(tempTeam[0])
    goalsScored.append(int(tempTeam[1]))
    winPercentage.append(float(tempTeam[2]))
    total_goals = total_goals + int(tempTeam[1])
    total_percentge = total_percentge + float(tempTeam[2])

for j in range(len(teams)):
    if goalsScored[j] > hiGoals:
        hiGoals = goalsScored[j]
        hiGoalsTeam = teams[j]

    if winPercentage[j] > hiWinPerc:
        hiWinPerc = winPercentage[j]
        hiWinPercTeam = teams[j]

    teamCompScore = goalsScored[j] * 1 + winPercentage[j] * 2

    if teamCompScore > hiComp:
        hiComp = teamCompScore
        hiCompTeam = teams[j]

print(formatting.format('Team Name', 'Goals Scored', 'Win Percentage'))
print('-'*57)

for _ in range(len(teams)):
    printing = number_formatting.format(teams[_], goalsScored[_], winPercentage[_])
    print(printing)

print('='*57)
print(number_formatting.format('Total', total_goals, total_percentge))

print('Team with most goals scored is', hiGoalsTeam,'with', hiGoals,'scored.')
print('Team with highest win percentage is', hiWinPercTeam,'with', hiWinPerc,'percent.')
print('Team with highest composite score is', hiCompTeam,'with', hiComp,'scored.')