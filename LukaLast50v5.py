import pandas as pd
from nba_api.stats.endpoints import LeagueGameLog, TeamGameLogs

# Main function
def main():
    # Fetch Luka Doncic's points scored for the last 50 games
    luka_points = get_luka_points_last_50_games()
    if luka_points is None:
        return
    
    # Fetch Dallas Mavericks' team game log for the last 50 games
    mavericks_outcomes = get_mavericks_team_gamelog_last_50_games()
    if mavericks_outcomes is None:
        return
    
    # Merge Luka's points and Mavericks' outcomes based on the game date
    merged_data = pd.merge(luka_points, mavericks_outcomes, left_on='GAME_ID', right_on='GAME_DATE')
    
    print("Merged Data:")
    print(merged_data.head())  # Print merged DataFrame
    
    # Calculate Luka's average points in wins and points in losses
    avg_points_in_wins = merged_data[merged_data['WL'] == 'W']['PTS'].mean()
    points_in_losses = merged_data[merged_data['WL'] == 'L']['PTS']
    
    # Display the results
    print("Luka Doncic's Average Points in Wins:", avg_points_in_wins)
    print("Luka Doncic's Points in Losses:")
    print(points_in_losses)

# Function to fetch Luka Doncic's points scored for the last 50 games
def get_luka_points_last_50_games():
    # Use the LeagueGameLog API to fetch the game log for Luka Doncic
    # You'll need to replace the arguments with the appropriate parameters for the API request
    game_log = LeagueGameLog(season='2023-24', player_or_team_abbreviation='P', last_n_games=50)
    
    # Convert the game log data into a DataFrame
    luka_game_log_df = game_log.get_data_frames()[0]
    
    # Filter and select required columns
    luka_points = luka_game_log_df[['GAME_ID', 'GAME_DATE', 'PTS', 'WL']]
    
    return luka_points

# Function to fetch Dallas Mavericks' team game log for the last 50 games
def get_mavericks_team_gamelog_last_50_games():
    # Use the TeamGameLogs API to fetch the game log for the Dallas Mavericks
    # You'll need to replace the arguments with the appropriate parameters for the API request
    mavericks_game_logs = TeamGameLogs(team_id='1610612742', season='2023-24', last_n_games_nullable=50)
    
    # Convert the game log data into a DataFrame
    mavericks_game_logs_df = mavericks_game_logs.get_data_frames()[0]
    
    return mavericks_game_logs_df

if __name__ == "__main__":
    main()

