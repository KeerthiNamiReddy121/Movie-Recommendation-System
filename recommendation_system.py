import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_movies():
    """Load movie information from the CSV file."""
    return pd.read_csv("movies.csv")


def create_similarity_matrix(movies):
    """Convert movie genres to numerical features and calculate similarity."""

    vectorizer = TfidfVectorizer()
    genre_matrix = vectorizer.fit_transform(movies["genres"])

    similarity_matrix = cosine_similarity(genre_matrix)

    return similarity_matrix


def recommend_movies(movie_title, movies, similarity_matrix, number=5):
    """Recommend movies that are similar to the selected movie."""

    matching_movies = movies[
        movies["title"].str.lower() == movie_title.lower()
    ]

    if matching_movies.empty:
        return None

    movie_index = matching_movies.index[0]

    similarity_scores = list(
        enumerate(similarity_matrix[movie_index])
    )
    
    # Remove the selected movie itself from the results
    similarity_scores = [
        (index, score)
        for index, score in similarity_scores
        if index != movie_index
    ]

    # Rank the remaining movies from most similar to least similar
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )
    
    similar_movies = similarity_scores[:number]

    recommendations = []

    for index, score in similar_movies:
        recommendations.append(
            (movies.iloc[index]["title"], score)
        )

    return recommendations


def main():

    print("=" * 45)
    print("       MOVIE RECOMMENDATION SYSTEM")
    print("=" * 45)

    movies = load_movies()

    similarity_matrix = create_similarity_matrix(movies)

    print("\nAvailable Movies:\n")

    for number, title in enumerate(movies["title"], start=1):
        print(f"{number}. {title}")

    movie_title = input(
        "\nEnter the name of a movie you like: "
    )

    recommendations = recommend_movies(
        movie_title,
        movies,
        similarity_matrix
    )

    if recommendations is None:

        print("\nMovie not found.")
        print("Please select a movie from the available list.")

    else:

        print(
            f"\nBecause you liked '{movie_title}', "
            "you may also like:\n"
        )

        for number, (title, score) in enumerate(
            recommendations,
            start=1
        ):
            print(
                f"{number}. {title} "
                f"(Similarity: {score:.2f})"
            )

    print(
        "\nThank you for using the "
        "Movie Recommendation System!"
    )


if __name__ == "__main__":
    main()