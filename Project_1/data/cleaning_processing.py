import pandas as pd


df = pd.read_csv("data/spotify.csv")

# remove duplicates
df = df.drop_duplicates(subset=['track_id'], keep='last')

# remove rows that dont contribute to analyzing audio features 
df = df.drop(subset=['track_name', 'album_name', 'artists'])

# convert true false to 1, 0
df['explicit'] = df['explicit'].astype(int)

df['is_hit'] = (df['popularity'] >= 0.75).astype(float)

df.to_csv("data/spotify_cleaned.csv", index=False)
