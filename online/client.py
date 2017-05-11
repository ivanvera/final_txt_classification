# coding=UTF-8
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')
from classify_service import ClassifyService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

from config.config import FilePathConfig
from util.util import Util
import codecs
import json

def get_document_classify():
    for number in range(10000):
        data = codecs.open(FilePathConfig.total_corpus_path)

        index = 0
        for line in data:
            if index % 10000 == 0:
                Util.log_tool.log.debug(str(number) + ":" + str(index))
            index += 1
            json_data = line.split('\t')[0]
            json_object = json.loads(json_data, encoding='utf-8')

            ID = str(index)
            # ID = json_object['ID']
            user = "mayq"
            title = json_object['title']
            split_title = json_object['splitTitle']
            split_content = json_object['splitContent']
            keyword_list = json_object['features']
            if 'source' in json_object:
                source = json_object["source"]
            else:
                source = ''

            classify_result = classify_request(ID, user, title, split_title, split_content, source, keyword_list)
            Util.log_tool.log.debug(title + '\t' + classify_result + '\t' + str(number) + "\t" + str(index))


def classify_request(ID, user, title, splitTitle, splitContent, source, featureList):
    transport = TSocket.TSocket('10.90.9.87', 9901)
    wrap_transport = TTransport.TFramedTransport(transport)
    protocol = TCompactProtocol.TCompactProtocol(wrap_transport)
    client = ClassifyService.Client(protocol)
    transport.open()
    classify_result = client.classify_default(ID, user, title, splitTitle, splitContent, source, featureList)
    transport.close()
    return classify_result


if __name__ == '__main__':
    get_document_classify()
