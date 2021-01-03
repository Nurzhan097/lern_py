from bs4 import BeautifulSoup
import urllib.request


class Parser:

    raw_html = ""
    html = ""
    results = []

    def __init__(self, url, file_path):
        self.url = url
        self.file_path = file_path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, features='html.parser')

    def parsing(self):
        self.results = []
        news = self.html.find_all('li', class_='liga-news-item')
        for item in news:
            title = item.find('span', class_='d-block').get_text(strip=True)
            description = item.find('span', class_='name-dop').get_text(strip=True)
            href = item.a.get('href')

            # print(title, description, href, sep="\n", end="\n\n")
            self.results.append({
                "title": title,
                "description": description,
                "href": href,
            })

    def save(self):
        with open(self.file_path, 'w', encoding="utf-8") as f:
            for index, item in enumerate(self.results):
                f.write(f"{index}. {item['title']}\n\t{item['description']}\n\t{item['href']}\n\n")

    def run(self):
        self.get_html()
        self.parsing()
        self.save()


# parser = Parser("https://www.ua-football.com/sport", "pars.txt")
# parser.run()
# print(parser.results)







