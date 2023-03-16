import urllib.request

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

def main():
    """
    This function uses a web scraper in order to collect metadata from a set of
    games on the epic games store website
    The list of games will be loaded from a cvs file, the output will also be
    a csv file.
    """

    # api = EpicGamesStoreAPI()
    # test_catalog = api.fetch_catalog(1, "games", )

    enpoint_request_base = "https://store-content-ipv4.ak.epicgames.com/api/en-US/content/products/"
    slug_example = "red-dead-redemption-2"

    data = urllib.request.urlopen(enpoint_request_base + slug_example)
    print(enpoint_request_base + slug_example)
    for line in data:
        game_data = line

    breakpoint()

if __name__ == "__main__":
    main()
