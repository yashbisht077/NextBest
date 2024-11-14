import pandas as pd
import numpy as np
import requests
import pickle

# Load data from pickle file
movie_similarity = pickle.load(open("../models/movie_similarity.pkl", "rb"))
movie_list = pickle.load(open("../models/movie_list.pkl", "rb"))

api_keys = [
    "58d20f63752ade8c6e45e49c08002a38",
    "8265bd1679663a7ea12ac168da84d2e8",
    "53070df475a34d2304aded57801fde38",
    "36107e2c5e86005819066f1aec8dca34",
    "27ce69086ff30b91cc60c0a4f465c5d"
]


# Function to fetch movie poster and rating based on movie_id
def fetch_movie_details(movie_id):
    url_template = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US"

    for api_key in api_keys:
        url = url_template.format(movie_id, api_key)

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()

                poster_path = data.get('poster_path')
                vote_average = data.get('vote_average', 'N/A')

                poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else "https://via.placeholder.com/500"

                return poster_url, vote_average

        except requests.exceptions.RequestException:
            continue

    return "https://via.placeholder.com/500", "N/A"


# Function to recommend movies based on similarity
def get_movie_recommendations(movie, num_recommendations):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(movie_similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_movie_posters = []
    for i in distances[1:num_recommendations+1]:
        movie_id = movie_list.at[i[0], 'movie_id']
        poster_url, vote_average = fetch_movie_details(movie_id)
        recommended_movie_posters.append((poster_url, vote_average))
        recommended_movies.append(movie_list.iloc[i[0]].title)
    return recommended_movies, recommended_movie_posters


# Function to recommend movies with rating filter
def get_filtered_recommendations(movie, num_recommendations, min_rating):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(movie_similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_movie_posters = []
    for i in distances[1:]:
        movie_index = i[0]
        similarity_score = i[1]
        vote_average = movie_list.iloc[movie_index]['vote_average']
        if vote_average >= min_rating:
            movie_id = movie_list.at[i[0], 'movie_id']
            poster_url, vote_average = fetch_movie_details(movie_id)
            recommended_movie_posters.append((poster_url, vote_average))
            recommended_movies.append(movie_list.iloc[i[0]].title)
            if len(recommended_movies) == num_recommendations:
                break
    return recommended_movies, recommended_movie_posters
