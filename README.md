# Movie Recommendation System

## Project Overview

This project is a content-based movie recommendation system developed in Python. The system recommends movies based on similarities in movie genres. It uses TF-IDF vectorization to convert genre information into numerical features and cosine similarity to measure similarity between movies.

The project demonstrates the use of artificial intelligence techniques together with human-computer interaction (HCI) concepts to provide users with a simple and understandable recommendation experience.

## Features

- Displays a list of available movies
- Accepts a movie title from the user
- Generates five movie recommendations
- Uses TF-IDF vectorization and cosine similarity
- Displays similarity scores
- Supports case-insensitive movie-title input
- Handles invalid movie selections with a clear error message
- Prevents the selected movie from appearing in its own recommendations

## Technologies Used

- Python 3.10
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Visual Studio Code

## Project Files

- recommendation_system.py - Main Python program
- movies.csv - Movie title and genre dataset
- requirements.txt - Required Python packages
- README.md - Project documentation
- screenshots/ - Screenshots from system testing

## Installation

Install the required packages with:

pip install -r requirements.txt

## Running the Application

Run the program with:

python recommendation_system.py

The program displays the available movies and asks the user to enter a movie title. It then calculates similarity scores and returns five recommended movies.

## Recommendation Method

The system uses a content-based filtering approach. Movie genres are converted into numerical features using TF-IDF vectorization. Cosine similarity is then used to compare the selected movie with the other movies in the dataset. Movies with higher similarity scores are ranked higher in the recommendation results.

## How It Works

The recommendation process follows these steps:

1. The program loads movie titles and genres from `movies.csv`.
2. TF-IDF vectorization converts the genre information into numerical feature vectors.
3. Cosine similarity calculates the similarity between each pair of movies.
4. The user selects a movie by entering its title.
5. The program matches the title using case-insensitive comparison.
6. The selected movie is removed from the recommendation candidates.
7. The remaining movies are ranked from highest to lowest similarity.
8. The five most similar movies are displayed with their similarity scores.

## Testing

The system was tested using movies from different genres. It was also tested with an invalid movie title to verify error handling.

During testing, the selected movie initially appeared in its own recommendation results when movies had identical similarity scores. The issue was corrected by explicitly removing the selected movie's index before ranking the remaining movies.

The testing process verifies that:

- Valid movie titles return five recommendations.
- Movie-title matching is case-insensitive.
- The selected movie does not appear in its own recommendation results.
- Invalid movie titles produce an appropriate error message.
- Recommendation results include similarity scores.

Screenshots of the Inception recommendation test, Titanic recommendation test, and invalid-input test are included in the `screenshots/` directory.

## Limitations

The current system uses a small movie dataset and relies primarily on genre information to calculate similarity. As a result, movies with similar genre labels may receive similar scores even when they differ in other characteristics.

The system does not currently use user ratings, viewing history, actors, directors, or plot descriptions. Therefore, the recommendations are based on movie-to-movie content similarity rather than individual user preferences.

## Future Improvements

Future improvements could include:

- Expanding the movie dataset
- Adding movie plot descriptions, actors, and directors as content features
- Incorporating user ratings
- Implementing collaborative filtering
- Developing a hybrid recommendation approach
- Creating a graphical user interface
- Supporting personalized recommendations based on user history

## Author

Keerthi Nami Reddy
