file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2022\Day4.txt", "r")

totalOverlaps = 0
for line in file:
    #Creates list containing first assignment and second assignment
    assignments = line.split(',')

    #Splits the assignments in to two variables
    firstAssignment = assignments[0].split('-')
    secondAssignment = assignments[1].split('-')

    #Removes the /n at the end of the second list item
    firstAssignment[1] = firstAssignment[1].strip('\n')
    secondAssignment[1] = secondAssignment[1].strip('\n')
    
    if int(secondAssignment[0]) >= int(firstAssignment[0]) and int(secondAssignment[0]) <= int(firstAssignment[1]):
        totalOverlaps += 1

    elif int(secondAssignment[1]) >= int(firstAssignment[0]) and int(secondAssignment[1]) <= int(firstAssignment[1]):
        totalOverlaps += 1

    elif int(firstAssignment[0]) >= int(secondAssignment[0]) and int(firstAssignment[0]) <= int(secondAssignment[1]):
        totalOverlaps += 1

    elif int(firstAssignment[1]) >= int(secondAssignment[0]) and int(firstAssignment[1]) <= int(secondAssignment[1]):
        totalOverlaps += 1


print(totalOverlaps)

file.close()
