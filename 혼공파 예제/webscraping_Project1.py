import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs = {"class":"hdline_article_list"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        title = news.fine("a").get_text()
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("  (링크 : {})".format(link))
    print()