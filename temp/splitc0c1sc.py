import cPickle
import codecs
import json
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

data = codecs.open("test.bak", encoding="utf-8")
result = codecs.open("result.json", 'w', encoding="utf-8")
c1 = cPickle.load(open("c1.pkl"))
sc = cPickle.load(open("sc.pkl"))
c0 = cPickle.load(open("c0.pkl"))


def get_content_words_feature(content):
    content = re.sub('_[A-Za-z]+', '', content)
    content = re.sub('http://(.*).jpg', '', content)
    words = content.split()
    words = [word.lower() for word in words if len(word.strip()) > 1]
    return words


# result.write('{\n"RECORDS":[\n')
count = 0
for line in data:
    if not count == 0:
        result.write(",\n")
    count += 1
    json_dic = dict()
    json_object = json.loads(line.strip(), 'utf-8')
    json_dic["ID"] = json_object["id"]
    json_dic["splitTitle"] = ",".join(get_content_words_feature(json_object["splitTitle"]))
    json_dic["splitContent"] = ",".join(get_content_words_feature(json_object["splitContent"]))

    class_info = json_object["class"]
    if len(class_info) == 0:
        print "class null"
        continue
    json_dic["weight"] = class_info[2]
    index = 0
    while index < len(class_info):
        if class_info[index] in c0:
            json_dic["c0"] = class_info[index]
        elif class_info[index] in c1:
            json_dic["c1"] = class_info[index]
        else:
            json_dic["sc"] = class_info[index]

        index += 3

    raw_document = json.dumps(json_dic, encoding="utf-8", ensure_ascii=False)
    result.write(raw_document)


# result.write('\n]\n}')
