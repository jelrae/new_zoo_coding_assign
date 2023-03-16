from bs4 import BeautifulSoup

def main():
    """
    This function uses a web scraper in order to collect metadata from a set of
    games on the epic games store website
    The list of games will be loaded from a cvs file, the output will also be
    a csv file.
    """

    # api = EpicGamesStoreAPI()
    # test_catalog = api.fetch_catalog(1, "games", )

    endpoint_request_base = "https://store-content-ipv4.ak.epicgames.com/api/en-US/content/products/"
    slug_example = "red-dead-redemption-2"
    combined = endpoint_request_base+slug_example
    soup = BeautifulSoup(combined, 'html.parser')
    print(soup.prettify())

if __name__ == "__main__":
    main()
