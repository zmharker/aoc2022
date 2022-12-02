# A = opponent Rock
# B = opponent Paper
# C = opponent Scissors

# X = play Rock     (+1)
# Y = play Paper    (+2)
# Z = play Scissors (+3)

# loss +0
# win  +6
# draw +3

def bad_data(round):
    print(f'error in round data: {round}')

def score(round):
    play = round[2]
    opp = round[0]
    if play == 'X':
        play_score = 1
    elif play == 'Y':
        play_score = 2
    elif play == 'Z':
        play_score = 3
    else:
        bad_data(round)

    if opp == 'A':
        if play == 'X':
            win_score = 3
        elif play == 'Y':
            win_score = 6
        elif play == 'Z':
            win_score = 0
        else:
            bad_data(round)
    
    elif opp == 'B':
        if play == 'X':
            win_score = 0
        elif play == 'Y':
            win_score = 3
        elif play == 'Z':
            win_score = 6
        else:
            bad_data(round)
    
    elif opp == 'C':
        if play == 'X':
            win_score = 6
        elif play == 'Y':
            win_score = 0
        elif play == 'Z':
            win_score = 3
        else:
            bad_data(round)
    
    return(play_score + win_score)
    


with open('input.txt','r') as input:
    rounds = [a.strip() for a in input.readlines()]
    total_score = 0
    for round in rounds:
        total_score += score(round)
    print(f'total score: {total_score}')
