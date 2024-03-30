import httpx
from parsel import Selector

MAIN_URL = "https://www.mashina.kg/search/all/"
BASE_URL = "https://www.mashina.kg"


def get_html(url):
    response = httpx.get(url)
    # return response.text
    return Selector(response.text)


def get_title(html):
    title = html.css("title::text").get()
    return title


def get_car_links(html):
    cars = html.css(".list-item a::attr(href)").getall()
    links = list(map(lambda x: BASE_URL + x, cars))
    return links


def get_car_data(html):
    data = []
    cars = html.css(".list-item a")
    for car in cars:
        current_car = {}
        title = car.css(".title .name::text").get()
        current_car["title"] = title.strip().replace("\n", "")
        price = car.css(".price strong::text").get()
        current_car["price"] = int(price.strip().replace(" ", "").replace("$", ""))
        data.append(current_car)
        # Save to DB or CSV

    return data


def paginate(from_page, to_page):
    for page in range(from_page, to_page):
        yield f"{MAIN_URL}?page={page}"

    # def get_cars():


#     """Получаем только ссылки на объявления"""
#     links = []
#     for url in paginate(1, 2):
#         html = get_html(url)
#         cars = get_car_links(html)
#         links.extend(cars)

#     return links

def get_cars():
    """Получаем данные об объявлениях"""
    data = []
    for url in paginate(1, 2):
        html = get_html(url)
        cars = get_car_data(html)
        data.extend(cars)

    return data



print(get_cars())