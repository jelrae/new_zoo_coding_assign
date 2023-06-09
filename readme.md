About:

This folder contains the structure, data and code to needed to collect the metadata from the epic games store for the games listed in the 'egs_games_ranking.csv' file. The code is written in python.

How to run:

The function can be run by using the command python main.py in the terminal while in the directory new_zoo_coding_assign. The sorted list of action games will be exported as a CSV file in the output folder.

Requirements:

Packages:
pandas, json, copy, requests. tqdm, os

Input file:

The script requires the input csv to be called 'egs_games_ranking.csv' and to be in the folder 'Newzoo Data Analyst Assignment' and requires 2 columns in order to run, 'Game slug' and 'Epic Games rating'. 'Game slug' must be a string for the game slug used in the api callout, while epic games rating must be a number.

Output:

The output is a CSV file found in the output folder called 'action_games_sorted', which shows the game title and the associated score in descending order.

Extra Information:

When examining the meta data, there were some cases where there was no tag data available. I looked into a few of these cases to see if there was another source I could use, but I did not find one. I could implement another solution such as trying to find them online with another scraper, but since this assignment asked to use this link, I only used the data I had available from the link.

Future work:

Since the meta data also contains the date last updated, I would want to add in a check to see if the data had been updated since the last visit, if it hasn't been we can skip updating which would save time if the dataset was much larger.  Additionally, depending on the future use of this dataframe, I would want to add in more of the metadata, and also possibly remove the tags column and just have a boolean column for each of the game tags/genres. This could make repeated access faster and cleaner.
