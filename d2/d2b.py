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

    if opp == 'A': # ROCK
        if outcome == 'X':   # LOSE
            play = 'Z'
        elif outcome == 'Y': # DRAW
            play = 'X'
        elif outcome == 'Z': # WIN
            play = 'Y'
        else:
            bad_data(round)

    elif opp == 'B': # PAPER
        if outcome == 'X':   # LOSE
            play = 'X'
        elif outcome == 'Y': # DRAW
            play = 'Y'
        elif outcome == 'Z': # WIN
            play = 'Z'
        else:
            bad_data(round)

    elif opp == 'C': # SCISSORS
        if outcome == 'X':   # LOSE
            play = 'Y'
        elif outcome == 'Y': # DRAW
            play = 'Z'
        elif outcome == 'Z': # WIN
            play = 'X'
        else:
            bad_data(round)
    
    else:
        bad_data(round)
    
    return play

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
