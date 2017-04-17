# coding=UTF-8
import codecs
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('UTF-8')
from feature_extractor.entity.document import Document

gongyi_data = codecs.open("../file/type_4.txt", 'r', 'utf-8', 'ignore')
filtered_gongyi_data = codecs.open("../file/type_4_filtered.txt", 'w', 'utf-8', 'ignore')
key_words = ["相机", "拍照", "科技", "明星", "足球", "篮球", "汽车", "工作", "经济", "星座", "科学", "时尚", "公益", "家居", "娱乐", "体育", "健康", "移民",
             "中学", "表白", "字画", "文物", "动漫", "高中", "科比", "YY", "高考", "娱乐圈", "景点", "投降", "佛教", "考古", "挖掘", "爆笑", "APA",
             "摇滚", "白人",
             "身体", "再不去", "学习", "英语", "游客", "全世界", "墓", "单曲", "冠军", "女神", "教练", "考研", "失踪", "打工", "佛", "僧"]
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
