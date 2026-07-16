'''
**Netflix**! What started in 1997 as a DVD rental service has since exploded into one of the largest entertainment and media companies.

Given the large number of movies and series available on the platform, it is a perfect opportunity to flex your exploratory data analysis skills and dive into the entertainment industry.

You work for a production company that specializes in nostalgic styles. You want to do some research on movies released in the 1990's. You'll delve into Netflix data and perform exploratory data analysis to better understand this awesome movie decade!

You have been supplied with the dataset `netflix_data.csv`, along with the following table detailing the column names and descriptions. Feel free to experiment further after submitting!

## The data
### **netflix_data.csv**
| Column | Description |
|--------|-------------|
| `show_id` | The ID of the show |
| `type` | Type of show |
| `title` | Title of the show |
| `director` | Director of the show |
| `cast` | Cast of the show |
| `country` | Country of origin |
| `date_added` | Date added to Netflix |
| `release_year` | Year of Netflix release |
| `duration` | Duration of the show in minutes |
| `description` | Description of the show |
| `genre` | Show genre |
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_data.csv")
netflix_90s = netflix_df[np.logical_and(netflix_df['release_year'] >= 1990, netflix_df['release_year'] < 2000)]

# Plot histogram
plt.hist(netflix_90s['duration'], bins=10)
plt.show()

# Find the most common value (mode) in the 'duration' column
duration = netflix_90s['duration'].mode().iloc[0]

# Filter for action movies
netflix_90s_action = netflix_90s[netflix_90s['genre'] == 'Action']
# print(netflix_90s_action)

# Count how many action movies have a duration of less than 90 minutes
short_movie_count = 0
for label, row in netflix_90s_action.iterrows():
    if row['duration'] < 90:
        short_movie_count += 1
        
print(duration)
print(short_movie_count)