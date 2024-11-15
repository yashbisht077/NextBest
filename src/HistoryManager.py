import csv
import os


def save_recommendations_to_csv(movieORanime,selected_movie_or_anime,recommended_movie_or_anime,folder_path='../src',filename='recommended.csv'):
    from datetime import datetime
    datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_path = os.path.join(folder_path, filename)
    row_count = 0
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for row in csv.reader(file):
                row_count += 1

    row_count -= 1
    write_mode = 'w' if row_count >= 10 else 'a'

    recommended_movie_names_str = ", ".join(recommended_movie_or_anime)
    with open (file_path,mode=write_mode,encoding='utf-8') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(['Datetime', 'Movie/Anime', 'Name', 'Recommended'])
        writer.writerow([datetime,movieORanime,selected_movie_or_anime, recommended_movie_names_str])
