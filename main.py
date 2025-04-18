import pandas as pd
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from sklearn.linear_model import LinearRegression
import time

# Function to find a player ID
def get_player_id(player_name):
    player_dict = players.find_players_by_full_name(player_name)
    if player_dict:
        return player_dict[0]["id"]
    else:
        raise ValueError("Player not found!")

# Fetch recent games
def fetch_player_stats(player_id, season='2023-24'):
    time.sleep(0.6)  # prevent rate limit
    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season, season_type_all_star='Regular Season')
    df = gamelog.get_data_frames()[0]
    return df.head(10)  # Last 10 games

# Get player ID
player_name = "Stephen Curry"  # change this to any player
player_id = get_player_id(player_name)
df = fetch_player_stats(player_id)

# Select and rename features
df = df[["MIN", "FGA", "FGM", "FG3A", "FG3M", "PTS"]]
df.columns = ["minutes", "fg_attempts", "fg_made", "three_pa", "three_pm", "points"]
df = df.astype(float)

# Prepare model
X = df[["minutes", "fg_attempts", "fg_made", "three_pa", "three_pm"]]
y = df["points"]

model = LinearRegression()
model.fit(X, y)

# Predict next game
latest_game = df.iloc[0]
input_data = pd.DataFrame([{
    "minutes": latest_game["minutes"],
    "fg_attempts": latest_game["fg_attempts"],
    "fg_made": latest_game["fg_made"],
    "three_pa": latest_game["three_pa"],
    "three_pm": latest_game["three_pm"]
}])

predicted_points = model.predict(input_data)[0]
print(f"Predicted points for {player_name}'s next game: {predicted_points:.2f}")
