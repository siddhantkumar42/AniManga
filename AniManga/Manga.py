import requests
from bs4 import BeautifulSoup

class Manga:
	'''
	Manga class.
	'''
	def __init__(self):
		'''
		__init__
		'''
		self.base_manga_url = "https://www.anime-planet.com/manga/"
		self.base_manga_reviews = "https://www.anime-planet.com/manga/{}/reviews"

    #helper functions
    def check_if_exists(manga):
        r = requests.get("https://www.anime-planet.com/manga/{}".format(manga))
        soup = BeautifulSoup(r.content, "html5lib")

        results = soup.find("meta", property="og:title")

        if not results:
            return False
        else:
            return True


    def format(manga: str) -> str:
        return manga.lower().replace(" ", "-")

    #main functions
	def get_manga_reviews(self, manga: str) -> list:
		'''
		Get the reviews of a manga.
		'''
		manga = self.format(manga)
		r = requests.get(self.base_manga_reviews.format(manga))
		soup = BeautifulSoup(r.content, "html5lib")
		if self.check_if_exists(manga):
			reviews = soup.find_all("div", {"class":"pure-1 userContent readMore"})
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

			return reviews
		else:
			return "We could not find that."


	def get_manga_info(self, manga: str) -> dict:
		'''
		Get information on a manga.
		'''
		manga = self.format(manga)
		r = requests.get(self.base_manga_url + f"{manga}")
		soup = BeautifulSoup(r.content, "html5lib")

		if self.check_if_exists(manga):
			dict = {}
			dict["title"] = soup.find("meta", property="og:title")["content"]
			dict["description"] = soup.find("meta", property="og:description")["content"]
			dict["url"] = soup.find("meta", property="og:url")["content"]
			dict["type"] = soup.find("meta", property="og:type")["content"]
			dict["author"] = soup.find("meta", property="book:author")["content"]
			dict["author"] = dict["author"].replace("https://www.anime-planet.com/people/","")
			dict["cover"] = soup.find("meta", property="og:image")["content"]
			dict["reviews"] = self.get_manga_reviews(manga)
			return dict
		else:
			return "We could not find that."

	def get_manga_description(self, manga: str) -> str:
		'''
		Get manga description.
		'''
		x = self.get_manga_info(manga)
		try:
			return x["description"]
		except:
			return x

	def get_manga_url(self, manga: str) -> str:
		'''
		Get Anime-Planet link of a manga.
		'''
		x = self.get_manga_info(manga)
		try:
			return x["url"]
		except:
			return x

	def get_manga_cover(self, manga: str) -> str:
		'''
		Get cover image of manga.
		'''
		x = self.get_manga_info(manga)
		try:
			return x["cover"]
		except:
			return x

	def get_manga_author(self, manga: str) -> str:
		'''
		Get author of a manga.
		'''
		x = self.get_manga_info(manga)
		try:
			return x["author"]
		except:
			return x
