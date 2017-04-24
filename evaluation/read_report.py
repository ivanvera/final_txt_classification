import cPickle
import codecs

report_file_name = "../file/" + "result_report-2017-04-21-17-24-lr.pkl"
report = cPickle.load(open(report_file_name, 'r'))
confusion_matrix = report.confusion_matrix
labels = report.labels
file = codecs.open("asd.csv", "w", encoding="utf-8")

for i in range(confusion_matrix.shape[0]):
    file.write("," + labels[i][0:2])
file.write("\n")
for i in range(confusion_matrix.shape[0]):
    file.write(labels[i][0:2])
    for j in range(confusion_matrix.shape[1]):
        file.write("," + str(confusion_matrix[i][j]))
    file.write("\n")
file.close()
