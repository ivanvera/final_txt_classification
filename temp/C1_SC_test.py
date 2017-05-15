# coding=UTF-8
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')
from online.C1_SC_CLASSIFY import C1_SC_CLASSIFY_Service
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


source = '腾讯体育'
featurelist = ['詹姆斯', '韦德', '库里', '保罗', 'NBA', '骑士队', '篮球', '季后赛', '全明星', '常规赛', 'MVP', '总冠军']
c_triple_list = ['体育', 'c', '0.91']
title = '詹姆斯三双，大获全胜'

print C1SCService('1', featurelist, featurelist, title, c_triple_list)
