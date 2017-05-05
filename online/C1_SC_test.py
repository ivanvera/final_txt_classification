# coding=UTF-8
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')
from C1_SC_CLASSIFY import C1_SC_CLASSIFY_Service
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol


def C1SCService(ID, featurelist, source, title, c_triple_list):
    transport = TSocket.TSocket('10.90.7.58', 7911)
    wrap_transport = TTransport.TFramedTransport(transport)
    protocol = TCompactProtocol.TCompactProtocol(wrap_transport)
    client = C1_SC_CLASSIFY_Service.Client(protocol)
    transport.open()
    c1sc_result = client.classify(ID, featurelist, source, title, c_triple_list)
    transport.close()
    return c1sc_result


featurelist = ["政策", "保障", "代表", "民族", "和谐", "经济", "美国"]
source = "人民网"
title = "习近平访问美国"
c_triple_list = ["时政", "c", "1.0"]

C1SCService('1', featurelist, source, title, c_triple_list)
