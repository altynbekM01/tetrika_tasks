import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import time
import csv

BASE_URL = "https://ru.wikipedia.org"
START_URL = f"{BASE_URL}/wiki/Категория:Животные_по_алфавиту"

HEADERS = {
    'User-Agent': 'Mozilla/5.0'
}

def parse_letter_counts():
    url = START_URL
    letter_counts = defaultdict(int)
    page_count = 0

    while url:
        print(f" Страница {page_count + 1}: {url}")
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        category_div = soup.select_one(
            'div.mw-category-generated > #mw-pages > div.mw-content-ltr > div.mw-category.mw-category-columns'
        )
        if not category_div:
            print("Структура не найдена")
            break

        for group in category_div.select('div.mw-category-group'):
            h3 = group.find('h3')
            ul = group.find('ul')
            if h3 and ul:
                letter = h3.get_text(strip=True)
                if re.fullmatch(r'[А-ЯЁ]', letter):
                    li_count = len(ul.find_all('li'))
                    letter_counts[letter] += li_count

        next_link = soup.find('a', string="Следующая страница")
        if next_link and next_link.get("href"):
            url = BASE_URL + next_link['href']
            page_count += 1
            time.sleep(0.5)
        else:
            break

    return letter_counts

if __name__ == "__main__":
    counts = parse_letter_counts()

    print("\n Подсчёт по буквам:")
    for letter in sorted(counts):
        print(f"{letter}: {counts[letter]}")

    with open("beasts.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for letter in sorted(counts):
            writer.writerow([letter, counts[letter]])

    print("\n Данные сохранены в файл beasts.csv")
