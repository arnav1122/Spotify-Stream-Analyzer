import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
df=pd.read_csv("cleaned_dataset.csv")
df= df.drop(columns=[
    "Title",
    "Channel"
])
while True:
    print("===== SPOTIFY ANALYZER =====")
    menu = {
        1: "Danceability vs Stream",
        2: "Energy vs Stream",
        3: "Loudness vs Stream",
        4: "Acousticness vs Stream",
        5: "Valence vs Stream",
        6: "Tempo vs Stream",
        7: "Correlation Heatmap",
        8: "Dataset Summary",
        9: "Missing Values Report",
        10: "Top 10 Streamed Songs",
        11: "Top 10 Most Viewed Songs",
        12: "Top 10 Artists by Total Streams",
        13: "Official Video vs Streams",
        14: "Licensed vs Streams",
        15: "Spotify vs YouTube Song Count",
        16: "Average Streams by Album Type",
        17: "Average Song Duration",
        18: "Longest Songs",
        19: "Shortest Songs",
        20: "Top 10 Most Liked Songs",
        21: "Top 10 Most Commented Songs",
        22: "Exit"
    }
    scatter_features = {
        1: "Danceability",
        2: "Energy",
        3: "Loudness",
        4: "Acousticness",
        5: "Valence",
        6: "Tempo"
    }
    for key, value in menu.items():
        print(f"{key}. {value}")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    if choice in scatter_features :
        sns.scatterplot(
        x=scatter_features[choice],
        y="Stream",
        data=df
        )
        plt.show()
    elif choice == 7:
        print("\n===== CORRELATION HEATMAP =====")
        numeric_df = df.select_dtypes(include='number')
        plt.figure(figsize=(12, 8))
        sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Feature Correlation Heatmap")
        plt.tight_layout()
        plt.show()
    elif(choice==8):
        print("\n===== DATASET SUMMARY =====")
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")
        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nStatistics:")
        print(df.describe())
    elif choice == 9:
        print("\n===== MISSING VALUES REPORT =====")
        print(df.isnull().sum())
    elif choice == 10:
        print("\n===== TOP 10 STREAMED SONGS =====")
        top = df.sort_values(by="Stream", ascending=False)
        print(top[["Track", "Artist", "Stream"]].head(10))
    elif choice == 11:
        print("\n===== TOP 10 MOST VIEWED SONGS =====")
        top = df.sort_values(by="Views", ascending=False)
        print(top[["Track", "Artist", "Views"]].head(10))
    elif choice == 12:
        print("\n===== TOP 10 ARTISTS BY STREAMS =====")
        artists = df.groupby("Artist")["Stream"].sum()
        print(artists.sort_values(ascending=False).head(10))
    elif choice == 13:
        print("\n===== OFFICIAL VIDEO VS STREAMS =====")
        print(df.groupby("official_video")["Stream"].mean())

        sns.boxplot(x="official_video", y="Stream", data=df)
        plt.show()
    elif choice == 14:
        print("\n===== LICENSED VS STREAMS =====")
        print(df.groupby("Licensed")["Stream"].mean())

        sns.boxplot(x="Licensed", y="Stream", data=df)
        plt.show()
    elif choice == 15:
        print("\n===== SPOTIFY VS YOUTUBE =====")
        print(df["most_playedon"].value_counts())
    elif choice == 16:
        print("\n===== AVERAGE STREAMS BY ALBUM TYPE =====")
        print(df.groupby("Album_type")["Stream"].mean())
    elif choice == 17:
        print("\n===== AVERAGE SONG DURATION =====")
        print(f"{df['Duration_min'].mean():.2f} minutes")
    elif choice == 18:
        print("\n===== LONGEST SONGS =====")
        longest = df.sort_values(by="Duration_min", ascending=False)
        print(longest[["Track", "Artist", "Duration_min"]].head(10))
    elif choice == 19:
        print("\n===== SHORTEST SONGS =====")
        shortest = df.sort_values(by="Duration_min")
        print(shortest[["Track", "Artist", "Duration_min"]].head(10))
    elif choice == 20:
        print("\n===== TOP 10 MOST LIKED SONGS =====")
        top = df.sort_values(by="Likes", ascending=False)
        print(top[["Track", "Artist", "Likes"]].head(10))
    elif choice == 21:
        print("\n===== TOP 10 MOST COMMENTED SONGS =====")
        top = df.sort_values(by="Comments", ascending=False)
        print(top[["Track", "Artist", "Comments"]].head(10))
    elif choice == 22:
        print("Thank you for using Spotify Analyzer!")
        break
    elif choice  not in range(1,22):
        print("enter no in range 1-22")