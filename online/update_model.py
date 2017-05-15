# coding=UTF-8
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')
from run.main_classifier import MainClassifier
from config.config import FilePathConfig


def update_corpus():
    # 调用Java从线上取数据，并进行过滤判断，取出有效准确的新数据，并进行采样，添加到语料集中
    # 需要判断语料集什么时候需要删除老语料
    raw_data_path = ""
    filtered_data_path = ""
    total_corpus_path = ""

    get_data_from_db()
    filter_data()
    insert_data()
    pass


def get_data_from_db(raw_data_path):
    pass


def filter_data(raw_data_path, filtered_data_path):
    pass


def insert_data(filtered_data_path, total_corpus_path):
    pass


if __name__ == '__main__':
    main_classifier = MainClassifier()
    main_classifier.construct_lexicon(FilePathConfig.total_corpus_path)
    main_classifier.train(FilePathConfig.total_corpus_path)
    main_classifier.test(FilePathConfig.total_corpus_path)
