import pickle

# Load data from pickle file
anime_similarity = pickle.load(open("../models/anime_similarity.pkl", "rb"))
anime_list = pickle.load(open("../models/anime_list.pkl", "rb"))

def get_anime_recommendations(anime, num_recommendations):
    anime_index = int(anime_list[anime_list["Name"] == anime].index[0])
    top_10_similar_anime_ids = anime_similarity[anime_index]
    recommended_animes = []
    recommended_animes_posters = []
    for anime_id in top_10_similar_anime_ids[:num_recommendations]:
        vote_average = anime_list.at[anime_id,"Rating"]
        poster_url = anime_list.at[anime_id,"Image URL"]
        recommended_animes_posters.append((poster_url, vote_average))
        recommended_animes.append(anime_list.iloc[anime_id].Name)
    return recommended_animes,recommended_animes_posters
