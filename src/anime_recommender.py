import pandas as pd
import numpy as np
import requests
import pickle

# Load data from pickle file
anime_similarity = pickle.load(open("../models/anime_similarity.pkl", "rb"))
anime_list = pickle.load(open("../models/anime_list.pkl", "rb"))

def get_anime_recommendations(anime, num_recommendations):
    anime_index = int(anime_list[anime_list["Name"] == anime].index[0])
    distances = sorted(list(enumerate(anime_similarity[anime_index])), reverse=True, key=lambda x: x[1])
    recommended_animes = []
    recommended_animes_posters = []
    for i in distances[1:num_recommendations+1]:
        vote_average = anime_list.at[i[0],"Rating"]
        poster_url = anime_list.at[i[0],"Image URL"]
        recommended_animes_posters.append((poster_url, vote_average))
        recommended_animes.append(anime_list.iloc[i[0]].Name)
    return recommended_animes,recommended_animes_posters
