import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

for data in reader:
    if(len(data) == 19):
        tagnames, node_type = data[2], data[5]
        if(node_type == 'question'):
            tagnames = tagnames.split(' ')
            tagnames = set(tagnames)
            for tagname in tagnames:
                print(tagname)
