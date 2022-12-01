file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2022\Day1.txt", "r")

mostCalories = 0
totalCalories = 0
for calories in file:
    if calories == '\n':
        if totalCalories > mostCalories:
            mostCalories = totalCalories

        totalCalories = 0
    else:
        totalCalories += int(calories)

print(mostCalories)
file.close()
