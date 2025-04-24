import pandas as pd


df = pd.read_csv("data/spotify.csv")

# remove duplicates
df = df.drop_duplicates(subset=['track_id'], keep='last')

# remove nan rows 
df = df.dropna(subset=['track_name', 'album_name', 'artists'])

df.to_csv("data/spotify_cleaned.csv", index=False)
