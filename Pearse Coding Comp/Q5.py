score1 = 0
score2 = 0

last_wand_winner = None

winning_combinations = {
    ('R', 'S'): 1,  # Rock beats Scissors
    ('S', 'P'): 1,  # Scissors beats Paper
    ('P', 'R'): 1,  # Paper beats Rock
    ('W', 'R'): 1,  # Wand beats Rock
    ('W', 'S'): 1,  # Wand beats Scissors
    ('W', 'P'): 1,  # Wand beats Paper
    ('S', 'R'): 2,  # Scissors loses to Rock
    ('P', 'S'): 2,  # Paper loses to Scissors
    ('R', 'P'): 2,  # Rock loses to Paper
    ('R', 'W'): 2,  # Rock loses to Wand
    ('S', 'W'): 2,  # Scissors loses to Wand
    ('P', 'W'): 2  # Paper loses to Wand
}

# Process each round
for i in range(6):
    p1, p2 = input().strip()

    if p1 == p2:
        if p1 == 'W' and p2 == 'W' and last_wand_winner is not None:
            if last_wand_winner == 1:
                score1 = 0
            elif last_wand_winner == 2:
                score2 = 0
        continue

    if (p1, p2) in winning_combinations:
        winner = winning_combinations[(p1, p2)]
    else:
        winner = winning_combinations[(p2, p1)]

    if winner == 1:
        score1 += 1
        if p1 == 'W':
            last_wand_winner = 1
    elif winner == 2:
        score2 += 1
        if p2 == 'W':
            last_wand_winner = 2

print(f"{score1}-{score2}")