exercise_time = input().split()
max_streak = 0
streak = 0
time = 0

for _ in exercise_time:
  if int(_) >= int(time):
    streak +=1
    time = _
  elif int(_) <= int(time):
    time = _
    max_streak = streak
    streak = 0

print(max_streak + 1)