# coding=UTF-8
import json
import re

from config.config import ClassifierConfig
from feature_extractor.word_extractor.bigram_extractor import BiGramExtractor
from feature_extractor.word_extractor.common_word_extractor import CommonWordExtractor
from util.util import Util


class Document(object):
    def __init__(self, raw_document):
        split_data = raw_document.split('\t')
        json_data = split_data[0]

        json_object = json.loads(json_data, strict=False)

        self.json = json_data
        self.splitContent = None
        self.id = json_object['ID']
        self.title = json_object['title']
        self.words = []
        self.source = ""
        self.filters = []

        self.words = None
        self.raw_content = None
        self.label = None

        if "splitContent" in json_object:
            self.splitContent = json_object['splitContent']

        if "splitTitle" in json_object:
            if self.splitContent is not None:
                self.splitContent += json_object['splitTitle']

        if 'source' in json_object:
            self.source = json_object['source']

        if len(split_data) == 4:
            # 目前因为已经把数据处理好，节省时间，所以就按这种方式取
            self.words = split_data[1].strip().split(',')
            self.raw_content = split_data[2].strip()
            self.label = split_data[3].strip()

        if len(split_data) == 2:
            self.label = split_data[1].strip()

        if ClassifierConfig.is_use_bigram is True:
            self.abstract_extractor = BiGramExtractor()
        else:
            self.abstract_extractor = CommonWordExtractor()

    def add_filter(self, added_filter):
        self.filters.append(added_filter)
        return self

    # 目前因为已经把数据处理好，所以加了一层检验
    def get_content_words_feature(self):
        # if len(self.words) == 0:
        #     raw_content = self.abstract_extractor.extract(self.raw_content)
        # else:
        #     raw_content = self.words
        content = self.splitContent
        if content is None:
            return None
        content = re.sub('_[A-Za-z]+', '', content)
        words = content.split()
        words.append(self.source)
        words = [word.lower() for word in words if len(word.strip()) > 1]
        return words

    # 从正文中取出词，并过滤
    def get_filtered_content_words_feature(self):
        if self.words is not None:
            return self.words
        content = self.splitContent
        if content is None:
            return None
        content = Util.filter_text(content)
        content = content.split()
        content.append(self.source)
        # 对添加的filter进行排序，使优先级高的先进行过滤
        sorted(self.filters)
        for single_filter in self.filters:
            content = single_filter.filter(content)
        return content

    def get_raw_content(self):
        if self.raw_content is not None:
            return self.raw_content
        content = self.splitContent
        if content is None:
            return None
        content = re.sub('_[A-Za-z]+', '', content)
        content = Util.filter_text(content)
        content = content.replace(' ', '')
        return content.strip()
