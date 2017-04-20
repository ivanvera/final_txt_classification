# coding=UTF-8

from abstract_classifier import AbstractClassifier
from config.config import ClassifierConfig
from util.util import Util


class BoostingClassifier(AbstractClassifier):
    def __init__(self):
        self.model_path = ClassifierConfig.boosting_model_path
        self.sub_models = {}
        self.base_model_weights = ClassifierConfig.classifier_weight_dic
        self.base_model_names = ClassifierConfig.boosting_using_classifiers

    def classify_top_k(self, feature_mat, top_k):
        self.load_model()

        predict_dic = {}
        for base_model_name, base_model in self.sub_models.iteritems():
            predict_result = base_model.classify_top_k(feature_mat, top_k)
            predict_dic[base_model_name] = predict_result

        final_result = []
        length = feature_mat.shape[0]
        for index in xrange(length):
            result_dic = {}
            for base_model_name, predict_list in predict_dic.iteritems():
                predict = predict_list[index]
                for class_id_pro in predict:
                    class_id = class_id_pro[0]
                    class_pro = class_id_pro[1]
                    if class_id not in result_dic:
                        result_dic[class_id] = 0
                    result_dic[class_id] += class_pro * self.base_model_weights[base_model_name]
            sorted_result_list = sorted(result_dic.iteritems(), key=lambda d: d[1], reverse=True)
            final_result.append(sorted_result_list)
        return final_result

        # # 检查top_k
        # if top_k < 1:
        #     top_k = 1
        # top_k = int(top_k)
        #
        # length = feature_mat.shape[0]
        # final_result = []
        # for index in xrange(0, length):
        #     feature_vec = feature_mat.getrow(index)
        #     result_dic = {}
        #     for sub_model_name, sub_model in self.sub_models.iteritems():
        #         predict = sub_model.classify_top_k(feature_vec, top_k)
        #         for class_id_pro in predict[0]:
        #             class_id = class_id_pro[0]
        #             class_pro = class_id_pro[1]
        #             if class_id not in result_dic:
        #                 result_dic[class_id] = 0
        #             result_dic[class_id] += class_pro * self.base_model_weights[sub_model_name]
        #
        #     sorted_result_list = sorted(result_dic.iteritems(), key=lambda d: d[1], reverse=True)
        #     final_result.append(sorted_result_list)
        # return final_result

    def load_model(self):
        if len(self.sub_models) > 0:
            Util.log_tool.log.debug("vote model load already")
            return

        for base_model_name in self.base_model_names:
            model_path = ClassifierConfig.classifier_path_dic[base_model_name]
            Util.log_tool.log.debug("vote add " + base_model_name)
            if not Util.is_file(model_path):
                # 如果base模型不存在，则跳过
                Util.log_tool.log.debug("not having " + base_model_name)
                continue
            base_model = AbstractClassifier()
            base_model.model_path = model_path
            base_model.load_model()

            self.sub_models[base_model_name] = base_model
