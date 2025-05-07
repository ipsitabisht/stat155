from sklearn.model_selection import train_test_split

def pick_top_contributing_genres(df):
  top_15_genres = df['track_genre'].value_counts().head(15).index.tolist()
  
  
  
def main():
  
if __name__ == "__main__":
    main()
