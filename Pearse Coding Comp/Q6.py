
grid = [[f"{i:02d}" for i in range(j * 10, (j + 1) * 10)] for j in range(10)]

n = int(input().strip())

for i in range(n):
    instruction = input().strip()

    if instruction.startswith('r'):
        range_str = instruction[1:]
        A, B = map(int, range_str.split('-'))
        grid = [row for i, row in enumerate(grid) if i < A or i > B]

    elif instruction.startswith('c'):
        range_str = instruction[1:]
        A, B = map(int, range_str.split('-'))
        grid = [row[:A] + row[B + 1:] for row in grid]

for row in grid:
    print(" ".join(row))