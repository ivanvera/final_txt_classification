# coding=UTF-8
from config.config import ClassifierConfig
from main_classifier import MainClassifier


class MainClassifierWrapper(object):
    def __init__(self):
        self.main_classifier = MainClassifier()

    def online_classify_document(self, raw_document):
        return self.online_classify_document_top_k(raw_document, 1)

    def online_classify_document_top_k(self, raw_document, top_k):
        raw_document = [raw_document]
        feature_mat = self.main_classifier.data_to_feature(raw_document)
        # 只返回单分类
        classify_result = self.main_classifier.classify_documents(feature_mat)
        result = self.main_classifier.category_reverse_dic[int(classify_result[0][0][0])]
        return result

    def online_classify_document_default(self, raw_document):
        raw_document = [raw_document]
        feature_mat = self.main_classifier.data_to_feature(raw_document)

        single_model_result = {}
        if ClassifierConfig.is_single_model is True:
            raw_result = self.main_classifier.classify_documents_top_k(feature_mat, 2)[0]
        else:
            # 如果是走模型融合，则获取到两个结果
            raw_result, single_model_result = self.main_classifier.classify_documents_top_k(feature_mat, 2)
            # 因为线上是一条请求，所以只需取第一条
            raw_result = raw_result[0]

        top_1_class = raw_result[0][0]
        top_1_class_weight = raw_result[0][1]
        top_2_class = raw_result[1][0]
        top_2_class_weight = raw_result[1][1]

        final_result = []
        final_result.append(self.main_classifier.category_reverse_dic[top_1_class].encode('utf-8'))
        final_result.append('c')
        if self.main_classifier.category_reverse_dic[top_1_class] in ClassifierConfig.negative_types:
            top_1_class_weight = -top_1_class_weight
        final_result.append(str(round(top_1_class_weight, 2)))

        # 因为取了SVM，会把所有权重都给到top-1，所以在第二个可能的类别的控制上需要额外的考虑
        if (abs(top_1_class_weight) - top_2_class_weight < 0.25) and (top_2_class_weight > 0.25):
            final_result.append(self.main_classifier.category_reverse_dic[top_2_class].encode('utf-8'))
            final_result.append('c')
            if self.main_classifier.category_reverse_dic[top_2_class] in ClassifierConfig.negative_types:
                top_2_class_weight = -top_2_class_weight
            final_result.append(str(round(top_2_class_weight, 2)))

        return final_result, single_model_result
