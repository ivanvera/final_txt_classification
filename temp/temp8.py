# coding=UTF-8
import codecs
import sys

from feature_extractor.entity.document import Document

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')

data = codecs.open("total_corpus.json", "r", "utf-8")
result = codecs.open("total_corpus_new.json", 'w', 'utf-8')
title_set = set()
index = 0
for line in data:
    if index % 10000 == 0:
        print index
    index += 1

    document = Document(line.strip())
    title = document.title

    if title in title_set:
        print title
        continue

    json_data = document.json
    raw_content = document.get_raw_content()
    words = document.get_filtered_content_words_feature()
    source = document.source
    label = document.label

    words.append(source)
    words = ','.join(words)

    result.write(json_data + '\t' + words + '\t' + raw_content + '\t' + label + '\n')

data.close()
result.close()
