# AniManga 

AniManga is a python module which scrapes the web to get information on Anime, Manga (and hentai).

## Installation

```
python3 -m pip install AniManga
```

## Manga
- Get description, author, cover page and reviews of a Manga by name.

### Example:

```py
from AniManga import Manga

manga_description = Manga().get_manga_description("naruto")

print(manga_description)
```

Output:
```
'Once, the ninja village of Konohagakure was attacked by an evil nine-tailed fox spirit. This demon slaughtered many people until the leader of Konohagakure, the 4th Hokage, sacrificed his life to seal the fox inside a newborn child - Naruto Uzumaki. Now, twelve years later, Naruto is a member of the Ninja Academy; but due to his past Naruto is shunned by the rest of the village, and since he has no friends or family he plays the part of class idiot to get attention. However, he is determined to gain respect by becoming the next Hokage - the most powerful shinobi in the village. With his apparent lack of abilities, will Naruto be able to realize his goal through determination alone?'
```

Detailed docs will soon be available.

## Acknowledgement
### Sites scraped:
- [Anime-Planet](https://animeplanet.com)
