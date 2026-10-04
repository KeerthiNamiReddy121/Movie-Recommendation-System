import pandas as pd

from recommendation_system import (
    create_similarity_matrix,
    recommend_movies,
)


def create_test_movies():
    """Create a small movie dataset for automated testing."""
    return pd.DataFrame(
        {
            "title": [
                "Inception",
                "Interstellar",
                "The Matrix",
                "Titanic",
                "The Notebook",
                "Avatar",
            ],
            "genres": [
                "Sci-Fi Thriller",
                "Sci-Fi Drama",
                "Sci-Fi Action",
                "Romance Drama",
                "Romance Drama",
                "Sci-Fi Adventure",
            ],
        }
    )


def test_valid_movie_returns_five_recommendations():
    """A valid movie should return five recommendations."""
    movies = create_test_movies()
    similarity_matrix = create_similarity_matrix(movies)

    recommendations = recommend_movies(
        "Inception",
        movies,
        similarity_matrix,
    )

    assert recommendations is not None
    assert len(recommendations) == 5


def test_selected_movie_is_not_recommended():
    """The selected movie should not appear in its own recommendations."""
    movies = create_test_movies()
    similarity_matrix = create_similarity_matrix(movies)

    recommendations = recommend_movies(
        "Inception",
        movies,
        similarity_matrix,
    )

    recommended_titles = [
        title for title, score in recommendations
    ]

    assert "Inception" not in recommended_titles


def test_case_insensitive_movie_title():
    """Movie-title matching should be case-insensitive."""
    movies = create_test_movies()
    similarity_matrix = create_similarity_matrix(movies)

    recommendations_lowercase = recommend_movies(
        "inception",
        movies,
        similarity_matrix,
    )

    recommendations_uppercase = recommend_movies(
        "INCEPTION",
        movies,
        similarity_matrix,
    )

    assert recommendations_lowercase is not None
    assert recommendations_uppercase is not None
    assert recommendations_lowercase == recommendations_uppercase


def test_invalid_movie_returns_none():
    """An invalid movie title should return None."""
    movies = create_test_movies()
    similarity_matrix = create_similarity_matrix(movies)

    recommendations = recommend_movies(
        "Movie That Does Not Exist",
        movies,
        similarity_matrix,
    )

    assert recommendations is None


def test_recommendations_include_similarity_scores():
    """Each recommendation should contain a title and similarity score."""
    movies = create_test_movies()
    similarity_matrix = create_similarity_matrix(movies)

    recommendations = recommend_movies(
        "Inception",
        movies,
        similarity_matrix,
    )

    for title, score in recommendations:
        assert isinstance(title, str)
        assert isinstance(score, float)
        assert 0.0 <= score <= 1.0
