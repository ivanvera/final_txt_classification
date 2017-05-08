# coding=UTF-8
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from C1_SC_CLASSIFY import C1_SC_CLASSIFY_Service
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

from run.main_classifier import MainClassifier
from util.util import Util


class ClassifyServiceWrapper:
    def __init__(self):
        self.main_class_fier = MainClassifier()
        self.main_class_fier.abstract_classifier.load_model()

    def hello(self):
        print 'sayHello'

    def chat(self, input):
        return self.classify(input)

    def classify(self, ID, user, title, split_title, split_content, source, keywordList):
        return self.classify_top_k(ID, user, title, split_title, split_content, source, keywordList, 1)

    def classify_top_k(self, ID, user, title, split_title, split_content, source, keywordList, k):
        return ''

    def classify_default(self, ID, user, title, split_title, split_content, source, keyword_list):
        if not self.is_input_valid(ID, user, title, split_title, split_content, source):
            return ''
        raw_document = str(self.dump_json(ID, title, split_title, split_content, source))
        class_list = self.main_class_fier.online_classify_document_default(raw_document)
        Util.log_tool.log.debug("ID:" + ID + "main class:" + str(class_list))
        c1sc_result = self.request_c1_sc(ID, class_list, keyword_list, source, title)
        Util.log_tool.log.debug("ID:" + ID + "sub class:" + str(c1sc_result))
        self.merge_c1_sc_result(c1sc_result, class_list)

        final_result = dict()
        final_result['features'] = class_list
        Util.log_tool.log.debug("ID:" + ID + "final class:" + str(final_result))
        return json.dumps(final_result, ensure_ascii=False)

    def request_c1_sc(self, ID, class_list, keyword_list, source, title):
        if len(class_list) >= 3:
            c_triple_list = [class_list[0], class_list[1], class_list[2]]
        c1sc_result = []
        keyword_list = [x.encode('utf-8') for x in keyword_list]
        source = source.encode('utf-8')
        title = title.encode('utf-8')
        length = len(keyword_list)
        final_feature_list = []
        for index in range(length):
            if index % 3 == 0:
                word = keyword_list[index]
                if word is None:
                    continue
                final_feature_list.append(word)
        try:
            c1sc_result = self.C1SCService(ID, final_feature_list, source, title, c_triple_list)
        except Exception, e:
            Util.log_tool.log.error("error c1sc " + ID + " " + title)
            Util.log_tool.log.error(repr(e))
        return c1sc_result

    def merge_c1_sc_result(self, c1sc_result, class_list):
        if len(c1sc_result) > 0:
            if c1sc_result[1] == 'c':
                if c1sc_result[0] != class_list[0]:
                    for key in c1sc_result:
                        class_list.append(key)
                else:
                    if len(c1sc_result) > 3:
                        result_index = 3
                        while result_index < len(c1sc_result):
                            class_list.append(c1sc_result[result_index])
                            result_index += 1
            else:
                for key in c1sc_result:
                    class_list.append(key)

    def dump_json(self, ID, title, split_title, split_content, source):
        json_dic = dict()
        json_dic["title"] = title
        json_dic["splitTitle"] = split_title
        json_dic["splitContent"] = split_content
        json_dic["source"] = source
        json_dic["ID"] = ID

        raw_document = json.dumps(json_dic, encoding="utf-8", ensure_ascii=False)
        return raw_document

    def C1SCService(self, ID, featurelist, source, title, c_triple_list):
        transport = TSocket.TSocket('10.90.7.58', 7911)
        wrap_transport = TTransport.TFramedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocol(wrap_transport)
        client = C1_SC_CLASSIFY_Service.Client(protocol)
        transport.open()
        c1sc_result = client.classify(ID, featurelist, source, title, c_triple_list)
        transport.close()
        return c1sc_result

    def is_input_valid(self, ID, user, title, splitTitle, splitContent, source):
        if len(splitContent) > 0 and len(splitTitle) > 0 and len(title) > 0:
            return False
        return True
