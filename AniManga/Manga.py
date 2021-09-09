import requests
from bs4 import BeautifulSoup
from AniManga.helpers.MangaHelpers import check_if_exists, format

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
		self.base_manga_tags = "https://www.anime-planet.com/manga/"

    #main functions
	def get_manga_reviews(self, manga: str) -> list:
		'''
		Get the reviews of a manga.
		'''
		manga = format(manga)
		r = requests.get(self.base_manga_reviews.format(manga))
		soup = BeautifulSoup(r.content, "html5lib")
		if check_if_exists(manga):
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

	def get_manga_tags(self, manga: str) -> list:
		'''
		Get the tags of a manga.
		'''
		manga = format(manga)
		r = requests.get(self.base_manga_tags + manga)
		soup = BeautifulSoup(r.content, "html5lib")
		tags = soup.find_all("div", {"class":"tags"})

		if check_if_exists(manga):
			tags_list = []

			for x in tags:
				x = x.find_all("li")
				for z in x:
					tags_list.append(z.text)
			
			return tags_list
		else:
			return "We could not find that."
	
	def get_manga_info(self, manga: str) -> dict:
		'''
		Get information on a manga.
		'''
		manga = format(manga)
		r = requests.get(self.base_manga_url + f"{manga}")
		soup = BeautifulSoup(r.content, "html5lib")

		if check_if_exists(manga):
			dict = {}
			dict["title"] = soup.find("meta", property="og:title")["content"]
			dict["description"] = soup.find("meta", property="og:description")["content"]
			dict["url"] = soup.find("meta", property="og:url")["content"]
			dict["type"] = soup.find("meta", property="og:type")["content"]
			dict["author"] = soup.find("meta", property="book:author")["content"]
			dict["author"] = dict["author"].replace("https://www.anime-planet.com/people/","")
			dict["cover"] = soup.find("meta", property="og:image")["content"]
			dict["tags"] = self.get_manga_tags(manga)
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

	def get_popular_manga(self) -> list:
		'''
		Gets current popular manga according to Anime-Planet.
		'''
		r = requests.get("https://www.anime-planet.com/manga/all")
		soup = BeautifulSoup(r.content, "html5lib")

		x = soup.find_all("ul", {"class":"cardDeck cardGrid"})

		list = []

		for ultag in x:
			for y in ultag.find_all("li"):
				y = y.text.replace("Add to list ", "").replace("\n", "")
				list.append(y)
		
		return list