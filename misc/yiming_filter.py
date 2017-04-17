# coding=UTF-8
import codecs
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('UTF-8')
from feature_extractor.entity.document import Document

gongyi_data = codecs.open("../file/type_8.txt", 'r', 'utf-8', 'ignore')
filtered_gongyi_data = codecs.open("../file/type_8_filtered.txt", 'w', 'utf-8', 'ignore')
# key_words = ["美联储", "出境游","汉服","斯琴高娃","游客","诺贝尔","楼市","霍启刚","华商节","旅游","厨王争霸","济州岛","免签","阅读",]
key_words = ["移民", "华人", "华裔", "签证", "绿卡", "EB"]
count = 0
for line in gongyi_data:

    document = Document(line)
    title = document.title
    words = document.splitContent
    words = document.get_filtered_content_words_feature()
    label = document.label

    if len(words) <= 10 or label is None:
        continue
    label = 0
    for word in key_words:
        if (word in title) or (word in words):
            label = 1
            break

    if label == 1:
        count += 1
        filtered_gongyi_data.write(line)
    else:
        print line

filtered_gongyi_data.close()
gongyi_data.close()
print count
