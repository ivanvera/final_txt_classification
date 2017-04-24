from datetime import datetime

from sklearn import metrics

from config.config import FilePathConfig, ClassifierConfig
from util.util import Util

class TestResult(object):
    def __init__(self, predicted_class, raw_class_label, labels):
        self.predicted_class = predicted_class
        self.raw_class_label = raw_class_label
        self.labels = labels
        self.macro_precision = None
        self.macro_recall = None
        self.classification_report = None
        self.confusion_matrix = None
        self.prams = ClassifierConfig.classifier_pram_dic[ClassifierConfig.cur_single_model]

    def print_report(self):
        predicted_class = self.predicted_class
        raw_class_label = self.raw_class_label
        self.macro_precision = metrics.precision_score(raw_class_label, predicted_class, average="macro")
        self.macro_recall = metrics.recall_score(raw_class_label, predicted_class, average="macro")

        self.classification_report = metrics.classification_report(raw_class_label, predicted_class,
                                                                   target_names=self.labels, digits=4)
        self.confusion_matrix = metrics.confusion_matrix(raw_class_label, predicted_class)

        Util.log_tool.log.info(self.classification_report.encode(FilePathConfig.file_encodeing))
        Util.log_tool.log.info(
            "macro_precision:" + str(self.macro_precision) + ",macro_recall:" + str(self.macro_recall))
        self.save_report()

    def save_report(self):
        time = datetime.now().strftime("-%Y-%m-%d-%H-%M")
        if ClassifierConfig.is_single_model:
            model_name = ClassifierConfig.cur_single_model
        else:
            model_name = ClassifierConfig.boosting_name

        label = time + '-' + model_name

        Util.save_object_into_pkl(self, str(FilePathConfig.result_report_path) % label)
