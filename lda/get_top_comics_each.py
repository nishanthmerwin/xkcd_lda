
import json

with open("../data/topics.json") as fp:
    topics = json.load(fp)

with open("../data/annotated_comics.json") as fp:
    comics = json.load(fp)

for comic in comics:

    score_map = {}
    for score in comic['scores']:
        score_map[score['topic']] = score['score']
    if len(score_map) != 10:
        for i in range(10):
            if i not in score_map:
                score_map[i] = 0.0
    comic['score_map'] = score_map


for topic in topics:

    index = topic['index']
    words = topic['words']

    comics = sorted(comics, key=lambda x:x['score_map'][index])[::-1]
    top_5 = comics[:5]
    print(index, words)
    for comic in top_5:
        print(comic['img'], comic['score_map'][index])
    input()
