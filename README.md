# Movie Review Scraping and Analysis

![illustration](https://github.com/Vishwas-Chakilam/movies-review-scraping-analysis/blob/main/Movie%20Scraping%20and%20Analysis.png)

## Table of Contents
- [Overview](#overview)
- [Data Collection Options](#data-collection-options)
  - [1. Web Scraping (Deprecated)](#1-web-scraping-deprecated)
  - [2. Using the OMDb API (Recommended)](#2-using-the-omdb-api-recommended)
- [File Structure](#file-structure)
- [Next Steps](#next-steps)
  - [1. Data Cleaning](#1-data-cleaning)
  - [2. Data Analysis](#2-data-analysis)
  - [3. Data Visualization](#3-data-visualization)
- [Analysis Findings](#analysis-findings)
- [License](#license)
- [Contact](#contact)

## Overview

Welcome to the Movie Review Scraping and Analysis project. This repository contains resources and scripts for gathering and analyzing movie data. Due to recent updates on IMDb's website, the previous web scraping approach might no longer work. Therefore, we offer an alternative approach using the OMDb API to obtain movie data reliably.

## Data Collection Options

### 1. Web Scraping (Deprecated)

**File**: `imdb_scraping.py`

**Description**: This script was designed to scrape the IMDb Top 250 movies. Due to changes on IMDb’s website, this approach may no longer function correctly. If you still want to try web scraping, you can use this script, but be aware that it might require modifications to work with the current IMDb site structure.

**Instructions**:
- Install required packages: `beautifulsoup4`, `requests`.
- Run the script to attempt scraping data.

**Note**: Web scraping can be fragile due to frequent website updates. For a more stable solution, consider using the OMDb API.

### 2. Using the OMDb API (Recommended)

**File**: `omdb_api_fetch.py`

**Description**: This script retrieves movie data using the OMDb API. The OMDb API provides a structured and reliable way to fetch movie information, making it a preferred alternative to web scraping.

**Instructions**:
- Obtain an API key from [OMDb API](http://www.omdbapi.com/).
- Install required packages: `requests`, `pandas`.
- Modify the script with your API key.
- Run the script to fetch movie data and save it to a CSV file.

## File Structure

Here's an overview of the project directory structure:

```
Movie-Review-Scraping-Analysis/
│
├── imdb_scraping.py         # Script for web scraping IMDb Top 250 movies (Deprecated)
├── omdb_api_fetch.py        # Script for fetching movie data from OMDb API
├── requirements.txt         # List of required Python packages
├── data/                    # Directory for storing data files
│   ├── omdb_movies.csv      # Output CSV file with movie data from OMDb API
│   └── imdb_movies.csv      # Previously used for web scraping (Deprecated)
├── analysis/                # Directory for analysis scripts and notebooks
│   ├── data_cleaning.py     # Script for data cleaning
│   ├── data_analysis.py     # Script for data analysis
│   └── data_visualization.py # Script for data visualization
└── README.md                # This file
```

## Next Steps

After obtaining the data using either method, follow these steps to process and analyze it:

### 1. Data Cleaning

Data cleaning involves preprocessing the raw data to ensure it is accurate, complete, and ready for analysis. This includes:
- **Handling Missing Values**: Identify and address missing values in the dataset.
- **Correcting Data Types**: Ensure that each column has the correct data type (e.g., integers for ratings, strings for movie titles).
- **Removing Duplicates**: Check for and remove any duplicate entries.
- **Standardizing Formats**: Ensure consistent formatting, such as date formats and text capitalization.

Data cleaning can be performed using the `data_cleaning.py` script located in the `analysis/` directory.

### 2. Data Analysis

Perform data analysis to extract meaningful insights from the cleaned data. Key areas to focus on include:
- **Distribution of IMDb Ratings**: Analyze how movie ratings are distributed across the dataset. This helps in understanding the overall rating pattern and identifying any common rating trends.
- **Count of Movies by Genre**: Determine the number of movies in each genre. This insight reveals the popularity of different genres and can highlight trends in movie production.
- **Movies Released Over Time**: Examine the number of movies released each year to visualize trends and identify any significant changes in release patterns.
- **Top Rated Movies**: Identify movies with the highest ratings and explore their characteristics. This can help in understanding what makes a movie highly rated.
- **Correlation Analysis**: Explore correlations between different numerical variables, such as IMDb ratings and the number of votes. This analysis helps to understand the relationships between various metrics.

Data analysis can be performed using the `data_analysis.py` script located in the `analysis/` directory.

### 3. Data Visualization

Visualizing data helps to communicate insights effectively. You can use the following tools for visualization:
- **Python Libraries**: Use libraries like Matplotlib or Seaborn for creating various types of plots and charts. Examples include histograms for rating distributions, bar charts for genre counts, and line charts for release trends.
- **Power BI**: Create interactive dashboards with Power BI for a more comprehensive view of the data. Power BI allows you to build visualizations and dashboards that can be shared with others.

Data visualization can be performed using the `data_visualization.py` script located in the `analysis/` directory.

## Analysis Findings

Based on the data analysis, you may answer questions such as:
- **What is the distribution of IMDb ratings across different genres?**
  - **Finding**: This analysis might reveal that most movies have ratings between 7 and 9, with certain genres showing a higher average rating.

- **Which genres are most prevalent in the dataset?**
  - **Finding**: You may find that genres like "Drama" and "Action" have the highest counts, while genres like "Documentary" and "Animation" are less common.

- **How have movie releases varied over different years?**
  - **Finding**: Trends might show an increase in movie releases in recent years, reflecting changes in the film industry.

- **What are the top-rated movies and their features?**
  - **Finding**: Movies like "The Shawshank Redemption" and "The Godfather" might appear as top-rated films, with specific attributes contributing to their high ratings.

- **Is there a correlation between the number of votes and IMDb ratings?**
  - **Finding**: A strong correlation might be observed, indicating that movies with more votes tend to have higher ratings.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions, issues, or contributions, please contact [here](mailto:vishwas.chakilam@gmail.com). We welcome feedback and suggestions to improve the project.
