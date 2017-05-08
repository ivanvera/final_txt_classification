# coding=UTF-8
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')
from classify_service import ClassifyService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TProcessPoolServer

from classify_service_wrapper import ClassifyServiceWrapper

class ClassifyServiceHandler:

    def __init__(self):
        self.log = {}
        self.classify_service_wrapper = ClassifyServiceWrapper()

    def hello(self):
        print 'sayHello'

    def chat(self, input):
        return str(len(input()))

    def classify(self, ID, user, title, split_title, split_content, source, keywordList):
        return self.classify_top_k(ID, user, title, split_title, split_content, source, keywordList, 1)

    def classify_top_k(self, ID, user, title, split_title, split_content, source, keywordList, k):
        return self.classify_service_wrapper.classify_top_k(ID, user, title, split_title, split_content, source,
                                                            keywordList, k)

    def classify_default(self, ID, user, title, split_title, split_content, source, keyword_list):
        return self.classify_service_wrapper.classify_default(ID, user, title, split_title, split_content, source,
                                                              keyword_list)


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
