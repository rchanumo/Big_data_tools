import sys
from heapq import heapify, heappush, heappop

top10 = []
count = 0
prev_tag = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue    
    
    tag = data_mapped
    if(prev_tag is not None and prev_tag!=tag):
        heappush(top10, (count, prev_tag))
        if(len(top10) > 10):
            _ = heappop(top10)
        count = 0

    count += 1
    prev_tag = tag

heappush(top10, (count, tag))
if(len(top10) > 10):
    _ = heappop(top10)
count = 0

for elem in top10:
    print("{0}\t{1}".format(elem[1], elem[0]))