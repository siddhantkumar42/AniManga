from setuptools import setup, find_packages
import codecs
import os

with open("README.md") as f:
    LONGDESCRIPTION = f.read()

VERSION = "0.0.10"
DESCRIPTION = "AniManga is a python module which scrapes the web to get information on Anime, Manga (and hentai)."

# Setting up
setup(
    name="AniManga",
    version=VERSION,
    author="Siddhant Kumar",
    author_email="centipedemonster@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONGDESCRIPTION,
    packages=find_packages(),
    install_requires=["bs4"],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
