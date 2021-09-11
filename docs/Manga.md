# Docs for AniManga - Manga

## Importing:

```py
from AniManga import Manga
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

### `get_manga_description`

```
Gets description of a manga. Use get_manga_json to get a faster execution.

        Args:
            manga (str): manga for which description you need.

        Returns:
            str: description of the manga.
```

## `get_manga_url`

```
Get Anime-Planet URL of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: Anime-Planet URL.
```

## `get_manga_size`

```
Get the chapters/volume of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: chapters/volume numbers.
```

## `get_manga_year`

```
Get the years a manga ran.

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: years the manga ran.
```

## `get_manga_rating`

```
Get the rating of a manga

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: the rating.
```

## `get_manga_rank`

```
Get the rank of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: the rank.
```

## `get_manga_cover`

```
Get the cover image url of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: cover image url. 
```

## `get_manga_author`

```
Get the author of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            str: author.
```

## `get_manga_tags`

```
Get the tags of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            list: tags of the manga.
```

## `get_manga_content_warning`

```
Get the content warning of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            list: content warning.
```

## `get_manga_reviews`

```
Get the reviews of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            list: reviews of the manga.
```

## `get_manga_characters`

```
Get the characters of a manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            list: characters.
```

## `get_popular_manga`

```
Get currently popular manga.

        Args:
            manga (str): manga you want to search for.

        Returns:
            list: popular manga.
```

## Notes

- Examples will be added soon.