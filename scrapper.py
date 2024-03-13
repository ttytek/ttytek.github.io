import requests
import re
import time
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from googlesearch import search


def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())


def search_duckduckgo(query):
    data=[]
    url = f"https://duckduckgo.com/html/?q={query}&ia=web"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    while response.status_code != 200:
        response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('a', class_='result__a')
    for result in results:
        if len(data) >=5:
            break
        data.append({'title': result.text, 'link': result['href']})

    return data


r = requests.get('https://www.thechesswebsite.com/chess-openings/')
test_string='<h5>Adelaide Counter Gambit</h5>'
regex = r'<h5>(.*)<\/h5>'
#regex = re.compile('.*')
matches = re.findall(regex, r.text)
#print(matches)
markdown = ''
prev_title=None
count = 0

xd="---\n---\n"
first='Larsens'
with open('list.md', 'w') as index:
    index.write(xd)
    for el in matches:
        if(el<first):
            print(f'skipped {el}')
            continue
        print(f'at {el}')
        subpage=el
        index.write(f'<span style="font-size:larger;">[{el}](/{subpage}.html)</span><br>\n')

        with open(subpage+'.md', 'w') as sp:
            sp.write(xd)
            try:
                data = search(el, stop=5)
                for url in data:
                    response = requests.get(url)
                    tries=0
                    while response.status_code != 200:
                        tries = tries+1
                        if tries>10:
                            break
                        time.sleep(3)
                        response = requests.get(url)
                    if tries>10:
                        continue
                    title = BeautifulSoup(response.content, "html.parser").title.text.strip()
                    if title != prev_title:
                        sp.write(f'[{title}]({url})<br>')
                    prev_title=title
            except:
                pass




