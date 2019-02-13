
import json
import requests
import shutil
from pathlib import Path
from tqdm import tqdm


with open("../data/all_comics.json") as fp:
    comics = json.load(fp)

img_dir = Path("../data/img")

for comic in tqdm(comics):
    url = comic['img']
    num = comic['num']
    response = requests.get(url, stream=True)
    img_path = img_dir / f'{num}.jpg'
    with img_path.open("wb") as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
