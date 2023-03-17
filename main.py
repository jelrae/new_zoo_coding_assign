import requests
import json
import pandas as pd
import copy
from tqdm import tqdm
import os

def main():
    """
    This function uses extracts the metadata from the link
    in order to collect metadata from a set of games on the epic games store website
    The list of games will be loaded from a cvs file, the output will also be
    a csv file.
    """

    # Open the oritional csv and make it a pd dataframe for ease of access
    try:
        og_csv_filpath = "Newzoo Data Analyst Assignment/egs_game_ranking.csv"
        og_games_database = pd.read_csv(og_csv_filpath)
    except:
        print("There was an issue in loading the data, please check readme.")

    # Make a copy of the df so the original is preserved
    gdf = copy.deepcopy(og_games_database)

    # Add in the new columns that are needed for these operations (more could be added later)
    gdf["tags"] = ''
    gdf["Action"] = False
    gdf["Name"] = ''

    # Declare the base url to get the metadata using the game slugs
    endpoint_request_base = "https://store-content-ipv4.ak.epicgames.com/api/en-US/content/products/"

    # Cycle through the game slugs and extract the needed information from the dict
    for i, gs in tqdm(enumerate(gdf['Game slug'])):
        combined = endpoint_request_base+gs
        response = requests.get(combined)
        results = json.loads(response.text)

        # Try to access the product name to store it
        try:
            gdf.loc[i, "Name"] = results["productName"]
        except KeyError:
            gdf.loc[i, "Name"] = "Produc name unavailable"

        """
        I wasnt sure if each page would show a different game tag or if some
        would not have them so I added in a for loop to cycle through them and
        compare them. It will add all tags found in the pages. First initializing
        the game tags, then getting the new ones from one of the pages, they are
         then compared and any new tags are added to the existing game tags list.
        """
        game_tags = []
        for page in results["pages"]:
            try:
                new_game_tags = page['data']['meta']['tags']
                game_tags.extend(list(set(new_game_tags) - set(game_tags)))
            except KeyError:
                pass
        # Store the tags found, if there were none, then add there was no tag data
        if game_tags == []:
            gdf.at[i, "tags"] = ['No tag data avalable']
        else:
            gdf.at[i, "tags"] = game_tags
            if 'ACTION' in game_tags:
                gdf.loc[i, "Action"] = True

    # Select only the action games
    action_games = gdf[gdf["Action"]==True]

    # Export just the game slug and the epic games rating
    if os.path.exists("output"):
        action_games.sort_values('Epic Games rating', ascending = False).to_csv('output/action_games_sorted.csv', columns =["Name", "Epic Games rating"], index=False)
    else:
        os.makedirs("output")
        action_games.sort_values('Epic Games rating', ascending = False).to_csv('output/action_games_sorted.csv', columns =["Name", "Epic Games rating"], index=False)

if __name__ == "__main__":
    main()
