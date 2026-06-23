import streamlit as st
import pandas as pd

from recommender import recommend

if "history" not in st.session_state:
    st.session_state.history = []

movies = pd.read_csv("movies.csv")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Movies Available",
        len(movies)
    )

with col2:
    st.metric(
        "Genres",
        movies["genre"].nunique()
    )

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 AI Movie Recommendation System")

st.markdown(
    "Get movie recommendations based on content similarity."
)

st.write(
    "Select a movie and get similar recommendations."
)

selected_movie = st.selectbox(
    "Choose a Movie",
    movies["movie"]
)

movie_data = movies[
    movies["movie"] == selected_movie
]

st.write(
    "Genre:",
    movie_data["genre"].values[0]
)

if st.button("Recommend"):

    recommendations = recommend(
        selected_movie
    )

    st.subheader(
        "Recommended Movies"
    )

    for movie, score in recommendations:

       st.success(
           f"{movie} ({score}% Match)"
    )
       
if selected_movie not in st.session_state.history:
    st.session_state.history.append(selected_movie)
       
st.info(
    """
    This system uses Content-Based Filtering.

    Movies are compared based on genres.

    Cosine Similarity is used to find similar movies.
    """
)


st.sidebar.title("📜 Recommendation History")

if st.sidebar.button("🗑️ Clear History"):
    st.session_state.history = []

for item in reversed(st.session_state.history):
    st.sidebar.write("🎬", item)