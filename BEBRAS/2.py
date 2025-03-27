list = input().split(", ")

size = len(list)

total = 0

for i in range(1, size):
  current_sum = 0
  for j in range(i, size):
    current_sum = int(current_sum) + int(list[j])
    total = max(total, current_sum)

print(total)