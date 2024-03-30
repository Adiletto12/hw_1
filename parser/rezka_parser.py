import requests
from bs4 import BeautifulSoup as BS

URL = "https://vibish.com"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}


# start
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


# get data
def get_data(html):
    bs = BS(html, "html.parser")
    items = bs.find_all("div", class_='SdPosition mainbody')
    rezka_list = []
    for item in items:
        title = item.find("div", class_="name").get_text(strip=True)
        image = URL + item.find("div", class_="js-bigImg").find("img").get("src")
        rezka_list.append({"title": title, "image": image})
    return rezka_list


# parsing
def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        rezka_list_2 = []
        for page in range(1, 2):  # измените диапазон, чтобы начать с 1
            response = get_html('https://vibish.com/expensive', params={'page': page})  # передайте параметры правильно
            rezka_list_2.extend(get_data(response.text))
        return rezka_list_2
    else:
        raise Exception('Ошибка при парсинге')

print(parsing())



