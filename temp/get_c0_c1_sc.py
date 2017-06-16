import codecs

data = codecs.open("c0_c1_scRelation.txt", 'r', "utf-8")
c1_set = list()
sc_set = list()
c0_set = list()

c1_result = codecs.open("c1.txt", 'w', 'utf-8')
sc_result = codecs.open("sc.txt", 'w', 'utf-8')
c0_result = codecs.open("c0.txt", "w", "utf-8")
for line in data:
    print line.strip()
    if "c0" in line:
        c0 = line[line.index("c0=") + 3:line.index(",c1=")]
        if c0 not in c0_set:
            c0_set.append(c0)

    if "c1" in line:
        if "sc" in line:
            c1 = line[line.index("c1=") + 3:line.index(",sc=")]
        else:
            c1 = line[line.index("c1=") + 3:].strip()

        if c1 not in c1_set:
            c1_set.append(c1)

    if "sc" in line:
        sc = line.split('sc=')[1].strip()
        if sc not in sc_set:
            sc_set.append(sc)

for item in c1_set:
    c1_result.write(item + '\n')

for item in sc_set:
    sc_result.write(item + '\n')

for item in c0_set:
    c0_result.write(item + '\n')

import cPickle

cPickle.dump(c1_set, open("c1.pkl", "w"))
cPickle.dump(sc_set, open("sc.pkl", 'w'))
cPickle.dump(c0_set, open("c0.pkl", 'w'))

c0_result.close()
c1_result.close()
sc_result.close()
