

import json
import requests
from tqdm import tqdm, trange
from bs4 import BeautifulSoup
import bs4
from pathlib import Path

base = 'http://xkcd.com/'
tail = 'info.0.json'

base = 'https://www.explainxkcd.com/wiki/index.php/'
all_comics = []


def get_transcript(soup):
    theader = soup.find(id="Transcript").parent
    descriptions = []
    for sibling in theader.next_siblings:
        if type(sibling) == bs4.element.NavigableString:
            continue
        hits = sibling.find_all("dd")
        if len(hits) == 0:
            break
        descriptions.append([])
        for hit in hits:
            descriptions[-1].append(hit.text)
    return descriptions

def get_explanation(soup):
    theader = soup.find(id="Explanation").parent
    explanation = []
    for sibling in theader.next_siblings:
        if type(sibling) == bs4.element.NavigableString:
            continue
        if sibling.name != "p":
            continue
        text = sibling.get_text().strip()
        if len(text) == 0:
            continue
        explanation.append(text)
        if "h" in sibling.name:
            break
    return explanation

base_dir = Path("../data/explained_comics")

for i in trange(1,2103):
    outpath = base_dir / f'{i}.json'
    if outpath.exists():
        continue
    url = f'{base}{i}'
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    try:
        descriptions = get_transcript(soup)
        explanation = get_explanation(soup)
    except Exception as e:
        print(e)
        continue
    comic = dict(url=url, index=i, transcript=descriptions, explanation=explanation)
    with outpath.open("w") as fp:
        json.dump(comic, fp)



