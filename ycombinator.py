import requests
from bs4 import BeautifulSoup
import lxml
import csv

def get_article_and_link(url_link , filename):

    
    request = requests.get(url_link)

    soup = BeautifulSoup(request.text, "lxml")

# heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]

# for tags in soup.find_all(heading_tags):
#     print(tags.text)

    article_title_list = ["ARTICLE TITLE"]
    article_link_list = ["ARTICLE LINKS"]


    for article in soup.select(".titlelink"):
        article_title_list.append(article.text)
        article_link_list.append(article.get('href'))

    with open(filename, 'w', encoding='UTF8', newline="") as f:
        writer = csv.writer(f)
        for article in zip(article_title_list, article_link_list):
            writer.writerow(article)

    print("Done")

get_article_and_link("https://news.ycombinator.com/news", "ycombinatornews.csv")
get_article_and_link("https://news.ycombinator.com/jobs", "ycombinatorjobs.csv")
# print(len(href_list), len(link_list))

# paragraph_tag = ["p"]
# for paragraph in soup.find_all(paragraph_tag):
#     print(paragraph.text)

