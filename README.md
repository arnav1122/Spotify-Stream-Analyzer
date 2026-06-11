# Spotify Stream Analyzer

Spotify Stream Analyzer is a Python-based data analysis project that explores the relationship between song characteristics and streaming performance. The project uses Spotify music data and provides various analytical tools to help understand how different audio features and engagement metrics relate to a song's popularity.

## Features

* Analyze Danceability, Energy, Loudness, Acousticness, Valence, and Tempo against Stream counts
* Generate correlation heatmaps for numerical features
* View dataset summaries and missing value reports
* Explore Top 10 Streamed Songs and Most Viewed Songs
* Identify Top Artists by Total Streams
* Compare Official Videos vs Non-Official Videos
* Analyze Licensed vs Non-Licensed content performance
* Compare Spotify and YouTube popularity metrics
* Examine Album Type performance and song duration statistics
* View Top Liked and Most Commented songs

## Technologies Used

* Python
* Pandas
* Seaborn
* Matplotlib

## Project Structure

```text
Spotify-Stream-Analyzer/
│
├── spotify.py
├── cleaned_dataset.csv
├── requirements.txt
└── README.md
```

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python spotify.py
```

The application provides a menu-driven interface where users can select different analyses and visualizations to explore the dataset.

## Learning Outcomes

This project demonstrates:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Data visualization using Seaborn and Matplotlib
* Working with real-world datasets
* Building interactive menu-driven Python applications

## Future Improvements

* Add Machine Learning models to predict song popularity
* Build an interactive dashboard
* Export analysis results to reports
* Add advanced statistical analysis

## Author

Arnav
