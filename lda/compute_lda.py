

import json
import gensim
from gensim import corpora, models
from tqdm import tqdm

with open("../data/lemma_text.json") as fp:
    comics = json.load(fp)


comics = [x for x in comics if "lemmed_text" in x]
processed_docs = [x['lemmed_text'] for x in comics]

dictionary = gensim.corpora.Dictionary(processed_docs)
dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)

bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]



print("Running LDA")
lda_model = gensim.models.LdaMulticore(corpus_tfidf, num_topics=10, id2word=dictionary, passes=40, workers=6)
print("Done LDA")

topics = []
for i in range(10):
    words = lda_model.get_topic_terms(i)
    word_names = [dictionary[x[0]] for x in words]
    topic = dict(index=i, words=word_names)
    topics.append(topic)

print(json.dumps(topics, indent=4))

with open("../data/topics.json", "w") as fp:
    json.dump(topics, fp)


for i, document in enumerate(tqdm(corpus_tfidf)):
    comic = comics[i]
    scores = [dict(topic=x[0],score=float(x[1])) for x in lda_model[document]]
    comic['scores'] = scores


with open("../data/annotated_comics.json", "w") as fp:
    json.dump(comics, fp)


