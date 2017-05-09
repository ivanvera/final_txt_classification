# coding=UTF-8
import codecs
import sys

import jieba.posseg as pseg

sys.path.append("../")
import json
from feature_extractor.entity.document import Document

reload(sys)
sys.setdefaultencoding('utf-8')

data = codecs.open("../file/total_corpus1000.json", "r", "utf-8")
result = codecs.open("../file/keywords_corpus.json", 'w', 'utf-8')

title_set = set()
index = 0


def get_cut(content):
    result_list = []
    words = pseg.cut(content)
    for word, flag in words:
        result_list.append(word + '_' + flag)
    return result_list


for line in data:
    if index % 100 == 0:
        print index
    index += 1
    json_dic = dict()

    document = Document(line.strip())
    title = document.title
    raw_content = document.get_raw_content()
    if raw_content.endswith(title.replace(' ', '')):
        raw_content = raw_content[:raw_content.index(title.replace(' ', ''))]

    json_dic['split_title'] = get_cut(title)
    json_dic['split_content'] = get_cut(raw_content)
    json_dic['title'] = title
    json_dic['content'] = raw_content

    json_data = json.dumps(json_dic, encoding="utf-8", ensure_ascii=False)

    result.write(json_data + '\n')

data.close()
result.close()
