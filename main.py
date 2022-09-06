from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
title_list = soup.find_all(name="a", class_="titlelink")
title_points = soup.find_all(name="span", class_="score")
# print(title_points)

articles = {int(points.getText().rstrip(" points")): [news.getText(), news.get("href")] for news, points
            in zip(title_list, title_points)}

list_articles = sorted(list(articles), reverse=True)

for article in list_articles:
    print(f"Article Title = {articles[article][0]}\n"
          f"Article Link = {articles[article][1]}\n"
          f"Points = {article}\n")
# print(list_articles)

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
