import requests
import re
from bs4 import BeautifulSoup


def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(index, title, link):
    print("{}. {}".format(index + 1, title))
    print("  (링크 : {})".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    print()
    url ="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%B2%9C%EC%95%88+%EB%82%A0%EC%94%A8&oquery=%EC%B2%9C%EC%95%88+%EB%82%A0%EC%94%A8&tqi=hkKxSsp0YiRsslVDBSCssssssw0-139860"
    soup = create_soup(url)
    # 흐림, 어제보다 00˚ 높아요
    cast = soup.find("div", attrs={"class":"temperature_info"}).get_text()
    # 현재 00˚C (최저 00˚ / 최고 00˚)
    curr_temp = soup.find("div", attrs={"class":"weather_graphic"}).get_text().strip()  # 현재 기온
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text()  # 최저 온도
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text()  # 최고 온도
    # 오전 강수확률 00% / 오후 강수확률 00%
    morning_rain_rate = soup.find("div", attrs={"class":"cell_weather"}).get_text()  # 오전,오후 강수 확률

    # 미세먼지 00㎍ / ㎥좋음
    dust = soup.find("ul", attrs={"class":"today_chart_list"})
    pm10 = dust.find_all("li")[0].get_text()  # 미세먼지
    pm25 = dust.find_all("li")[1].get_text()  # 초미세먼지
    # 초미세머지 00㎍ / ㎥좋음

    # 출력
    print(cast)
    print("{} ({} / {})".format(curr_temp, min_temp, max_temp))
    print("{}".format(morning_rain_rate))
    print()
    print("{}".format(pm10))
    print("{}".format(pm25))
    print()

def scrape_headline_news():  # 네이버 헤드라인 뉴스 가져오기
    print("[헤드라인 뉴스]")
    print()
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs = {"class":"hdline_article_list"}).find_all("li", limit=3)  # 3개의 기사만 가져오기
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    print()
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)  # 3개의 기사만 가져오기
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 img태그의 정보를 사용

        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    print()
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:  # 8문장이 있다고 가정 할때, index 기준 4~7 까지 잘라서 가져옴
        print(sentence.get_text().strip())

    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:  # 8문장이 있다고 가정 할때, index 기준 0~4 까지 잘라서 가져옴
        print(sentence.get_text().strip())
    print()


if __name__ == '__main__':
    scrape_weather()  # 오늘의 날씨 정보 가져오기
    scrape_headline_news()  # 헤드라인 뉴스 정보 가져오기
    scrape_it_news()  # IT 뉴스 정보 가져오기
    scrape_english()  # 오늘의 영어 회화 가져오기
