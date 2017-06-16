import codecs
import json

data = codecs.open("result5-10.json", 'r', 'utf-8')
result = codecs.open("unique5-10.json", 'w', 'utf-8')
title_set = set()
index = 0
for line in data:
    if index % 10000 == 0:
        print index
    index += 1
    json_object = json.loads(line.strip(), 'utf-8')
    title = json_object['title']
    if title in title_set:
        continue
    else:
        title_set.add(title)
    result.write(line)

data.close()
result.close()
