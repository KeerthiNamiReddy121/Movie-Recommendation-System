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

## Testing

The system was tested using movies from different genres. It was also tested with an invalid movie title to verify error handling.

During testing, the selected movie initially appeared in its own recommendation results when movies had identical similarity scores. The issue was corrected by explicitly removing the selected movie's index before ranking the remaining movies.

## Future Improvements

Future versions could use a larger movie dataset, user ratings, collaborative filtering, a graphical user interface, and personalized recommendations based on user history.

## Author

Keerthi Nami Reddy