from nba_api.stats.endpoints import PlayerGameLogs, TeamGameLogs
import pandas as pd

# Function to fetch Luka Doncic's points scored for the last 50 games
def get_luka_points_last_50_games():
    # Fetch Luka Doncic's game logs for the last 50 games
    luka_game_logs = PlayerGameLogs(player_id_nullable='1629029', season_nullable='2023-24', last_n_games_nullable=50)
    luka_data = luka_game_logs.get_data_frames()[0]
    
    # Extract points scored from Luka's game logs
    luka_points = luka_data[['GAME_DATE', 'PTS']]
    
    return luka_points

# Function to fetch Dallas Mavericks' team game log for the last 50 games
def get_mavericks_team_gamelog_last_50_games():
    # Fetch Dallas Mavericks' team game log for the last 50 games
    mavericks_game_logs = TeamGameLogs(team_id_nullable='1610612742', season_nullable='2023-24', last_n_games_nullable=50)
    mavericks_data = mavericks_game_logs.get_data_frames()[0]
    
    # Extract relevant columns
    mavericks_outcomes = mavericks_data[['GAME_DATE', 'MATCHUP', 'WL']]
    
    return mavericks_outcomes

# Main function
def main():
    # Fetch Luka Doncic's points scored for the last 50 games
    luka_points = get_luka_points_last_50_games()
    
    # Fetch Dallas Mavericks' team game log for the last 50 games
    mavericks_outcomes = get_mavericks_team_gamelog_last_50_games()
    
    # Merge Luka's points and Mavericks' outcomes based on the game date
    merged_data = pd.merge(luka_points, mavericks_outcomes, on='GAME_DATE')
    
    # Display the merged data
    print("Luka Doncic's Points and Dallas Mavericks' Game Outcomes for the Last 50 Games:")
    print(merged_data)

if __name__ == "__main__":
    main()

