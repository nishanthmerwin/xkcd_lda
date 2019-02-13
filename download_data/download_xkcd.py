

import json
import requests
from tqdm import tqdm, trange

base = 'http://xkcd.com/'
tail = 'info.0.json'

all_comics = []

for i in trange(1,2103):
    url = f'{base}{i}/{tail}'
    try:
        data = requests.get(url).json()
    except Exception as e:
        print(e)
        print(url)
        continue
    data['url'] = url
    all_comics.append(data)

with open("../data/all_comics.json", "w") as fp:
    json.dump(all_comics, fp)
