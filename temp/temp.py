import codecs
import json

data = codecs.open("unlabeled_news.json", "r", "utf-8")
filterd_data = codecs.open("unlabeled_news2.json", "w", "utf-8")
index = 0
index2 = 0
for line in data:
    index2 += 1
    if index2 % 10000 == 0:
        print index2
    if line.strip() == 'null':
        index += 1
        print index, 'null'
        continue

    json_object = json.loads(line, strict=False)
    if "splitContent" not in json_object:
        index += 1
        print index, line
        continue

    splitContent = json_object['splitContent']
    if len(splitContent.spilt()) < 8:
        index += 1
        print index, line
        continue

    filterd_data.write(line.strip() + '\n')

data.close()
filterd_data.close()
