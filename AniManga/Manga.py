"""
=====================
Get manga related stuff.
=====================
"""

import requests
from bs4 import BeautifulSoup
from AniManga.helpers.MangaHelpers import check_if_exists
from AniManga.helpers.MangaHelpers import format as format_manga_name


class Manga:
    """
    Manga class.
    """

    def __init__(self):
        """
        __init__
        """
        self.base_manga_url = "https://www.anime-planet.com/manga/"
        self.base_manga_reviews = "https://www.anime-planet.com/manga/{}/reviews"
        self.base_manga_tags = "https://www.anime-planet.com/manga/"

    def get_manga_json(self, manga: str) -> dict:
        """
        Get information on a manga.
        """
        manga = format_manga_name(manga)
        r = requests.get(self.base_manga_url + f"{manga}")
        soup = BeautifulSoup(r.content, "html5lib")
        tags = soup.find_all("div", {"class": "tags"})
        rr = requests.get(self.base_manga_reviews.format(manga))
        rsoup = BeautifulSoup(rr.content, "html5lib")

        if check_if_exists(manga):

            rank = soup.find_all("div", {"class": "pure-1 md-1-5"})
            for x in rank:
                if x.text.startswith("\nRank"):
                    rank = x.text.replace("\n", "")

            tags_list = []

            for x in tags:
                x = x.find_all("li")
                for z in x:
                    z = z.text.replace("\n", "")
                    tags_list.append(z)

            characters = []
            for x in soup.find_all(
                "strong", {"class": "CharacterCard__title rounded-card__title"}
            ):
                characters.append(x.text)

            characters = characters[:-1]

            warning_list = []

            content_warning = soup.find_all(
                "div", {"class": "tags tags--plain"})

            for x in content_warning:
                x = x.text.replace("\n", "").replace("Content Warning", "")
                warning_list.append(x)

            reviews = rsoup.find_all(
                "div", {"class": "pure-1 userContent readMore"})
            review_list = []

            for x in reviews:
                review_list.append(x)

            reviews = []

            for x in review_list:
                string = ""
                while True:
                    try:
                        x = x.find("p")
                        x = x.getText()
                        string += f"{x}\n"
                    except:
                        break

                reviews.append(string)

            manga_dict = {}
            manga_dict["title"] = soup.find("meta", property="og:title")["content"]
            manga_dict["description"] = soup.find("meta", property="og:description")[
                "content"
            ]
            manga_dict["url"] = soup.find("meta", property="og:url")["content"]
            manga_dict["type"] = soup.find("meta", property="og:type")["content"]
            manga_dict["size"] = soup.find("div", {"class": "pure-1 md-1-5"}).text.replace(
                "\n", ""
            )
            manga_dict["year"] = soup.find("span", {"class": "iconYear"}).text.replace(
                "\n", ""
            )
            manga_dict["rating"] = soup.find("div", {"class": "avgRating"}).text.replace(
                "\n", ""
            )
            manga_dict["rank"] = rank
            manga_dict["author"] = soup.find(
                "meta", property="book:author")["content"]
            manga_dict["author"] = manga_dict["author"].replace(
                "https://www.anime-planet.com/people/", ""
            )
            manga_dict["cover"] = soup.find("meta", property="og:image")["content"]
            manga_dict["tags"] = tags_list
            manga_dict["content warning"] = warning_list
            manga_dict["characters"] = characters
            manga_dict["reviews"] = reviews
            try:
                return manga_dict
            except:
                return "We could not find that. Manga is most likely not available."
        else:
            return "We could not find that."

    def get_manga_description(self, manga: str) -> str:
        """
        Get manga description.
        """
        x = self.get_manga_json(manga)
        try:
            return x["description"]
        except KeyError:
            return "We could not find characters from that manga, manga most likely isn't available."
        except:
            return "We could not find that"

    def get_manga_url(self, manga: str) -> str:
        """
        Get Anime-Planet link of a manga.
        """
        x = self.get_manga_json(manga)
        try:
            return x["url"]
        except KeyError:
            return "We could not find the url of that manga, manga most likely isn't available."
        except :
            return "We could not find that"

    def get_manga_size(self, manga: str) -> str:
        """
        Get size of a manga.
        """
        x = self.get_manga_json(manga)
        try:
            return x["size"]
        except KeyError:
            return "We could not find size of that manga, manga most likely isn't available."
        except Exception as ex:
            return ex

    def get_manga_year(self, manga: str) -> str:
        """
        Get the years the manga ran.
        """
        x = self.get_manga_json(manga)
        try:
            return x["year"]
        except KeyError:
            return "We could not find the year of that manga, manga most likely isn't available."
        except Exception as ex:
            return ex

    def get_manga_rating(self, manga: str) -> str:
        """
        Get rating of a manga according to Anime-Planet.
        """
        x = self.get_manga_json(manga)
        try:
            return x["rating"]
        except KeyError:
            return "We could not the rating of that manga, manga most likely isn't available."
        except Exception as ex:
            return ex

    def get_manga_rank(self, manga: str) -> str:
        """
        Get rank of the manga according to Anime-Planet.
        """
        x = self.get_manga_json(manga)
        try:
            return x["rank"]
        except KeyError:
            return "We could not find rank of that manga, manga most likely isn't available."
        except Exception as ex:
            return ex

    def get_manga_cover(self, manga: str) -> str:
        """
        Get cover image of manga.
        """
        x = self.get_manga_json(manga)
        try:
            return x["cover"]
        except KeyError:
            return "We could not find the cover page that manga, manga most likely isn't available."
        except Exception as ex:
            return ex

    def get_manga_author(self, manga: str) -> str:
        """
        Get author of a manga.
        """
        x = self.get_manga_json(manga)
        try:
            return x["author"]
        except KeyError:
            return "We could not find the author of that manga, manga most likely isn't available."
        except Exception as ex:
            return ex

    def get_manga_tags(self, manga: str) -> list:
        """
        Get the tags of a manga.
        """
        x = self.get_manga_json(manga)
        try:
            return x["tags"]
        except KeyError:
            return "We could not find the tags of that manga, manga most likely isn't available."
        except Exception as ex:
            return ex

    def get_manga_content_warning(self, manga: str) -> list:
        """
        Get content warning of a manga.
        """
        x = self.get_manga_json(manga)
        try:
            return x["content warning"]
        except KeyError:
            return "We could not find the content warning of that manga, manga most likely isn't available."
        except Exception as ex:
            return ex

    def get_manga_reviews(self, manga: str) -> list:
        """
        Get the reviews of a manga.
        """

        x = self.get_manga_json(manga)

        try:
            return x["reviews"]
        except KeyError:
            return "We could not find reviews of that manga, manga most likely isn't available."
        except Exception as ex:
            return ex

    def get_manga_characters(self, manga: str) -> list:
        """
        Get the characters of a manga.
        """
        manga = format_manga_name(manga)

        r = requests.get(
            "https://www.anime-planet.com/manga/{}/characters".format(manga)
        )
        soup = BeautifulSoup(r.content, "html5lib")
        
        try:
            character_list = []
            characters = soup.find_all("a", {"class": "name"})
            for i in characters:
                character_list.append(i.text)
            
            return character_list
        except:
            return "We could not find characters from that manga, manga most likely doesn't exist."



    def get_popular_manga(self) -> list:
        """
        Gets current popular manga according to Anime-Planet.
        """

        r = requests.get("https://www.anime-planet.com/manga/all")
        soup = BeautifulSoup(r.content, "html5lib")

        try:
            x = soup.find_all("ul", {"class": "cardDeck cardGrid"})

            popular_mangas = []

            for ultag in x:
                for y in ultag.find_all("li"):
                    y = y.text.replace("Add to list ", "").replace("\n", "")
                    popular_mangas.append(y)
        except Exception as ex:
            return ex