all_calories = []
n = []

f = open("data/day1.in", "r")

for x in f:
  if x != '\n':
    n.append(int(x))
  else:
    all_calories.append(n)
    n = []

total_calories = [sum(item) for item in all_calories]

print(sorted(total_calories))

print(max(total_calories))

top3 = sorted(total_calories)[-3:]
print("top3: ", top3)
print("sum of top3 = ", sum(top3))