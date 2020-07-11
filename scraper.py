from lxml import html
from datetime import datetime
from timeit import default_timer

import requests
import time


def main(page_start: int, page_end: int):
    start_time = default_timer()
    all_sold_cars_hrefs = []
    page_number = page_start

    while page_number != page_end + 1:
        print(f'Scraping page {page_number}')
        page = requests.get(f'https://autoplius.lt/skelbimai/naudoti-automobiliai?page_nr={page_number}', headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
        tree = html.fromstring(page.content)
        sold_cars_hrefs = tree.xpath('//a[@class="announcement-item is-sold is-inactive"]')
        sold_cars_photos = tree.xpath(
            '//a[@class="announcement-item is-sold is-inactive"]/div[@class="announcement-media"]/div[@class="announcement-photo"]/img[1]')
        sold_cars_prices = tree.xpath(
            '//a[@class="announcement-item is-sold is-inactive"]/div[@class="announcement-body"]/div[@class="announcement-pricing-info"]/strong')
        sold_cars_titles = tree.xpath(
            '//a[@class="announcement-item is-sold is-inactive"]/div[@class="announcement-body"]/div[@class="announcement-title"]')
        for i in range(len(sold_cars_hrefs)):
            href = sold_cars_hrefs[i].attrib.get('href')
            image_src = sold_cars_photos[i].attrib.get('data-src')
            price = sold_cars_prices[i].text.strip()
            title = sold_cars_titles[i].text.strip()
            print(f'Page {page_number}. Sold car href:{href}. Image url: {image_src}. Price: {price}. Title: {title}')
            all_sold_cars_hrefs.append(f'{href} {title} {price} {image_src}')
        page_number += 1

    all_sold_cars_hrefs.sort()
    f = open(f"cars/sold-cars-{datetime.utcnow()}.txt", "a")
    for car_href in all_sold_cars_hrefs:
        f.write(f'{car_href}\n')
    f.close()
    elapsed = default_timer() - start_time
    print('Elapsed time in seconds: ', elapsed)


main(page_start=1, page_end=1975)
