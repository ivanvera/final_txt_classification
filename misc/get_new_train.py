from config.config import FilePathConfig
from util.util import Util

lr_path = FilePathConfig.file_root_path + "raw_results-lr.pkl"
svm_path = FilePathConfig.file_root_path + "raw_results-lsvm.pkl"
xgb_path = FilePathConfig.file_root_path + "raw_results-xgb.pkl"
nb_path = FilePathConfig.file_root_path + "raw_results-nb.pkl"

lr_results = Util.load_object_from_pkl(lr_path)
svm_results = Util.load_object_from_pkl(svm_path)
xgb_results = Util.load_object_from_pkl(xgb_path)
nb_results = Util.load_object_from_pkl(nb_path)

length = len(lr_results)
print length
result = []
result2 = []

for i in xrange(length):
    print i
    lr_result = lr_results[i][0][0]
    svm_result = svm_results[i][0][0]
    xgb_result = xgb_results[i][0][0]
    nb_result = nb_result[i][0][0]

    result_set = set()
    result_set.add(lr_result)
    result_set.add(svm_result)
    result_set.add(xgb_result)
    result_set.add(nb_result)

    if len(result_set) == 1:
        result.append((i, lr_result))

    result2.append(i, len(result_set), lr_result, svm_result, xgb_result, nb_result)

Util.save_object_into_pkl(result, FilePathConfig.file_root_path + "result_total.pkl")
Util.save_object_into_pkl(result2, FilePathConfig.file_root_path + "result_perfect.pkl")

# result = Util.load_object_from_pkl(FilePathConfig.file_root_path + "result2.pkl")
# weight_dic = {}
# weight_dic[3] = 0
# weight_dic[2] = 0
# weight_dic[1] = 0
# weight_dic[0] = 0
#
# class_dic = {}
# for line in result:
#     weight = line[2]
#     weight_dic[weight] += 1
#     cla = line[1]
#     if weight >= 1:
#         if class_dic.get(cla) == None:
#             class_dic[cla] = 1
#         class_dic[cla] += 1
#
# for key, value in weight_dic.items():
#     print key, value
#
# for key, value in class_dic.items():
#     print key, value
