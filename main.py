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
    endpoint_request_base = "https://store-content-ipv4.ak.epicgames.com/api/en-US/content/products/"
    # breakpoint()
    for i, gs in enumerate(games_to_find['Game slug']):
        print(i)
        combined = endpoint_request_base+gs
        response = requests.get(combined)
        results = json.loads(response.text)
        # breakpoint()
        # for page in results["pages"]:
        try:
            games_to_find["tags"][i] = results["pages"][0]['data']['meta']['tags']
        except KeyError:
            games_to_find["tags"][i] = ['No tag data avalable']
    breakpoint()


if __name__ == "__main__":
    main()
