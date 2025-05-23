import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.inspection import permutation_importance
from sklearn.metrics import classification_report
from imblearn.over_sampling import RandomOverSampler
from load_data import load_file

def feature_importance(genres, X, y, model, numeric_features):
    for genre in genres:
        genre_col = f'track_genre_{genre}'
        if genre_col not in X.columns:
            print(f"'{genre_col}' not found. Skipping genre: {genre}")
            continue

        genre_subset = X[X[genre_col] == 1]
        y_genre = y.loc[genre_subset.index]

        if genre_subset.empty:
            print(f"No samples found for genre: {genre}")
            continue

        r = permutation_importance(
            model, genre_subset, y_genre,
            n_repeats=30, random_state=0, n_jobs=-1
        )

        imp_df = pd.DataFrame({
            'feature': genre_subset.columns,
            'importance_mean': r.importances_mean,
            'importance_std': r.importances_std
        })

        imp_df_numeric = imp_df[imp_df['feature'].isin(numeric_features)].sort_values(by='importance_mean')

        plt.figure(figsize=(10, 6))
        plt.barh(imp_df_numeric['feature'], imp_df_numeric['importance_mean'],
                 xerr=imp_df_numeric['importance_std'])
        plt.xlabel("Permutation Importance")
        plt.ylabel("Audio Feature")
        plt.title(f"Feature Importance for ANN - Genre: {genre}")
        plt.tight_layout()
        plt.show()

def prep(df):

    distinct_genres = ['jazz', 'country', 'rock', 'dubstep', 'pop', 'heavy-metal',
                       'bluegrass', 'soul', 'reggaeton', 'house', 'techno', 'k-pop']
    numeric_features = ['danceability', 'energy', 'valence', 'acousticness',
                        'speechiness', 'instrumentalness', 'tempo', 'loudness']

    df = df[df['track_genre'].isin(distinct_genres)].copy()


    y = df['is_hit']
    X_raw = df.drop(columns=['is_hit'])

    X_train_raw, X_test_raw, y_train, y_test = train_test_split(X_raw, y, test_size=0.2, random_state=42)


    # PREPROCESSING STEPS -> scale, encode, correct class imbalances
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_raw[numeric_features])
    X_test_scaled = scaler.transform(X_test_raw[numeric_features])

    X_train_scaled = pd.DataFrame(X_train_scaled, columns=numeric_features, index=X_train_raw.index)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=numeric_features, index=X_test_raw.index)


    ohe = OneHotEncoder(sparse_output=False, drop='first', handle_unknown='ignore')
    train_genre_encoded = ohe.fit_transform(X_train_raw[['track_genre']])
    test_genre_encoded = ohe.transform(X_test_raw[['track_genre']])

    genre_cols = ohe.get_feature_names_out(['track_genre'])
    train_genre_df = pd.DataFrame(train_genre_encoded, columns=genre_cols, index=X_train_raw.index)
    test_genre_df = pd.DataFrame(test_genre_encoded, columns=genre_cols, index=X_test_raw.index)


    X_train = pd.concat([X_train_scaled, train_genre_df], axis=1)
    X_test = pd.concat([X_test_scaled, test_genre_df], axis=1)

    # oversample the minority class (is hit) 
    ros = RandomOverSampler(random_state=42)
    X_resampled, y_resampled = ros.fit_resample(X_train, y_train)

    print("\nTraining ANN model...")
    ann = MLPClassifier(
        hidden_layer_sizes=(64, 32),
        activation='relu',
        solver='adam',
        batch_size=64,
        learning_rate_init=0.001,
        max_iter=2000,
        random_state=42
    )
    ann.fit(X_resampled, y_resampled)

    y_pred = ann.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    feature_importance(distinct_genres, X_test, y_test, ann, numeric_features)

def main():
    df = load_file()
    prep(df)

if __name__ == "__main__":
    main()
