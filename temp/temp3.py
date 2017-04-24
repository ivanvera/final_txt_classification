# coding=UTF-8
import codecs
import json
import sys

from config.config import FilePathConfig
from util.util import Util

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('UTF-8')
from feature_extractor.entity.document import Document

# gongyi_data = codecs.open("../file/new_corpus.txt", 'r', 'utf-8', 'ignore')
filtered_gongyi_data = codecs.open("../file/filter_new_corpus", 'r', 'utf-8', 'ignore')

cate_dic = Util.load_object_from_pkl(FilePathConfig.category_pkl_path)
count = 0
for line in filtered_gongyi_data:
    try:
        document = Document(line)
        title = document.title
        words = document.get_filtered_content_words_feature()
        label = document.label
        json_object = json.loads(document.json, strict=False)
        if label is None or label not in cate_dic:
            print line
    except:
        print line
        continue

filtered_gongyi_data.close()
print count
