from lxml import html
from datetime import datetime

import requests

page_number = 1
total_pages = 5
all_sold_cars_hrefs = []

while page_number != total_pages:
    page = requests.get(f'https://autoplius.lt/skelbimai/naudoti-automobiliai?page_nr={page_number}')
    tree = html.fromstring(page.content)
    sold_cars = tree.xpath('//a[@class="announcement-item is-sold is-inactive"]')
    for car in sold_cars:
        href = car.attrib.get('href')
        print(f'Page {page_number}. Sold car href:', car.attrib.get('href'))
        all_sold_cars_hrefs.append(href)
    page_number += 1

f = open(f"cars/sold-cars-{datetime.utcnow()}.txt", "a")
for car_href in all_sold_cars_hrefs:
    f.write(f'{car_href}\n')
f.close()
