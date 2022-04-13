from bs4 import BeautifulSoup
import requests

response= requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_archive =response.text

soup = BeautifulSoup(web_archive, "html.parser")
movies = soup.find_all(name="h3", class_="title")


movie_list = [movie.getText() for movie in movies]
with open("movie_list.txt", "w") as f:
        f.write('\n' .join(movie_list))
f.close()
print("Done")

