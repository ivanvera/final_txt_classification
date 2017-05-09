# coding=UTF-8
import codecs
import sys

sys.path.append("../")
from feature_extractor.entity.document import Document
from config.config import FilePathConfig
from util.util import Util

reload(sys)
sys.setdefaultencoding('utf-8')

data = codecs.open("../file/total_corpus.json", "r", "utf-8")
result = codecs.open("../file/total_corpus_new.json", 'w', 'utf-8')
category = Util.load_object_from_pkl(FilePathConfig.category_pkl_path)

title_set = set()
index = 0
for line in data:
    if index % 10000 == 0:
        print index
    index += 1

    document = Document(line.strip())
    title = document.title
    label = document.label
    if label not in category.keys():
        print label
        continue
    result.write(line)
    # if title is None or label is None:
    #     continue
    #
    # if title + label in title_set:
    #     print title, label
    #     continue
    # title_set.add(title + label)
    #
    # json_data = document.json
    # raw_content = document.get_raw_content()
    # words = document.get_filtered_content_words_feature()
    # source = document.source
    #
    #
    # words.append(source)
    # words = ','.join(words)
    #
    # result.write(json_data + '\t' + words + '\t' + raw_content + '\t' + label + '\n')

data.close()
# result.close()
