import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from load_data import load_file

def prep(df):
    
    # interesting genres
    distinct_genres = ['jazz', 'country', 'rock', 'dubstep', 'pop', 'heavy-metal','bluegrass', 'soul', 'reggaeton']
    features = [
        'danceability', 'energy', 'valence', 'acousticness',
        'speechiness', 'instrumentalness', 'tempo', 'loudness'
    ]
    # jazz, country, k-pop, rock, new-age, disney, dubstep, pop, techno, heavy-metal,bluegrass, soul, synth-pop, reggaeton  
    filtered_interesting_genres = df[df['track_genre'].isin(distinct_genres)]
    print(f"Number of songs in the interesting genres: {len(filtered_interesting_genres)}")


    genre_fingerprint = {}

    for genre in distinct_genres:
        print(genre)
        df_genre = df[df['track_genre'] == genre].copy()
        if df_genre.empty:
            print(f"No data found for genre: {genre}")
            continue 
        X = df_genre[features]
        
        if df_genre['is_hit'].nunique() <= 1:
            print(f"Skipping {genre} - all songs have the same hit status")
            continue
        y = df_genre['is_hit']

        scaler = StandardScaler()
        X_scaler = scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        logreg = LogisticRegression(C=0.1, random_state=0, tol=1e-5)
        logreg.fit(X_train, y_train)
        y_pred = logreg.predict(X_test)
        test_acc = accuracy_score(y_test, y_pred)
        print(f"PREDICTION for {genre}", test_acc)

        genre_fingerprint[genre] = pd.Series(logreg.coef_[0], index=features)

    fingerprints_df = pd.DataFrame(genre_fingerprint)

    # Plot heatmap-style bar chart
    fingerprints_df.T.plot(kind='bar', figsize=(14, 6), title="Feature Importance per Genre (Logistic Coefficients)")
    plt.xlabel("Genre")
    plt.ylabel("Coefficient (Higher = More Likely to Be a Hit)")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.tight_layout()
    plt.show()

def main():
  df = load_file()
  prep(df)
  
if __name__ == "__main__":
    main()
