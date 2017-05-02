import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from classify_service import ClassifyService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TProcessPoolServer

from run.main_classifier import MainClassifier
from util.util import Util


class ClassifyServiceHandler:
    main_class_fier = MainClassifier()

    def __init__(self):
        self.log = {}

    def hello(self):
        print 'sayHello'

    def chat(self, input):
        return self.classify(input)

    def classify(self, ID, user, title, split_title, split_content, source):
        return self.classify_top_k(ID, user, title, split_title, split_content, source, 1)

    def classify_top_k(self, ID, user, title, split_title, split_content, source, k):
        Util.log_tool.log.debug(ID + user + title)
        json_dic = dict()
        json_dic["title"] = title
        json_dic["splitTitle"] = split_title
        json_dic["splitContent"] = split_content
        json_dic["source"] = source
        json_dic["ID"] = 1

        raw_document = json.dumps(json_dic, encoding="utf-8", ensure_ascii=False)
        return self.main_class_fier.online_classify_document_top_k(str(raw_document), k)


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
