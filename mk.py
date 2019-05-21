import numpy as np

'''
    Mario Kart - War Points Counter
    Author: David García Fernández
    Date: 21/5/2019
'''

# Points earned depending on the position (from first to last)
weights_12p = np.array([15, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) # 12 players
weights_10p = [] # 10 players

# Total points per race
total_12p = sum(weights_12p)
total_10p = sum(weights_10p)

def race_points(team_pos, ten_p=False):
    
    p_player = 0
    p_rival = 0

    n_players = 10 if ten_p else 12
    positions = np.zeros(n_players)

    for i in range(n_players):
        if i+1 in team_pos:
            positions[i] = 1

    if ten_p:
        p_player = np.dot(weights_10p, positions)
        p_rival = total_10p - p_player
    else:
        p_player = np.dot(weights_12p, positions)
        p_rival = total_12p - p_player
    
    return p_player, p_rival
