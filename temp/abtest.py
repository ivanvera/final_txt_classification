import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
from util.util import Util
from config.config import FilePathConfig
import json

from sklearn import metrics

data = codecs.open("old_test_output.json", 'r', 'utf-8')

category_dic = Util.load_object_from_pkl(FilePathConfig.category_pkl_path)
category_reverse_dic = Util.load_object_from_pkl(FilePathConfig.category_reverse_pkl_path)
count1 = 0
count2 = 0
count = 0
num = 0
pre_array = []
label_array = []
for line in data:
    num += 1
    splited_data = line.split("\t")
    json_object = json.loads(splited_data[1])
    label = splited_data[2].strip()
    title = splited_data[0]
    features = json_object["features"]
    if len(features) == 3:
        label_array.append(label)
        pre_array.append(features[0])
        if features[0] == label:
            count1 += 1
            count += 1
    elif len(features) == 6:
        label_array.append(label)
        if features[0] == label or features[3] == label:
            pre_array.append(label)
        else:
            pre_array.append(features[0])
        if features[0] == label or features[3] == label:
            count2 += 1
            count += 1

print metrics.classification_report(label_array, pre_array, digits=4)
print count1, count2, count, num
