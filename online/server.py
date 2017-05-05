import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from classify_service import ClassifyService
from C1_SC_CLASSIFY import C1_SC_CLASSIFY_Service
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TProcessPoolServer

from run.main_classifier import MainClassifier
from util.util import Util

class ClassifyServiceHandler:

    def __init__(self):
        self.log = {}
        self.main_class_fier = MainClassifier()
        self.main_class_fier.abstract_classifier.load_model()

    def hello(self):
        print 'sayHello'

    def chat(self, input):
        return self.classify(input)

    def classify(self, ID, user, title, split_title, split_content, source, featurelist):
        return self.classify_top_k(ID, user, title, split_title, split_content, source, featurelist, 1)

    def classify_top_k(self, ID, user, title, split_title, split_content, source, featurelist, k):
        if not self.is_input_valid(ID, user, title, split_title, split_content, source):
            return ''
        raw_document = str(self.dump_json(ID, user, title, split_title, split_content, source))
        return self.main_class_fier.online_classify_document_top_k(raw_document, k)

    def classify_default(self, ID, user, title, split_title, split_content, source, featurelist):
        if not self.is_input_valid(ID, user, title, split_title, split_content, source):
            return ''
        raw_document = str(self.dump_json(ID, user, title, split_title, split_content, source))
        class_list = self.main_class_fier.online_classify_document_default(raw_document)

        if len(class_list) >= 3:
            c_triple_list = [class_list[0], class_list[1], class_list[2]]
        c1sc_result = []
        featurelist = ["政策", "保障", "代表", "民族", "和谐", "经济", "美国"]
        print c_triple_list
        try:
            c1sc_result = self.C1SCService(ID, featurelist, source, title, c_triple_list)
        except:
            Util.log_tool.log.debug("exc")

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

        final_result = {}
        final_result['features'] = class_list
        print final_result
        return json.dumps(final_result, ensure_ascii=False)

    def merge_result(self):
        pass

    def dump_json(self, ID, user, title, split_title, split_content, source):
        json_dic = dict()
        json_dic["title"] = title
        json_dic["splitTitle"] = split_title
        json_dic["splitContent"] = split_content
        json_dic["source"] = source
        json_dic["ID"] = 1

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
        if len(splitContent) < 4 or len(splitTitle) < 4:
            return False
        return True


handler = ClassifyServiceHandler()
processor = ClassifyService.Processor(handler)
transport = TSocket.TServerSocket(port=9901)
tfactory = TTransport.TFramedTransportFactory()
pfactory = TCompactProtocol.TCompactProtocolFactory()

server = TProcessPoolServer.TProcessPoolServer(processor, transport, tfactory, pfactory)
server.setNumWorkers(50)

print 'Starting the server...'
server.serve()
print 'done.'
