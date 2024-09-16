import requests
import pandas as pd

# Define the API key and base URL
api_key = '77699aa7'
base_url = 'http://www.omdbapi.com/'

# Function to fetch movie data
def fetch_movie_data(title):
    response = requests.get(base_url, params={'t': title, 'apikey': api_key})
    data = response.json()
    return data

# Example movie titles
movies = [
    'The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'The Lord of the Rings: The Return of the King',
    'Forrest Gump', 'Inception', 'Fight Club', 'The Lord of the Rings: The Fellowship of the Ring', 'The Matrix'
]

# Create a list to store movie information
movies_list = []

for movie_title in movies:
    data = fetch_movie_data(movie_title)
    
    if data['Response'] == 'True':
        movie_data = {
            "Title": data.get('Title'),
            "Year": data.get('Year'),
            "Rated": data.get('Rated'),
            "Released": data.get('Released'),
            "Runtime": data.get('Runtime'),
            "Genre": data.get('Genre'),
            "Director": data.get('Director'),
            "Writer": data.get('Writer'),
            "Actors": data.get('Actors'),
            "Plot": data.get('Plot'),
            "Language": data.get('Language'),
            "Country": data.get('Country'),
            "Awards": data.get('Awards'),
            "IMDB Rating": data.get('imdbRating'),
            "IMDB Votes": data.get('imdbVotes'),
            "IMDB ID": data.get('imdbID')
        }
        movies_list.append(movie_data)

# Convert the list of movie data to a pandas DataFrame
df = pd.DataFrame(movies_list)

# Save the data to a CSV file
df.to_csv('omdb_movies.csv', index=False)
print("Data successfully saved to omdb_movies.csv")
