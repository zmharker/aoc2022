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
    play_scores = {'X':1, 'Y':2, 'Z':3}
    win_scores =  {'X':0, 'Y':3, 'Z':6}
    
    return(play_scores[play] + win_scores[round[2]])
    


with open('input.txt','r') as input:
    rounds = [a.strip() for a in input.readlines()]
    total_score = 0
    for round in rounds:
        total_score += score(round)
    print(f'total score: {total_score}')
