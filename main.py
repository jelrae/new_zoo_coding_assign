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

    endpoint_request_base = "https://store-content-ipv4.ak.epicgames.com/api/en-US/content/products/"
    slug_example = "red-dead-redemption-2"
    combined = endpoint_request_base+slug_example
    response = requests.get(combined)
    print(response)
    results = json.loads(response.text)
    breakpoint()


if __name__ == "__main__":
    main()
