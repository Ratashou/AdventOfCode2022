file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2022\Day2.txt", "r")

score = 0
for game in file:
    #A is Rock, B is Paper, C is Scissors
    #X is Rock (worth 1), Y is Paper (worth 2), Z is Scissors (worth 3)
    match game[0]:
        case 'A':
            match game[2]:
                #Tie
                case 'X':
                    score += 4
                #Win
                case 'Y':
                    score += 8
                #Lose
                case 'Z':
                    score += 3

        case 'B':
            match game[2]:
                #Lose
                case 'X':
                    score += 1
                #Tie
                case 'Y':
                    score += 5
                #Win
                case 'Z':
                    score += 9

        case 'C':
            match game[2]:
                #Win
                case 'X':
                    score += 7
                #Lose
                case 'Y':
                    score += 2
                #Tie
                case 'Z':
                    score += 6

print(score)

file.close()
