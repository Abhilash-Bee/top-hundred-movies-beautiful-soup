from bs4 import BeautifulSoup
import requests
import html

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/"
                            "best-movies-2/")
movies_from_website = response.text

soup = BeautifulSoup(movies_from_website, "html.parser")
movies_list = soup.find_all(name="h3", class_="title")

movies_item = [movie.getText() for movie in movies_list]
with open("movies.txt", "a", encoding="utf-8") as file:
    for movie in reversed(movies_item):
        file.write(f"{html.unescape(movie)}\n")
