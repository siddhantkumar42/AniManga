import requests
from bs4 import BeautifulSoup


def check_if_exists(manga: str) -> bool:
    r = requests.get("https://www.anime-planet.com/manga/{}".format(manga))
    soup = BeautifulSoup(r.content, "html5lib")

    results = soup.find("meta", property="og:title")

    if not results:
        results = False
    else:
        results = True
    return results


def format_(manga: str) -> str:
    return manga.lower().replace(" ", "-")
