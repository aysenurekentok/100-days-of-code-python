import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movies_list = [movie.getText().split(" ", 1)[1] for movie in movies]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies_list[::-1]:
        file.write(f"{movies_list[::-1].index(movie) + 1}) {movie}\n")
