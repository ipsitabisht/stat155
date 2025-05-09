import pandas as pd


df = pd.read_csv("spotify.csv")

# remove duplicates
df = df.drop_duplicates(subset=['track_id'], keep='last')

# convert true false to 1, 0
df['explicit'] = df['explicit'].astype(int)

df['is_hit'] = (df['popularity'] >= 75).astype(float)

df.to_csv("spotify_cleaned.csv", index=False)
