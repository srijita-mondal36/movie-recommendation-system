import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("movies_dataset.csv")   # Replace with your CSV filename

# Keep only popular movies (at least 50 ratings)
movie_counts = df["Movie_Name"].value_counts()
popular_movies = movie_counts[movie_counts >= 50].index

df = df[df["Movie_Name"].isin(popular_movies)]

# Remove duplicates so each movie appears once
movies_df = df[["Movie_Name", "Genre"]].drop_duplicates()

# Fill missing genres
movies_df["Genre"] = movies_df["Genre"].fillna("")

print("Movies available for recommendation:", len(movies_df))

# Convert genres to vectors
cv = CountVectorizer(stop_words="english")
genre_matrix = cv.fit_transform(movies_df["Genre"])

# Similarity matrix (now much smaller)
similarity = cosine_similarity(genre_matrix)

def recommend(movie_name):
    movie_name = movie_name.lower()

    matches = movies_df[
        movies_df["Movie_Name"].str.lower() == movie_name
    ]

    if matches.empty:
        print("Movie not found!")
        return

    idx = matches.index[0]

    # Convert original index to position
    pos = movies_df.index.get_loc(idx)

    scores = list(enumerate(similarity[pos]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nTop 5 Recommendations:\n")

    count = 0
    for i, score in scores[1:]:
        print(movies_df.iloc[i]["Movie_Name"])
        count += 1

        if count == 5:
            break

# Main program
movie = input("Enter a movie name: ")
recommend(movie)