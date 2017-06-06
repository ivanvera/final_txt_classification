# coding=UTF-8
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')
from classify_service import ClassifyService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol


def get_document_classify():
    ID = 'cmpp_16961583'
    user = "mayq"
    title = '这个地方越粗，血管越差？每天喝一杯它，血管越喝越年轻！'
    split_title = '这个_h 地方_n 越_h 粗_k ，_w 血管_x 越_h 差_k ？_w 每天_r 喝_h 一杯_mq 它_r ，_w 血管_x 越_h 喝_h 越_h 年轻_a ！_w '
    split_content = "  _w 这个_h 地方_n 越_h 粗_k ，_w 血管_x 越_h 差_k ？_w 每天_r 喝_h 一杯_mq 它_r ，_w 血管_x 越_h 喝_h 越_h 年轻_a ！_w   _w \n_w   _w \n_w  _w 皱纹_x 越来越_d 多_m ，_w 意味着_v 人_r 越来越_d 老_n 了_u ！_w  _w \n_w   _w \n_w  _w 身体_n 发生_v 变化_v 后_f ，_w 人们_r 可以_v 从_p 身体_n 上_f 一些_h 信号_n 看_v 出来_v 。_w 但是_c 任_v 其_u 发展_v 下去_v 就_d 可能_v 会_v 更_v 严重_a ，_w 所以_c 应当_v 引起_v 我们_r 的_u 重视_v ！_w  _w \n_w   _w \n_w  _w 不管_c 是_v 人_r 的_u 衰老_x 或_k 疾病_n 的_u 发生_v ，_w 都_h 会_v 有_v 信号_n 提示_k 你_r ！_w 那么_k ，_w 血管_x 差_k 又_d 有_v 什么_r 信号_n 呢_k ？_w  _w \n_w   _w \n_w  _w 脖子_n 越_h 粗_k ，_w 血管_x 越_h 差_k ！_w  _w \n_w    _w \n_w  _w 一般来说_l ，_w 脖子_n 粗细_n 和_c 肥胖_x 程度_n 有着_v 直接_a 关联_v 。_w 尤其_d 是_v 男性_n 到_v 了_u 中年_n 以后_f ，_w 女性_n 到_v 围_k 绝经期_x 以后_f ，_w 大_k 部分_n 会_v 有_v 明显_a 的_u 体形_n 改变_v 。_w 尤其_d 是_v 男性_n ，_w 到_v 了_u 四五十岁_mq ，_w 会_v 明显_a 发福_x ，_w 脖子_n 也_d 会_v 跟着_v 变_k 粗_k 。_w  _w \n_w   _w \n_w  _w 美国_x 《_w 临床_x 内分泌学_nz 与_p 代谢_x 》_w 杂志_n 上_v 的_u 一篇_mq 研究_v 就_d 提出_v ，_w 研究_v 对_p 3000多名_mq 研究_v 对象_n 进行_v 脖子_n 测量_v ，_w 同时_k 对_p 这些_r 人_h 进行_v 血压_x 、_w 血脂_x 、_w 血糖_x 等_u 指标_n 检测_v 。_w 结果_k 发现_k ，_w 脖子_n 越_h 粗_k 的_u 人_h ，_w 其_h 心血管疾病_x 风险_n 就_d 越_h 大_k 。_w  _w \n_w  _w \n_w    _w \n_w  _w \n_w    _w \n_w   _w \n_w  _w 北京_h 世纪_n 坛_n 医院_n 心血管内科_x 主任_n 杨水祥_nr 通过_k 临床_x 观察_v 也_d 发现_k ，_w 脑袋_n 大_d 脖子_n 粗_k ，_w 说明_h 营养_k 过剩_v ，_w 例如_v 伙夫_n 经常_d 要_v 品尝_v 菜_n ，_w 大款_n 吃吃喝喝_l ，_w 他们_r 往往_d 有_v 更_v 高_n 的_u 心脑血管病_x 风险_n ，_w 而_h 脖子_n 粗_k ，_w 就是_k 这_r 类_q 人群_n 的_u 特征_n 之一_mq 。_w  _w \n_w   _w \n_w  _w 脖子_n 粗_k 不_h 粗_k ，_w 一_m 测_v 便_h 知_h ！_w  _w \n_w   _w \n_w    _w \n_w   _w \n_w  _w 如果_c 男性_n 颈_k 围_v 超过_v 39厘米_mq ，_w 女性_n 颈_k 围_v 超过_v 35厘米_mq ，_w 则_k 说明_v 脖子_n 较_k 粗_k ，_w 发生_v 心血管_x 事件_n 的_u 风险_n 高_k 。_w  _w \n_w   _w \n_w  _w 解放军总医院_x 国际医学_x 中心_k 主任_n 曾强_nr 提醒_v ，_w 测量_v 脖子_n 时_n ，_w 将_d 皮尺_n 水平_n 置于_v 颈部_n 最_n 细处_n 进行_v 测量_v ，_w 即_h 颈_k 后_f 第七_mq 颈椎_x 上_f 缘_k （_w 低头_v 时_n 摸_v 到_v 的_u 颈_k 后_f 最_k 突起_k 处_k ）_w ，_w 至_k 前面_f 的_u 喉结_n 下方_f ，_w 完成_v 测量_v 。_w  _w \n_w   _w \n_w  _w 测_v 完_h 后_f ，_w 你_r 的_u 脖子_n 正常_a 么_u ？_w  _w \n_w   _w \n_w   _w 如果_c 你_r 的_u 脖子_n 较_k 粗_k ，_w 就_d 一定_k 要_v 引起_v 注意_v 了_u 。_w 早点_n 养_k 血管_x ，_w 胜_k 于老_nr 来_v 治_k 。_w 因此_c 保护_v 血管_x ，_w 永远_d 都_h 不_h 嫌_k 迟_k ，_w 有_v 什么_r 有效_a 的_u 方法_n 能_v 保护_v 好_k 血管_x 呢_k ？_w  _w \n_w   _w \n_w  _w 每天_r 一杯_mq ，_w 血管_x 越_h 喝_h 越_h 年轻_a ！_w  _w \n_w   _w \n_w  _w 可能_h 菊花_x 在_p 人们_r 生活_v 中_n 一般_k 是_v 用来_v 降火_x 的_u ，_w 可是_k 不_h 知道_v 它_r 还_v 有助于_v 血管_x 扩张_v ，_w 使_v 心血管系统_x 保持_v 健康_x 的_u 作用_k 。_w  _w \n_w   _w \n_w  _w 在_p 前人_n 留下_v 的_u 关于_p 药用植物_nz 的_u 古书_n 中_f ，_w 关于_p 菊花_x 的_u 功效_n 与_p 作用_v 有_v 如下_v 记载_k ：_w 味_h 甘苦_n 、_w 性_n 微_k 寒_k ，_w 主治_v 风热感冒_x 、_w 头痛_k 眩晕_x 、_w 皮肤病_x 和_c 血流_v 不_h 畅_k 。_w  _w \n_w   _w \n_w  _w 常_k 喝_h 菊花茶_x 可以_v 有助于_v 保护_v 血管_x ，_w 其实_d ，_w 在_p 泡_k 菊花茶_x 时_n 加上_v 其他_r 材料_n 一起_k 效果_n 更_v 佳_a 。_w  _w \n_w   _w \n_w  _w -_w  _w 桑杞_nr 菊花茶_x  _w -_w  _w \n_w  _w \n_w   _w \n_w  _w 材料_n ：_w 桑葚_x 6g_mq  _w /_w  _w 枸杞_x 6g_mq  _w /_w  _w 菊花_x 3g_mq  _w \n_w  _w \n_w  _w 做法_n ：_w  _w \n_w  _w \n_w  _w 1_mq 、_w 把_p 这_r 三种_mq 材料_n 分别_k 洗_k 干净_a 。_w  _w \n_w  _w \n_w  _w 2_mq 、_w 放入_n 杯中_s ，_w 再_d 用_v 沸水_n 冲泡_v ，_w 可_k 代_k 茶_e 饮用_v 。_w  _w \n_w  _w \n_w  _w 桑葚_x ：_w  _w \n_w  _w \n_w  _w 既_k 可_v 食用_k 又_d 可_v 入药_v ，_w 中医_x 认为_v 桑葚_x 味_h 甘_k 酸性_n 微_k 寒_k ，_w 入_k 心_k 、_w 肝_n 、_w 肾经_nz ，_w 可_k 滋补_v 强壮_k 、_w 养心_x 益智_x 、_w 生津止渴_l 。_w 桑椹_e 中_f 的_u 脂肪酸_x 具有_v 分解_v 脂肪_x 、_w 降低_v 血脂_x 、_w 防止_v 血管_x 硬化_v 等_u 作用_k 。_w  _w \n_w   _w \n_w  _w 枸杞_x ：_w  _w \n_w  _w \n_w  _w 具有_v 清除_v 人体_n 自由基_x 的_u 作用_k ，_w 可_k 有效_a 保护_v 心脏_n 血管_x 内皮_n ，_w 维持_v 血管_x 的_u 弹性_n ，_w 对_p 调整_v 心律不齐_x 也_d 有_v 一定_k 的_u 帮助_v 。_w 它_r 还_v 参与_v 维生素A_x 合成_v ，_w 含有_v 的_u 铁_e 元素_n 可_v 促进_v 造血_v 功能_n 。_w  _w \n_w   _w \n_w  _w -_w  _w 菊花_x 山楂茶_x  _w -_w  _w \n_w  _w \n_w   _w \n_w  _w 材料_n ：_w 菊花_x 、_w 山楂_x 适量_v 。_w  _w \n_w  _w \n_w  _w 做法_n ：_w  _w \n_w  _w \n_w  _w 1_mq 、_w 把_p 菊花_x 和_c 山楂_x 用水_k 冲洗_v 。_w  _w \n_w  _w \n_w  _w 2_mq 、_w 把_p 这_r 2种_mq 材料_n 放入_n 茶壶_e ，_w 用_k 开水_n 冲泡_v ，_w 盖_k 盖_v 焖_v 6-8_mq 分钟_q 即可_v 饮用_v 。_w  _w \n_w  _w \n_w  _w 山楂_x ：_w  _w \n_w  _w \n_w  _w 含_v 多种_mq 维生素_x 、_w 有机酸_e 、_w 矿物质_n 和黄_x 酮_x 类_k 物质_n ，_w 具有_v 平稳_a 血压_x 、_w 调整_v 血脂_x 、_w 降低_v 胆固醇_x 、_w 软化_v 血管_x 、_w 增加_v 冠状动脉_x 血流_v 量_k 的_u 作用_k 。_w  _w \n_w   _w \n_w  _w 菊花_x 和_c 山楂_x 搭配_v ，_w 两种_mq 药材_x 相_k 辅_k ，_w 经常_d 饮用_v 菊花_x 山楂茶_x 有_v 软化_v 血管_x 的_u 作用_k 。_w "
    features_list = ["中医", "cn", "0.1", "lt_87", "t", "0.5", "lt_396", "t", "0.2", "lt_422", "t", "0.2", "临床内分泌学与代谢",
                     "kb", "0.1", "菊花", "et", "0.5", "枸杞", "et", "0.1", "风热感冒", "et", "0.1", "国际医学", "et", "0.1", "心血管",
                     "et", "0.1", "皮肤病", "et", "0.1", "益智", "et", "0.1", "血管", "x", "-1.0", "菊花茶", "x", "-0.1", "山楂",
                     "x", "-0.1", "桑葚", "x", "-0.1", "血脂", "x", "-0.1", "山楂茶", "x", "-0.1", "临床", "x", "-0.1", "血压",
                     "x", "-0.1", "心脑血管病", "x", "-0.1", "绝经期", "x", "-0.1", "心血管内科", "x", "-0.1", "冠状动脉", "x", "-0.1",
                     "维生素A", "x", "-0.1", "心律不齐", "x", "-0.1", "心血管系统", "x", "-0.1", "心血管疾病", "x", "-0.1", "自由基", "x",
                     "-0.1", "脂肪酸", "x", "-0.1", "解放军总医院", "x", "-0.1", "胆固醇", "x", "-0.1", "维生素", "x", "-0.1", "降火",
                     "x", "-0.1", "养心", "x", "-0.1", "血糖", "x", "-0.1", "代谢", "x", "-0.1", "衰老", "x", "-0.1", "杨水祥",
                     "nr", "-0.1", "桑杞", "nr", "-0.1", "曾强", "nr", "-0.1", "内分泌学", "nz", "-0.1", "药用植物", "nz", "-0.1",
                     "肾经", "nz", "-0.1", "地方", "n", "-0.5", "脖子", "n", "-0.1", "材料", "n", "-0.1", "男性", "n", "-0.1",
                     "风险", "n", "-0.1", "信号", "n", "-0.1", "女性", "n", "-0.1", "放入", "n", "-0.1", "主任", "n", "-0.1",
                     "身体", "n", "-0.1", "做法", "n", "-0.1", "内皮", "n", "-0.1", "伙夫", "n", "-0.1", "矿物质", "n", "-0.1",
                     "喉结", "n", "-0.1", "皮尺", "n", "-0.1", "酸性", "n", "-0.1", "甘苦", "n", "-0.1", "沸水", "n", "-0.1",
                     "有机酸", "ne", "-0.1", "桑椹", "ne", "-0.1", "作用", "k", "-0.1"]
    source = '润德教育'

    classify_result = classify_request(ID, user, title, split_title, split_content, source, features_list)
    print title + '\t' + classify_result


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
