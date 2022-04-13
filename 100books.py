from bs4 import BeautifulSoup
import requests

response= requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/books/features/best-books-2/")
web_archive =response.text

soup = BeautifulSoup(web_archive, "html.parser")
books = soup.find_all(name="h3", class_="title")


book_list = [book.getText() for book in books]
with open("book_list.txt", "w") as f:
        f.write('\n' .join(book_list))
f.close()
print("Done")

