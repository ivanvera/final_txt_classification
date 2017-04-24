# coding=UTF-8
import codecs
import json
import sys

from config.config import FilePathConfig
from util.util import Util

reload(sys)
sys.setdefaultencoding('UTF-8')

perfect_result = Util.load_object_from_pkl(FilePathConfig.file_root_path + "result_perfect_qian100w.pkl")
cate_reverse_dic = Util.load_object_from_pkl(FilePathConfig.category_reverse_pkl_path)

index_set = set()
index_cate = {}
count_dic = {}

filter_list = ["生活", "公益", "摄影", "职场", "文化", "动漫", "风水", "移民", "收藏"]

for item in perfect_result:
    index_set.add(item[0])
    cate = cate_reverse_dic[item[1]]
    index_cate[item[0]] = cate
    if cate not in count_dic:
        count_dic[cate] = 0
    count_dic[cate] += 1

for key, value in count_dic.iteritems():
    print key, value

data = codecs.open(FilePathConfig.file_root_path + "unlabeled_news_qian100w.json", 'r', FilePathConfig.file_encodeing)
result = codecs.open(FilePathConfig.file_root_path + "match_result_qian100w.json", 'w', FilePathConfig.file_encodeing)
index = 0

for line in data:
    if index in index_set:
        if index_cate[index] not in filter_list:
            json_object = json.loads(line.strip())
            if json_object.has_key("category"):
                if (not json_object["docType"] == "video") and (index_cate[index] in json_object["category"]):
                    result.write(line.strip() + "\t" + index_cate[index] + "\n")
    index += 1

data.close()
result.close()
