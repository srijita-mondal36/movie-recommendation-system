import streamlit as st
import pandas as pd

# Load only first 5000 rows
df = pd.read_csv(r"D:\movies_dataset.csv")

st.title("🎬 Movie Recommendation System")

movies = df["Movie_Name"].drop_duplicates().tolist()

selected_movie = st.selectbox(
    "Choose a Movie",
    movies
)

if st.button("Recommend"):

    movie_genre = df[df["Movie_Name"] == selected_movie]["Genre"].iloc[0]

    recommendations = df[
        (df["Genre"] == movie_genre)
        & (df["Movie_Name"] != selected_movie)
    ]["Movie_Name"].drop_duplicates().head(5)

    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.write("🎥", movie)