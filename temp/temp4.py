import codecs
import json

data = codecs.open("db_json_10-15.txt", "r", "utf-8")
index_null = 0
index_vedio = 0
index_without_content = 0
index = 0
category_dic = {}

for line in data:
    index += 1
    if index % 10000 == 0:
        print index

    if line.strip() == 'null':
        index_null += 1
        continue

    if ':"video",' in line:
        index_vedio += 1
        continue

    json_object = json.loads(line, strict=False)
    if "splitContent" not in json_object:
        index_without_content += 1
        continue

    if json_object.has_key("category"):
        for category in json_object["category"]:
            if category not in category_dic:
                category_dic[category] = 0
            category_dic[category] += 1

print index_null, index_vedio, index_without_content
for key, value in category_dic.iteritems():
    print key, value

data.close()
