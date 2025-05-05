import pandas as pd
import numpy as np

# Sample data for player statistics in the last 5 games
data = {
    'Player': ['Shai Gilgeous-Alexander', 'Stephen Curry', 'Nikola Jokic', 'Jalen Brunson', 'Jayson Tatum', 'Anthony Edwards'],
    'Points_Game_1': [38, 22, 16, 40, 35, 15],
    'Points_Game_2': [31, 29, 25, 16, 37, 43],
    'Points_Game_3': [27, 13, 13, 32, 36, 29],
    'Points_Game_4': [15, 17, 36, 30, 17, 25],
    'Points_Game_5': [42, 36, 23, 37, 16, 22],
    'Assists_Game_1': [6, 7, 8, 7, 10, 8],
    'Assists_Game_2': [8, 2, 8, 7, 3, 6],
    'Assists_Game_3': [5, 7, 12,11, 4, 8],
    'Assists_Game_4': [5, 3, 8, 9, 4, 0],
    'Assists_Game_5': [6, 9, 13, 7, 8, 9],
    'Rebounds_Game_1': [5, 10, 10, 4, 8, 11],
    'Rebounds_Game_2': [4, 7, 7, 3, 14, 9],
    'Rebounds_Game_3': [8, 3, 10, 5, 9, 8],
    'Rebounds_Game_4': [3, 3, 21, 7, 14, 6],
    'Rebounds_Game_5': [6, 7, 13, 3, 8, 8],
    'Blocks_Game_1': [1, 2, 1, 0, 0, 0],
    'Blocks_Game_2': [1, 1, 1, 0, 0, 1],
    'Blocks_Game_3': [0, 0, 2, 1, 1, 1],
    'Blocks_Game_4': [2, 0, 1, 1, 1, 0],
    'Blocks_Game_5': [1, 2, 0, 0, 0, 0],
    'Steals_Game_1': [2, 2, 3, 0, 1, 3],
    'Steals_Game_2': [1, 2, 3, 0, 3, 0],
    'Steals_Game_3': [2, 0, 1, 0, 1, 2],
    'Steals_Game_4': [0, 1, 2, 0, 1, 0],
    'Steals_Game_5': [0, 1, 1, 2, 0, 1],
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Calculate average points, assists, rebounds, blocks, and steals over the last 5 games
df['Avg_Points'] = df[['Points_Game_1', 'Points_Game_2', 'Points_Game_3', 'Points_Game_4', 'Points_Game_5']].mean(axis=1)
df['Avg_Assists'] = df[['Assists_Game_1', 'Assists_Game_2', 'Assists_Game_3', 'Assists_Game_4', 'Assists_Game_5']].mean(axis=1)
df['Avg_Rebounds'] = df[['Rebounds_Game_1', 'Rebounds_Game_2', 'Rebounds_Game_3', 'Rebounds_Game_4', 'Rebounds_Game_5']].mean(axis=1)
df['Avg_Blocks'] = df[['Blocks_Game_1', 'Blocks_Game_2', 'Blocks_Game_3', 'Blocks_Game_4', 'Blocks_Game_5']].mean(axis=1)
df['Avg_Steals'] = df[['Steals_Game_1', 'Steals_Game_2', 'Steals_Game_3', 'Steals_Game_4', 'Steals_Game_5']].mean(axis=1)

# Function to predict over/under based on recent performance
def predict_over_under(player, points_line, assists_line, rebounds_line, blocks_line, steals_line):
    # Get the player's stats
    player_data = df[df['Player'] == player]
    avg_points = player_data['Avg_Points'].values[0]
    avg_assists = player_data['Avg_Assists'].values[0]
    avg_rebounds = player_data['Avg_Rebounds'].values[0]
    avg_blocks = player_data['Avg_Blocks'].values[0]
    avg_steals = player_data['Avg_Steals'].values[0]

    # Predict points over/under
    if avg_points > points_line:
        points_prediction = 'Over'
    else:
        points_prediction = 'Under'

    # Predict assists over/under
    if avg_assists > assists_line:
        assists_prediction = 'Over'
    else:
        assists_prediction = 'Under'

    # Predict rebounds over/under
    if avg_rebounds > rebounds_line:
        rebounds_prediction = 'Over'
    else:
        rebounds_prediction = 'Under'

    # Predict blocks over/under
    if avg_blocks > blocks_line:
        blocks_prediction = 'Over'
    else:
        blocks_prediction = 'Under'

    # Predict steals over/under
    if avg_steals > steals_line:
        steals_prediction = 'Over'
    else:
        steals_prediction = 'Under'

    return points_prediction, assists_prediction, rebounds_prediction, blocks_prediction, steals_prediction

# Example of predicting for a player with specific lines
player_name = input("Enter player name (Shai Gilgeous-Alexander, Stephen Curry, Jalen Brunson, Nikola Jokic, Jayson Tatum, Anthony Edwards): ")
points_line = float(input(f"Enter points line for {player_name}: "))
assists_line = float(input(f"Enter assists line for {player_name}: "))
rebounds_line = float(input(f"Enter rebounds line for {player_name}: "))
blocks_line = float(input(f"Enter blocks line for {player_name}: "))
steals_line = float(input(f"Enter steals line for {player_name}: "))

# Call the function
points_pred, assists_pred, rebounds_pred, blocks_pred, steals_pred = predict_over_under(
    player_name, points_line, assists_line, rebounds_line, blocks_line, steals_line
)

print(f"Prediction for {player_name}:")
print(f"Points: {points_pred}")
print(f"Assists: {assists_pred}")
print(f"Rebounds: {rebounds_pred}")
print(f"Blocks: {blocks_pred}")
print(f"Steals: {steals_pred}")
