```
NextBest/
│
├── data/                   # Store datasets here
│   ├── tmdb_5000_credits.csv
│   ├── tmdb_5000_movies.csv
│   └── anime-dataset-2023.csv
│
├── models/                 # Store model files
│   ├── anime_list.pkl          # models will be saved here automatically when running
│   ├── anime_similarity.pkl    # the Movie and Anime recommender notebooks
│   ├── movie_list.pkl
│   └── movie_similarity.pkl
│
├── notebooks/              # Jupyter notebooks for model development
│   ├── Movie_Recommender_Model.ipynb   # Running these notebooks will generate model files
│   └── Anime_Recommender_Model.ipynb   # and save them in the models/ directory
│
├── src/                    # Source code files
│   ├── movie_recommender.py   # Movie recommendation functionality
│   └── anime_recommender.py   # Anime recommendation functionality
│
├── streamlit_app/          # Streamlit application
│   └── app.py              # Main Streamlit app
│
├── README.md               # Project overview and instructions
├── requirements.txt        # List of dependencies
└── .gitignore              # Files and directories to ignore in Git
```
