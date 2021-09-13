"""
=====================
Get anime related stuff.
=====================
"""

import requests
from bs4 import BeautifulSoup
from AniManga.helpers.helpers import format_

class Anime:
    def __init__(self, verbose=False):
        """__init__
        """
        self.base_url = "https://www.anime-planet.com/anime/"
    
    def get_anime_json(self, anime: str) -> dict:
        """Get anime dict/json data.
        Args:
            anime (str): anime you want to search for.

        Returns:
            dict: dict/json object with data of anime.
        """
        r = requests.get(self.base_url + format_(anime))
        s = BeautifulSoup(r.content,"html5lib")
        anime_json = {}
        anime_json["title"] = s.find("meta",property="og:title")["content"]
        anime_json["url"] = s.find("meta",property="og:url")["content"]
        anime_json["cover url"] = s.find("meta",property="og:image")["content"]
        anime_json["description"] = s.find("meta",property="og:description")["content"]
        anime_json["keywords"] = s.find("meta", attrs={"name":"keywords"})["content"].split(", ")
        tags = s.find_all("div",{"class":"tags"})
        tags_list = []
        for x in tags:
            x = x.find_all("a")
            for y in x:
                y = y.text.replace("\n","")
                tags_list.append(y)
        anime_json["tags"] = tags_list
        section_bar = s.find("section",{"class":"pure-g entryBar"})
        _div = section_bar.find_all("div",{"class":"pure-1 md-1-5"})
        _section_bar_list = []
        for y in _div:
            y = y.text.replace("\n","")
            _section_bar_list.append(y)
        anime_json["episodes"] = _section_bar_list[0]
        anime_json["studio"] = _section_bar_list[1]
        anime_json["year"] = _section_bar_list[2]
        anime_json["rating"] =  _section_bar_list[3]
        anime_json["rank"] = _section_bar_list[4]
        r = requests.get(f"https://www.anime-planet.com/anime/{format_(anime)}/reviews")
        s = BeautifulSoup(r.content,"html5lib")

        review = s.find_all("div",{"class":"pure-1 userContent readMore"})

        review_list = []

        for x in review:
            review_list.append(x.text)
        anime_json["reviews"] = review_list

        return anime_json