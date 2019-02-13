
import json
from tqdm import tqdm
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
from pathlib import Path
import itertools
import nltk

np.random.seed(2018)


with open("../data/all_comics.json") as fp:
    comics = json.load(fp)

explained_dir = Path("../data/explained_comics")

stemmer = SnowballStemmer("english")
def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result

for comic in tqdm(comics):
    comic_num = comic['num']
    transcript_path = explained_dir / f'{comic_num}.json'
    if not transcript_path.exists():
        continue
    with transcript_path.open() as fp:
        comic['explained'] = json.load(fp)
    all_text = []
    title = comic['safe_title']
    transcript = comic['explained']['transcript']
    transcript = list(itertools.chain(*transcript))
    for line in transcript:
        all_text += line.split(" ")
    explanation = comic['explained']['explanation']
    for line in explanation:
        all_text += line.split(" ")
    all_text += comic['safe_title'].split(" ")
    all_text = preprocess(" ".join(all_text))
    comic['lemmed_text'] = all_text

with open("../data/lemma_text.json", "w") as fp:
    json.dump(comics, fp)

