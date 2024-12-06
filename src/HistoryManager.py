import csv
import os

def save_recommendations_to_csv(movieORanime, selected_movie_or_anime, recommended_movie_or_anime, folder_path='../src', filename='recommended.csv'):
    from datetime import datetime
    # Get current datetime in the desired format
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_path = os.path.join(folder_path, filename)

    # Create the new row to be inserted
    recommended_movie_names_str = ", ".join(recommended_movie_or_anime)
    new_row = [datetime_now, movieORanime, selected_movie_or_anime, recommended_movie_names_str]

    # Check if the file exists
    if os.path.exists(file_path):
        # Read all the current rows from the file
        with open(file_path, 'r', encoding='utf-8') as file:
            rows = list(csv.reader(file))

        # Insert the new row at the beginning (after the header)
        rows.insert(1, new_row)  # Insert after the header (index 1)

        # If there are more than 10 rows, keep only the latest 10
        if len(rows) > 11:  # 1 for header + 10 data rows
            rows = rows[:11]  # Keep the first 10 data rows (after the header)

        # Write the updated content back to the CSV
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Datetime', 'Movie/Anime', 'Name', 'Recommended'])  # Write the header
            writer.writerows(rows[1:])  # Write the data (skip the header)
    else:
        # If file doesn't exist, create a new file and write the row
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Datetime', 'Movie/Anime', 'Name', 'Recommended'])  # Write the header
            writer.writerow(new_row)  # Write the new row as the first data
