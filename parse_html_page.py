from bs4 import BeautifulSoup
import urllib.request


req = urllib.request.urlopen('https://www.ua-football.com/sport')
print(req)

html = req.read()
# print(html)

soup = BeautifulSoup(html, features='html.parser')
# print(soup)

news = soup.find_all('li', class_='liga-news-item')
# print(news)

results = []
for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True)
    description = item.find('span', class_='name-dop').get_text(strip=True)
    href = item.a.get('href')

    # print(title, description, href, sep="\n", end="\n\n")
    results.append({
        "title": title,
        "description": description,
        "href": href,
    })


print(results)

f = open('news.txt', 'w', encoding="utf-8")
for index, item in enumerate(results):
    f.write(f"{index}. {item['title']}\n\t{item['description']}\n\t{item['href']}\n\n")















