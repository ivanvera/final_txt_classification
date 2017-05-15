# coding=UTF-8
import sys

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs

data = codecs.open("../../file/total_corpus.json", 'r', 'utf-8')
data_wenhua = codecs.open("../../file/wenhua_corpus.json", 'r', 'utf-8')
data_wenhua_without = codecs.open("../../file/without_wenhua_corpus.json", 'r', 'utf-8')

for line in data:
    split = line.strip().split("\t")
    label = split[3]
    if label == '文化':
        data_wenhua.write(line)
    else:
        data_wenhua_without.write(line)

data.close()
data_wenhua.close()
data_wenhua_without.close()
