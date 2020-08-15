import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

for data in reader:
    if(len(data) == 19):
        id, body, node_type, parent_id = data[0], data[4], data[5], data[6]
        if(node_type == 'question'):
            print("{0}\t{1}_{2}".format(id, len(body), 'q'))
        elif(node_type == 'answer'):
            print("{0}\t{1}_{2}".format(parent_id, len(body), 'a'))
        else:
            pass
