def calc_average(scores):
    return sum(scores) / len(scores)

with open("spellingResults.txt", 'r') as file:
    lines = file.readlines()


studentData = []
for line in lines:
    parts = line.strip().split(',')
    name = parts[0]
    scores = list(map(int, parts[1:]))
    studentData.append([name] + scores)

averages = []
print("Pupil Averages:")
for record in studentData:
    name = record[0]
    scores = record[1:]
    avg = calc_average(scores)
    averages.append((name, avg))
    print(f'{name}: {avg:.2f}')

highest = max(averages, key=lambda x: x[1])
lowest = min(averages, key=lambda x: x[1])

print(f'Highest scoring pupil: {highest[0]}, with an average of {highest[1]}')
print(f'Lowest scoring pupil: {lowest[0]}, with an average of {lowest[1]}')

with open('results.txt', 'w') as outfile:
    for name, avg in averages:
        outfile.write(f'{name}: {avg:.2f}\n')