import requests
from bs4 import BeautifulSoup as bs

url = "https://news.ycombinator.com/"
response = requests.get(url)
content = bs(response.text, "html.parser")
articles = []

for item in content.find_all('tr', class_='athing'):

    # get all <a> in athing
    for item_span in item.find_all('span', class_='titleline'):
        item_a = item_span.find('a').get('href')
        item_text = item_span.find('a').getText(strip=True)
        articles.append(item_a)
        articles.append(item_text)
    # get next <tr>
    next_row = item.find_next_sibling('tr')
    # get all items in subtext
    for subtext in next_row.find_all('td', class_='subtext'):
        subtext_score = subtext.find('span', class_='score')
        subtext_score_text = subtext_score.getText(strip=True) if subtext_score else "0 points"
        articles.append(subtext_score_text)

for art in range(0, len(articles), 3):
    art_dict = {
        'link': articles[art], 'title': articles[art + 1], 'score': articles[art + 2]
    }
    print(art_dict)
