# A = opponent Rock
# B = opponent Paper
# C = opponent Scissors

# X = play Rock     (+1) LOSE
# Y = play Paper    (+2) DRAW
# Z = play Scissors (+3) WIN

# loss +0
# win  +6
# draw +3

def bad_data(round):
    print(f'error in round data: {round}')

def what_to_play(round):
    opp = round[0]
    outcome = round[2]

    opp_offsets = {'A':0, 'B':1, 'C':2}
    outcome_index = {'X': 0, 'Y': 1, 'Z': 2}
    plays = ['Z','X','Y']
    play_index = (outcome_index[outcome] + opp_offsets[opp]) % 3
    return plays[play_index]

def score(round):
    play = what_to_play(round)
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
