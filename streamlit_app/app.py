import pandas as pd
import numpy as np
import streamlit as st
import pickle
import sys
import os

st.set_page_config(layout="wide")

folder_path = os.path.abspath("../src")
sys.path.append(folder_path)

from movie_recommender import get_movie_recommendations,get_filtered_recommendations
from anime_recommender import get_anime_recommendations


# Load data from pickle file
movie_list = pickle.load(open("../models/movie_list.pkl", "rb"))
anime_list = pickle.load(open("../models/anime_list.pkl", "rb"))


st.sidebar.title("NextBest:sparkles:")
option = st.sidebar.selectbox(
    "What would you like to explore?",
    ("Movie", "Anime"),
    index=None,
    help="Choose between movie recommendations or anime recommendations."
)

if(option == "Movie"):
    st.sidebar.header("_Movie-:blue[Mate]_ :movie_camera:")
    maxRecommend = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    # Movie selection dropdown
    selected_movie = st.sidebar.selectbox(
        "Select a Movie",
        movie_list["title"]
    )

    # Number of movies to recommend dropdown
    num_movies_to_recommend = st.sidebar.selectbox(
        "How Many Movies to Recommend",
        maxRecommend,
        help="Select how many movies you would like to be recommended."
    )
    # Rating filter toggle and rating selection
    if "filter_enabled" not in st.session_state:
        st.session_state.filter_enabled = False

    st.sidebar.checkbox(
        "Would you like to turn on or off the filter for ratings above a certain threshold?",
        key="filter_enabled"
    )
    rating_threshold = st.sidebar.selectbox(
        "Minimum Rating?",
        options=[float(x) for x in range(1, 11)],
        disabled=not st.session_state.filter_enabled,
        help="Select the minimum rating threshold (1 to 10) for the movie recommendations."
    )
    # Show recommendations on button click
    if st.sidebar.button("Show Recommendation"):
        st.sidebar.markdown("Generating your movie recommendations... :movie_camera:")
        if st.session_state.filter_enabled:
            recommended_movie_names, recommended_movie_posters = get_filtered_recommendations(selected_movie, num_movies_to_recommend, rating_threshold)
        else:
            recommended_movie_names, recommended_movie_posters = get_movie_recommendations(selected_movie, num_movies_to_recommend)

        cols = st.columns(num_movies_to_recommend)
        for i in range(num_movies_to_recommend):
            with cols[i]:
                st.text(recommended_movie_names[i])
                poster_url, vote_average = recommended_movie_posters[i]
                st.markdown(f"Rating:star:: {vote_average}")
                st.image(poster_url)

elif(option == "Anime"):
    st.sidebar.header("Anime-:blue[Mate]_ :movie_camera:")
    maxRecommend = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    # Anime selection dropdown
    selected_anime = st.sidebar.selectbox(
        "Select an Anime",
        anime_list["Name"],
        help="Pick an anime title from the list to get recommendations."
    )

    # Number of Animes to recommend dropdown
    num_animes_to_recommend = st.sidebar.selectbox(
        "How Many Animes to Recommend?",
        maxRecommend,
        help="Select how many animes you would like to be recommended."
    )
    # Show recommendations on button click
    if st.sidebar.button("Show Recommendation"):
        st.sidebar.markdown("Generating your anime recommendations... :video_camera:")
        recommended_anime_names, recommended_anime_posters = get_anime_recommendations(selected_anime, num_animes_to_recommend)

        cols = st.columns(num_animes_to_recommend)
        for i in range(num_animes_to_recommend):
            with cols[i]:
                st.text(recommended_anime_names[i])
                poster_url, vote_average = recommended_anime_posters[i]
                st.markdown(f"Rating:star:: {vote_average}")
                st.image(poster_url)
