import codecs
import copy
import sys

from config.config import FilePathConfig
from feature_extractor.entity.document import Document
from util.util import Util

reload(sys)
sys.setdefaultencoding('utf-8')

corpus = codecs.open(FilePathConfig.total_corpus_path, 'r', FilePathConfig.file_encodeing, 'ignore')
category_dic = Util.load_object_from_pkl(FilePathConfig.category_pkl_path)

total_dic = {}
count_dic = {}
for key in category_dic.keys():
    count_dic[key] = 0

for line in corpus:
    document = Document(line)
    label = document.label
    words = document.get_content_words_feature()
    for word in words:
        if word not in total_dic:
            total_dic[word] = copy.deepcopy(count_dic)
        total_dic[word][label] += 1

for key, value in count_dic.iteritems():
    print key, value
