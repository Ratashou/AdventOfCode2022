file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2022\Day1.txt", "r")

caloriesList = []
totalCalories = 0
for calories in file:
    if calories == '\n':
        caloriesList.append(totalCalories)
        totalCalories = 0
    else:
        totalCalories += int(calories)

caloriesList.sort(reverse=True)

totalCalories = caloriesList[0] + caloriesList[1] + caloriesList[2]
print(totalCalories)

file.close()
