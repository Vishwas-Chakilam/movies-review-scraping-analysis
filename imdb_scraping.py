from bs4 import BeautifulSoup
import requests
import pandas as pd

# Define headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# URL of the IMDb Top 250 Movies list
url = 'https://www.imdb.com/chart/top'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Print a snippet of the HTML to inspect the structure
print(soup.prettify()[:2000])

# Extract movie details from the correct HTML structure
movies = soup.select('td.titleColumn')
ratings = [b.contents[0] for b in soup.select('td.imdbRating strong')]

# Print extracted movie titles and ratings
print("Movies:", [movie.get_text(strip=True) for movie in movies])
print("Ratings:", ratings)

# Create an empty list for storing movie information
movies_list = []

# Iterating over movies to extract details
for index in range(len(movies)):
    movie = movies[index]
    movie_title = movie.a.text
    year = movie.span.text.strip('()')
    place = movie.get_text(strip=True).split('.')[0]
    
    # Storing movie information in a dictionary
    data = {
        "place": place,
        "movie_title": movie_title,
        "rating": ratings[index],
        "year": year
    }
    movies_list.append(data)

# Convert the list of movie data to a pandas DataFrame
df = pd.DataFrame(movies_list)

# Saving the data to a CSV file
df.to_csv('imdb_top_250_movies.csv', index=False)
print("Data successfully saved to imdb_top_250_movies.csv")
