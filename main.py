import requests
import json
import pandas as pd

def main():
    """
    This function uses a web scraper in order to collect metadata from a set of
    games on the epic games store website
    The list of games will be loaded from a cvs file, the output will also be
    a csv file.
    """

    og_csv_filpath = "Newzoo Data Analyst Assignment/egs_game_ranking.csv"

    games_to_find = pd.read_csv(og_csv_filpath)
    games_to_find["tags"] = ''
    games_to_find["Action"] = False
    endpoint_request_base = "https://store-content-ipv4.ak.epicgames.com/api/en-US/content/products/"

    for i, gs in enumerate(games_to_find['Game slug']):
        print(i)
        combined = endpoint_request_base+gs
        response = requests.get(combined)
        results = json.loads(response.text)

        for page in results["pages"]:
            game_tags = []
            try:
                new_game_tags = page['data']['meta']['tags']
                game_tags.extend(list(set(new_game_tags) - set(game_tags)))
            except KeyError:
                pass
        if game_tags == []:
            games_to_find["tags"][i] = ['No tag data avalable']
        else:
            games_to_find["tags"][i] = game_tags
            if 'ACTION' in game_tags:
                games_to_find["Action"][i] = True

    action_games = games_to_find[games_to_find["Action"]==True]
    action_games.sort_values('Epic Games rating', ascending = False)

    action_games.to_csv('output/action_games_sorted.csv', columns =["Game slug", "Epic Games rating", "Number of raters", " Bayes rating"])


if __name__ == "__main__":
    main()
