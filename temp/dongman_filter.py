# coding=UTF-8
import codecs
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('UTF-8')
from feature_extractor.entity.document import Document

gongyi_data = codecs.open("../file/type_5.txt", 'r', 'utf-8', 'ignore')
filtered_gongyi_data = codecs.open("../file/type_5_filtered.txt", 'w', 'utf-8', 'ignore')
key_words = ["科学家", "短篇", "小说", "鸡血", "压岁钱", "性生活", "春节", "王者荣耀", "玩具", "熊孩子", "休息", "买买买", "美瞳", "照片", "旗袍"
    , "单身狗", "壁纸", "年俗", "虐恋", "阴阳师", "男朋友", "微电影", "智商", "过年", "理发店", "谢霆锋", "歌手", "明星", "林心如", "剑侠情缘", "淘宝", "打呼噜",
             "日本媳妇", "甲基", "网剧"
    , "打女人", "AV", "美拍", "保险公司", "同居", "萝卜", "EXO", "美剧", "呵呵", "游戏", "王尼玛", "鸡十三", "撒贝宁", "现实"]

count = 0
for line in gongyi_data:
    document = Document(line)
    title = document.title
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
