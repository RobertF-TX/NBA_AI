import numpy as np
import tensorflow as tf
from nba_api.stats.endpoints import PlayerGameLogs

# Step 1: Preprocess Data
game_logs = PlayerGameLogs(
    player_id_nullable='1629029',
    season_nullable='2023-24',
    last_n_games_nullable=50
)
game_logs_data = game_logs.get_data_frames()[0]
points_last_50_games = game_logs_data['PTS'].tolist()

# Prepare input data (X) and target data (y)
X = np.array(points_last_50_games[:-5])  # Last 50 games' points (excluding last 5)
y = np.array(points_last_50_games[5:])   # Next 5 games' points

# Step 2: Build Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Step 3: Train Model
model.fit(X, y, epochs=50, batch_size=8)

# Step 4: Predict Next 5 Scores
next_5_predictions = model.predict(np.array(points_last_50_games[-5:]).reshape(-1, 1))
print("Predicted next 5 scores:", next_5_predictions.flatten())

