# coding=UTF-8
import codecs
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('UTF-8')
from feature_extractor.entity.document import Document

gongyi_data = codecs.open("../file/type_9.txt", 'r', 'utf-8', 'ignore')
filtered_gongyi_data = codecs.open("../file/type_9_filtered.txt", 'w', 'utf-8', 'ignore')
key_words = ["镜头", "合照", "习俗", "超市", "玩具", "神作", "手办", "孩子", "播放", "罐头", "歌曲", "停车", "舞曲", "鸣人", "英文歌", "广场舞"]
count = 0
for line in gongyi_data:
    label = 1
    document = Document(line)
    title = document.title
    words = document.splitContent
    words = document.get_filtered_content_words_feature()
    label = document.label

    if len(words) <= 10 or label is None:
        continue
    label = 1
    for word in key_words:
        if (word in title) or (word in words):
            label = 0
            break

    if label == 1:
        count += 1
        filtered_gongyi_data.write(line)
    else:
        print line

filtered_gongyi_data.close()
gongyi_data.close()
print count
