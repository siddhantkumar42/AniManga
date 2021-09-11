# Docs for AniManga - Manga

## Importing:

```py
>>> from AniManga import Manga
```

## Functions:


### `get_manga_json`

```
Get information on a manga.

        Args:
            manga (str): manga name you want to search for.

        Returns:
            dict: dict with information on the manga.
```
```py
print(Manga().get_manga_json("naruto"))
```
```
{'title': '', 'description': '', 'url': '', 'type': '', 'size': '', 'year': '', 'rating': '', 'rank': '', 'author': '', 'cover': '', 'tags': [], 'content warning': [], 'characters': [], 'reviews': []}
```
- Note: The list it returns is huge, and has been shortened for sake of better presentation.

### `get_manga_description`

```
Gets description of a manga. Use get_manga_json to get a faster execution.

        Args:
            manga (str): manga for which description you need.

        Returns:
            str: description of the manga.
```
```py
print(Manga().get_manga_description("naruto"))
```
```
Once, the ninja village of Konohagakure was attacked by an evil nine-tailed fox spirit. This demon slaughtered many people until the leader of Konohagakure, ...
```
- Note: Description shortened for better presentation.

## `get_manga_url`

```
Get Anime-Planet URL of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: Anime-Planet URL.
```
```py
print(Manga().get_manga_url("naruto"))
```
```
https://www.anime-planet.com/manga/naruto
```

## `get_manga_size`

```
Get the chapters/volume of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: chapters/volume numbers.
```
```py
print(Manga().get_manga_size("naruto"))
```
```
Vol: 72; Ch: 700
```

## `get_manga_year`

```
Get the years a manga ran.

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: years the manga ran.
```
```py
print(Manga().get_manga_year("naruto"))
```
```
 1999 - 2014 
 ```

## `get_manga_rating`

```
Get the rating of a manga

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: the rating.
```
```py
print(Manga().get_manga_rating("naruto"))
```
```
4.486 out of 5 from 21,643 votes
```

## `get_manga_rank`

```
Get the rank of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: the rank.
```
```py
print(Manga().get_manga_rank("naruto"))
```
```
Rank #860
```

## `get_manga_cover`

```
Get the cover image url of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: cover image url. 
```
```py
print(Manga().get_manga_cover("naruto"))
```
```
https://www.anime-planet.com/images/manga/covers/83.jpg?t=1395061673
```

## `get_manga_author`

```
Get the author of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: author.
```
```py
print(Manga().get_manga_author("naruto"))
```
```
masashi-kishimoto
```

## `get_manga_tags`

```
Get the tags of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            list: tags of the manga.
```
```py
print(Manga().get_manga_tags("naruto"))
```
```
['Action', 'Comedy', 'Drama', 'Fantasy', 'Shounen', 'Hand to Hand Combat', 'Japanese Mythology', 'Ninja', 'Revenge', 'Rivalries', 'Weak to Strong', 'Adapted to Anime', 'Violence']
```

## `get_manga_content_warning`

```
Get the content warning of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            list: content warning.
```
```py
print(Manga().get_manga_content_warning("naruto"))
```
```
['Violence']
```

## `get_manga_reviews`

```
Get the reviews of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            list: reviews of the manga.
```
```py
print(Manga().get_manga_reviews("naruto"))
```
```
["I've had to reserve judgement until the final ending came out. Now that it is here, I can safety and without a doubt state that the manga is not worth it.\n", "This series hates me.\xa0 For the last four or so years, I've\njust been coming back to Naruto over and over hoping things will get\nbetter, but it just keeps hurting and tormenting me.\n", ...]
```
- Note: Again, list has been shortened for presentation.

## `get_manga_characters`

```
Get the characters of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            list: characters.
```
```py
print(Manga().get_manga_characters("naruto"))
```
```
['Kakashi HATAKE', 'Naruto UZUMAKI', 'Sakura HARUNO', 'Sasuke UCHIHA', 'Asuma SARUTOBI', 'Choji AKIMICHI', 'Danzo SHIMURA', 'Deidara', 'Gaara', 'Hidan', 'Hinata HYUGA', 'Hiruzen SARUTOBI', 'Ino YAMANAKA', 'Itachi UCHIHA', 'Jiraiya', ...]
```
- Note: List shortened for presentation.

## `get_popular_manga`

```
Get currently popular manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            list: popular manga.
```
```py
print(Manga().get_popular_manga())
```
```
["Solo Leveling", ...]
```
- Note: I skipped most of the parts the list returns as it frequently changes.