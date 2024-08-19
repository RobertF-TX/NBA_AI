from nba_api.stats.endpoints import PlayerGameLogs

# Create an instance of the PlayerGameLogs class
game_logs = PlayerGameLogs(
    player_id_nullable='1629029',  # Use 'player_id_nullable' instead of 'player_id'
    season_nullable='2023-24', 
    last_n_games_nullable=50  # Use 'last_n_games_nullable' instead of 'last_n_games'
)

# Make the API request
game_logs_data = game_logs.get_data_frames()[0]

# Extract points scored in the last 50 games
points_last_50_games = game_logs_data['PTS'].tolist()

# Print the points scored in the last 50 games
print("Points scored in the last 50 games:", points_last_50_games)

