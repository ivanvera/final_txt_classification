# coding=UTF-8
import codecs
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('UTF-8')
from feature_extractor.entity.document import Document

gongyi_data = codecs.open("../file/type_2.txt", 'r', 'utf-8', 'ignore')
filtered_gongyi_data = codecs.open("../file/type_2_filtered.txt", 'w', 'utf-8', 'ignore')
key_words = ["奇趣", "荤菜", "马云", "搞笑", "登月", "足球", "自作孽", "副业", "相爱", "汉服", "死因", "倚天屠龙", "偷拍", "大哥", "小人物", "GIF", "gif",
             "死", "神秘山洞",
             "高分", "杀害", "食物", "爆笑", "莆田", "好听", "坦克", "王俊凯"]
count = 0
for line in gongyi_data:
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
