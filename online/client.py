# coding=UTF-8
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')
from online.classify_service import ClassifyService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol


# try:
#     # Make socket
#     transport = TSocket.TSocket('localhost', 9090)
#     # Buffering is critical. Raw sockets are very slow
#     transport = TTransport.TBufferedTransport(transport)
#     # Wrap in a protocol
#     protocol = TBinaryProtocol.TBinaryProtocol(transport)
#     # Create a client to use the protocol encoder
#     client = ClassifyService.Client(protocol)
#     # Connect!
#     transport.open()
#     client.hello()
#     print 'ping()'
#     print(client.chat("client access"))
#
#     title = "柯文哲纠正司仪“恭请市长”说法：别用封建语言"
#     ID = "1"
#     user = "mayq"
#     title = '柯文哲纠正司仪“恭请市长”说法：别用封建语言'
#     splitTitle = '柯文哲_nr 纠正_v 司仪_n 恭请_v 市长_x 说法_k ：_w 别_k 用_k 封建_k 语言_n '
#     splitContent = '_w 原_k 标题_n ：_w 纠正_v 恭请_v  _w 柯文哲_nr ：_w 别_k 用_k 封建_k 语言_n  _w \n_w  _w \n_w  _w 台海网_n 3月_t 30日_t 讯_k  _w 据_h 中国时报_x 报道_k ，_w 台北市府_x 29日_mq 举办_v 首长_n 领航_k 营_k ，_w 司仪_n 刚_d 宣布_v 恭请_v 市长_x 致词_k 后_f ，_w 旋_k 遭_k 柯文哲_nr 打_k 脸_n 不要_v 再_d 用_k 这种_mq 封建_k 时代_n 的_u 语言_n ，_w 引起_v 现场_n 哄堂大笑_i 。_w 但_k 卫生局_x 在_p 讲义_n 中_n 整理_v 40条_mq 柯_k 语录_x ，_w 连_h 奇怪_a 耶_k ，_w 听_k 起来_v 怪怪的_z 都_n 入列_v ，_w 卫生局长_x 黄世杰_nr 澄清_k ，_w 市长_x 的_u 核心_n 价值_n 很_d 重要_a ，_w 才_h 会_v 整理_v 市长_x 说_v 过_v 的_u 重点_h ，_w 纯属_v 参考_v 不用_v 牢记_v 或_d 盲从_v 。_w  _w \n_w  _w \n_w  _w 柯文哲_nr 透露_v ，_w 有_v 次_q 去_n 参加_v 国民党_x 一个_mq 会议_n ，_w 他们_r 很_d 喜欢_v 互_d 称_v 什么_r 公_k 、_w 什么_r 公_k ，_w 像_k 吴伯雄_x 就_d 被_p 称为_v 伯公_n 。_w 因此_c 有_v 次_q 遇到_v 民进党_x 主席_x 蔡英文_nr ，_w 自己_h 就_d 和_c 她_r 提起_v 这件_mq 事_k ，_w 并_h 说_v 还好_v 民进党_x 没有_v 这种_mq 文化_x ，_w 不然_c 像_k 苏贞昌_x 不_h 就_d 变_v 冲_k 公_k （_w 台语_nz ）_w ？_w  _w \n_w  _w \n_w  _w 柯文哲_nr 分享_v 完_h 这段_mq 故事_n 后_f 不_h 忘_v 再次_d 提醒_v 司仪_n ，_w 以后_f 就_d 不要_v 再_d 用_v 恭请_v 这种_mq 封建_k 时代_n 的_u 语言_n 。_w '
#     source = '台海网'
#
#     print client.classify(ID,user,title,splitTitle,splitContent,source)
#     # Close!
#     transport.close()
#
# except Thrift.TException, tx:
#     print '%s' % (tx.message)


def get_document_classify():
    for index in range(0, 10):
        ID = str(index)
        user = "mayq"
        title = '柯文哲纠正司仪“恭请市长”说法：别用封建语言'
        splitTitle = '柯文哲_nr 纠正_v 司仪_n 恭请_v 市长_x 说法_k ：_w 别_k 用_k 封建_k 语言_n '
        splitContent = '_w 原_k 标题_n ：_w 纠正_v 恭请_v  _w 柯文哲_nr ：_w 别_k 用_k 封建_k 语言_n  _w \n_w  _w \n_w  _w 台海网_n 3月_t 30日_t 讯_k  _w 据_h 中国时报_x 报道_k ，_w 台北市府_x 29日_mq 举办_v 首长_n 领航_k 营_k ，_w 司仪_n 刚_d 宣布_v 恭请_v 市长_x 致词_k 后_f ，_w 旋_k 遭_k 柯文哲_nr 打_k 脸_n 不要_v 再_d 用_k 这种_mq 封建_k 时代_n 的_u 语言_n ，_w 引起_v 现场_n 哄堂大笑_i 。_w 但_k 卫生局_x 在_p 讲义_n 中_n 整理_v 40条_mq 柯_k 语录_x ，_w 连_h 奇怪_a 耶_k ，_w 听_k 起来_v 怪怪的_z 都_n 入列_v ，_w 卫生局长_x 黄世杰_nr 澄清_k ，_w 市长_x 的_u 核心_n 价值_n 很_d 重要_a ，_w 才_h 会_v 整理_v 市长_x 说_v 过_v 的_u 重点_h ，_w 纯属_v 参考_v 不用_v 牢记_v 或_d 盲从_v 。_w  _w \n_w  _w \n_w  _w 柯文哲_nr 透露_v ，_w 有_v 次_q 去_n 参加_v 国民党_x 一个_mq 会议_n ，_w 他们_r 很_d 喜欢_v 互_d 称_v 什么_r 公_k 、_w 什么_r 公_k ，_w 像_k 吴伯雄_x 就_d 被_p 称为_v 伯公_n 。_w 因此_c 有_v 次_q 遇到_v 民进党_x 主席_x 蔡英文_nr ，_w 自己_h 就_d 和_c 她_r 提起_v 这件_mq 事_k ，_w 并_h 说_v 还好_v 民进党_x 没有_v 这种_mq 文化_x ，_w 不然_c 像_k 苏贞昌_x 不_h 就_d 变_v 冲_k 公_k （_w 台语_nz ）_w ？_w  _w \n_w  _w \n_w  _w 柯文哲_nr 分享_v 完_h 这段_mq 故事_n 后_f 不_h 忘_v 再次_d 提醒_v 司仪_n ，_w 以后_f 就_d 不要_v 再_d 用_v 恭请_v 这种_mq 封建_k 时代_n 的_u 语言_n 。_w '
        source = '台海网'

        classify_result = ClassifyService(ID, user, title, splitTitle, splitContent, source)
        print title + '\t' + classify_result


def ClassifyService(ID, user, title, splitTitle, splitContent, source):
    transport = TSocket.TSocket('localhost', 9901)
    wrap_transport = TTransport.TFramedTransport(transport)
    protocol = TCompactProtocol.TCompactProtocol(wrap_transport)
    client = ClassifyService.Client(protocol)
    transport.open()
    classify_result = client.classify(ID, user, title, splitTitle, splitContent, source)
    transport.close()
    return classify_result


if __name__ == '__main__':
    get_document_classify()
