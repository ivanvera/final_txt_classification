from config.config import FilePathConfig
from util.util import Util

lr_path = FilePathConfig.file_root_path + "lr-raw_results.pkl"
svm_path = FilePathConfig.file_root_path + "lsvm-raw_results.pkl"
xgb_path = FilePathConfig.file_root_path + "xgb-raw_results.pkl"
nb_path = FilePathConfig.file_root_path + "mnb-raw_results.pkl"

lr_results = Util.load_object_from_pkl(lr_path)
svm_results = Util.load_object_from_pkl(svm_path)
xgb_results = Util.load_object_from_pkl(xgb_path)
nb_results = Util.load_object_from_pkl(nb_path)

length = len(lr_results)
print length
result = []
result2 = []

result_dic = {}
for i in xrange(length):
    if i % 10000 == 0:
        print i
    lr_result = lr_results[i][0][0]
    svm_result = svm_results[i][0][0]
    xgb_result = xgb_results[i][0][0]
    nb_result = nb_results[i][0][0]

    result_set = set()
    result_set.add(lr_result)
    result_set.add(svm_result)
    result_set.add(xgb_result)
    result_set.add(nb_result)

    if len(result_set) == 1:
        result.append((i, lr_result))
        if lr_result not in result_dic:
            result_dic[lr_result] = 0
        result_dic[lr_result] += 1

    result2.append((i, len(result_set), lr_result, svm_result, xgb_result, nb_result))

Util.save_object_into_pkl(result2, FilePathConfig.file_root_path + "result_total_hou150w.pkl")
Util.save_object_into_pkl(result, FilePathConfig.file_root_path + "result_perfect_hou150w.pkl")

print len(result)
x = sorted(result_dic.iteritems(), key=lambda d: d[1], reverse=True)
print x
