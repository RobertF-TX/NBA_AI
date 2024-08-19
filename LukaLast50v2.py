from nba_api.stats.endpoints import PlayerGameLogs
import pandas as pd

# Create an instance of the PlayerGameLogs class
game_logs = PlayerGameLogs(
    player_id_nullable='1629029',
    season_nullable='2023-24',
    last_n_games_nullable=50
)

# Make the API request
game_logs_data = game_logs.get_data_frames()[0]

# Extract points scored and minutes played in the last 50 games
points_last_50_games = game_logs_data['PTS'].tolist()
minutes_last_50_games = game_logs_data['MIN'].tolist()

# Create a DataFrame to display the data in a table format
df = pd.DataFrame({
    'Game': range(1, len(points_last_50_games) + 1),
    'Points': points_last_50_games,
    'Minutes': minutes_last_50_games
})

# Display the DataFrame
print(df)

