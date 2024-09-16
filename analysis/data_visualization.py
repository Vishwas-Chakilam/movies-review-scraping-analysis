# data_visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """
    Load the cleaned movie data from a CSV file.
    """
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return None

def visualize_data(df):
    """
    Create visualizations from the DataFrame.
    """
    if df is None:
        print("No data to visualize.")
        return

    print("Starting data visualization...")

    # Distribution of IMDb Ratings
    plt.figure(figsize=(12, 6))
    sns.histplot(df['rating'].dropna(), bins=20, kde=True, color='blue')
    plt.title('Distribution of IMDb Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('visualizations/ratings_distribution.png')
    plt.show()

    # Count of Movies by Genre (if genre data is available)
    if 'genre' in df.columns:
        plt.figure(figsize=(14, 7))
        genre_counts = df['genre'].value_counts()
        sns.barplot(x=genre_counts.index, y=genre_counts.values, palette='viridis')
        plt.title('Number of Movies by Genre')
        plt.xlabel('Genre')
        plt.ylabel('Number of Movies')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.savefig('visualizations/movies_by_genre.png')
        plt.show()
    
    # Movies Released Over Time
    plt.figure(figsize=(14, 7))
    yearly_counts = df['year'].value_counts().sort_index()
    sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker='o', color='green')
    plt.title('Number of Movies Released Each Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.grid(True)
    plt.savefig('visualizations/movies_by_year.png')
    plt.show()

    # Top Rated Movies (Bar Chart)
    top_rated = df.sort_values(by='rating', ascending=False).head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=top_rated['rating'], y=top_rated['movie_title'], palette='rocket')
    plt.title('Top 10 Rated Movies')
    plt.xlabel('Rating')
    plt.ylabel('Movie Title')
    plt.grid(True)
    plt.savefig('visualizations/top_rated_movies.png')
    plt.show()

def main():
    input_filepath = 'data/imdb_top_250_movies_cleaned.csv'

    # Load data
    df = load_data(input_filepath)

    # Visualize data
    visualize_data(df)

if __name__ == "__main__":
    main()
