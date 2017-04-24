# coding=UTF-8
import codecs
import json
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('UTF-8')
from feature_extractor.entity.document import Document

gongyi_data = codecs.open("../file/new_corpus.txt", 'r', 'utf-8', 'ignore')
filtered_gongyi_data = codecs.open("../file/filter_new_corpus", 'w', 'utf-8', 'ignore')

count = 0
for line in gongyi_data:
    try:
        document = Document(line)
        title = document.title
        words = document.get_filtered_content_words_feature()
        label = document.label
        json_object = json.loads(document.json, strict=False)
        if json_object.has_key("category"):
            if label in json_object["category"]:
                filtered_gongyi_data.write(line)
                count += 1
    except:
        print line
        continue

filtered_gongyi_data.close()
gongyi_data.close()
print count
