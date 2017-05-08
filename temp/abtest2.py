import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
from util.util import Util
from config.config import FilePathConfig
import json

class_result = Util.load_object_from_pkl('../file/raw_results-vote.pkl')
index = 0
type_reverse_dic = Util.load_object_from_pkl(FilePathConfig.category_reverse_pkl_path)
raw_data = codecs.open(FilePathConfig.raw_news_path, 'r', ' utf-8')
notmatch_news = codecs.open("../file/notmatch_news.json", 'w', 'utf-8')

title_set = set()
for line in raw_data:
    json_obj = json.loads(line, encoding='utf-8')
    cates = json_obj['category']
    pre_cate = type_reverse_dic[int(class_result[index][0][0])]
    index += 1
    match = False
    if cates[0] not in type_reverse_dic.values():
        continue
    for cat in cates:
        if cat == pre_cate or cat in pre_cate:
            match = True
    if not match:
        if title in title_set():
            continue
        title_set.add(title)
        print cates[0], pre_cate
        title = json_obj['title']
        notmatch_news.write(cates[0] + '\t' + pre_cate + '\t' + title + '\n')

notmatch_news.close()
raw_data.close()
