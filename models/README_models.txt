This folder is intended to store the model files for the NextBest project.

Important Notes:
1. The model files (anime_list.pkl, anime_similarity.pkl, movie_list.pkl, movie_similarity.pkl) will be generated automatically when you run the respective Jupyter notebooks in the `notebooks/` directory:
   - Movie_Recommender_Model.ipynb for movie recommendations
   - Anime_Recommender_Model.ipynb for anime recommendations

2. Make sure you have installed all necessary dependencies from requirements.txt before running the notebooks.

3. Once generated, the .pkl files will be saved here and used by the main application in `streamlit_app/app.py`.

If the .pkl files are missing, please run the notebooks to create them before launching the Streamlit app.
