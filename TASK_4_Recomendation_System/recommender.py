import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")

vectorizer = CountVectorizer()

genre_matrix = vectorizer.fit_transform(
    movies["genre"]
)

similarity = cosine_similarity(
    genre_matrix
)

def recommend(movie_name):

    movie_index = movies[
        movies["movie"] == movie_name
    ].index[0]

    scores = list(
        enumerate(
            similarity[movie_index]
        )
    )

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for i in scores[1:6]:
        recommendations.append(
        (
          movies.iloc[i[0]]["movie"],
          round(i[1] * 100, 2)
        )
    )

    return recommendations