file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2022\Day2.txt", "r")

score = 0
for game in file:
    #A is Rock, B is Paper, C is Scissors
    #X is Lose (worth 0), Y is Tie (worth 3), Z is Win (worth 6)
    #Rock is 1, Paper is 2, Scissors is 3
    match game[0]:
        case 'A':
            match game[2]:
                #Lose Scissors
                case 'X':
                    score += 3
                #Tie Rock
                case 'Y':
                    score += 4
                #Win Paper
                case 'Z':
                    score += 8

        case 'B':
            match game[2]:
                #Lose Rock
                case 'X':
                    score += 1
                #Tie Paper
                case 'Y':
                    score += 5
                #Win Scissors
                case 'Z':
                    score += 9

        case 'C':
            match game[2]:
                #Lose Paper
                case 'X':
                    score += 2
                #Tie Scissors
                case 'Y':
                    score += 6
                #Win Rock
                case 'Z':
                    score += 7

print(score)

file.close()
