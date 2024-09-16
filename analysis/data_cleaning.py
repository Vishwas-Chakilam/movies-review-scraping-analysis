# data_cleaning.py

import pandas as pd

def load_data(filepath):
    """
    Load the movie data from a CSV file.
    """
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return None

def clean_data(df):
    """
    Perform data cleaning on the DataFrame.
    """
    if df is None:
        print("No data to clean.")
        return None

    print("Starting data cleaning...")

    # Drop any duplicate rows
    df = df.drop_duplicates()
    print(f"Duplicates removed. Remaining rows: {len(df)}")

    # Handle missing values
    # For simplicity, we will drop rows with missing values. 
    # You can also choose to fill missing values with a specific value.
    df = df.dropna()
    print(f"Missing values handled. Remaining rows: {len(df)}")

    # Ensure correct data types
    # For example, convert 'rating' column to float
    if 'rating' in df.columns:
        df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    
    # Ensure 'year' column is an integer
    if 'year' in df.columns:
        df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')
    
    # Reset index after cleaning
    df = df.reset_index(drop=True)
    
    print("Data cleaning completed.")
    return df

def save_clean_data(df, output_filepath):
    """
    Save the cleaned DataFrame to a new CSV file.
    """
    if df is not None:
        df.to_csv(output_filepath, index=False)
        print(f"Cleaned data saved to {output_filepath}")
    else:
        print("No data to save.")

def main():
    input_filepath = 'data/imdb_top_250_movies.csv'
    output_filepath = 'data/imdb_top_250_movies_cleaned.csv'

    # Load data
    df = load_data(input_filepath)

    # Clean data
    cleaned_df = clean_data(df)

    # Save cleaned data
    save_clean_data(cleaned_df, output_filepath)

if __name__ == "__main__":
    main()
