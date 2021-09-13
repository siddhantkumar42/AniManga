from bs4 import BeautifulSoup
import requests

class MAL:
    def __init__(self):
        self.base_url = "https://myanimelist.net/"
    
    def get_user_json(self, user: str) -> dict:
        """Get json/dict info on an MAL user.

        Args:
            user (str): MAL user you want to search for.

        Returns:
            dict: MAL user info.
        """
        r = requests.get(self.base_url + "profile/" + user)
        s = BeautifulSoup(r.content, "html5lib")
        user_dict = {}
        user_dict["username"] = s.find("title").text.replace("'s Profile - MyAnimeList.net","").replace("\n","")
        stats_list = []
        stats = s.find_all("span",{"class":"di-ib fl-r lh10"})
        for x in stats:
            stats_list.append(x.text)
        user_dict["stats"] = {}
        user_dict["stats"]["anime"] = {}
        user_dict["stats"]["anime"]["watching"] = stats_list[0]
        user_dict["stats"]["anime"]["completed"] = stats_list[1]
        user_dict["stats"]["anime"]["on hold"] = stats_list[2]
        user_dict["stats"]["anime"]["dropped"] = stats_list[3]
        user_dict["stats"]["anime"]["plan to watch"] = stats_list[4]
        user_dict["stats"]["manga"] = {}
        user_dict["stats"]["manga"]["reading"] = stats_list[5]
        user_dict["stats"]["manga"]["completed"] = stats_list[6]
        user_dict["stats"]["manga"]["on hold"] = stats_list[7]
        user_dict["stats"]["manga"]["dropped"] = stats_list[8]
        user_dict["stats"]["manga"]["plan to read"] = stats_list[9]
        user_dict["joined"] = s.find("span",{"class":"user-status-data di-ib fl-r"}).text
        user_dict["mean score"] = s.find("div",{"class":"di-tc ar pr8 fs12 fw-b"}).text.replace("\n","").replace(" ","")
        user_dict["days"] = s.find("div", {"class":"di-tc al pl8 fs12 fw-b"}).text
        return user_dict

    def get_all_mal_news(self, pages: int = 1, description: bool = False) -> list:
        """Get anime news from MAL. Set description = True to get news description.

        Args:
            pages (int, optional): Number of pages you want the news for. More pages = Slower code. Defaults to 1.
            description (bool, optional): If you want to get news description. Defaults to False.

        Returns:
            list: news.
        """

        if description:
            news_list = []
            n = 1
            for i in range(int(pages)):
                r = requests.get("https://myanimelist.net/news?p={}".format(n))
                s = BeautifulSoup(r.content, "html5lib")
                x = s.find_all("div",{"class":"news-unit clearfix rect"})
                news_list = []
                for i in x:
                    news_dict = {}
                    news_dict[i.find("p",{"class":"title"}).text.replace("\n","")] = i.find("div",{"class":"text"}).text.replace("\n","")
                    news_list.append(news_dict)
                n += 1

        else:
            news_list = []
            n = 1
            for i in range(int(pages)):
                r = requests.get("https://myanimelist.net/news?p={}".format(n))
                s = BeautifulSoup(r.content, "html5lib")
                x = s.find_all("p",{"class":"title"})
                for i in x:
                    news_list.append(i.text.replace("\n",""))
                n += 1

        return news_list

