"""
=====================
Get hentai/doujin related stuff.
=====================
"""

import requests
from bs4 import BeautifulSoup

class Doujin:
    """
    Scrapes nhentai.net for doujin information.
    """
    def __init__(self, verbose=False):
        """
        __init__ function.
        """
        self.base_doujin_url = "https://nhentai.net/"
        self.verbose = verbose
    
    def get_doujin_json(self, code: int) -> dict:
        """Get information on a doujin from nhentai.net in dict/json format.

        Args:
            code (int): the ~6 digit code used to uniquely identify doujins.

        Returns:
            dict: dict/json with doujin information.
        """
        code = str(code)
        r = requests.get(self.base_doujin_url + "g/" + code)
        s = BeautifulSoup(r.content, "html5lib")
        if s.find("div",{"class":"container error"}):
            return "Error: Doujin '{}' most likely doesnt exist.".format(code) if not self.verbose else "Error: Doujin '{}' most likely doesnt exist. Possible fixes might be rechecking the name.".format(code)
        else:
            doujin_dict = {}
            doujin_dict["title"] = s.find("meta", property="og:title")["content"]
            doujin_dict["image"] = s.find("meta", property="og:image")["content"]
            doujin_dict["tags"] = s.find("meta",attrs={"name":"twitter:description"})["content"].split(", ")
            doujin_dict["description"] = s.find("meta", attrs={"name":"description"})["content"]
            other_info = s.find_all("div",{"class":"tag-container field-name"})
            other_info_list = []
            for i in other_info:
                i = i.find_all("span",{"class":"name"})
                other_info_list.append(i)
            doujin_dict["artist"] = other_info_list[1][0].text
            languages = []
            for i in other_info_list[2]:
                languages.append(i.text)
            doujin_dict["languages"] = languages
            doujin_dict["type"] = other_info_list[3][0].text
            doujin_dict["pages"] = other_info_list[4][0].text
            return doujin_dict