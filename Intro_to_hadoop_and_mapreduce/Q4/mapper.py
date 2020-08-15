import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

for data in reader:
    if(len(data) == 19):
        id, author_id, node_type, parent_id = data[0], data[3], data[5], data[6]
        if(node_type == 'question'):
            print("{0}\t{1}".format(id, author_id))
        elif(node_type == 'answer'):
            print("{0}\t{1}".format(parent_id, author_id))
        else:
            pass