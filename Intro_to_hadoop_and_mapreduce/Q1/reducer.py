import sys

hour_max_activity = None
prev_id = None
count = {} #count number of times author posted at a specific hour
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    author_id, hour = data_mapped
    if(author_id != prev_id and prev_id is not None):
        max_activity = max(list(count.values()))
        for h in count.keys():
            if(count[h] == max_activity):
                print "{0}\t{1}".format(prev_id, h)
        count = {}

    count.setdefault(hour,0)
    count[hour] += 1
    prev_id = author_id

max_activity = max(list(count.values()))
for h in count.keys():
    if(count[h] == max_activity):
        print "{0}\t{1}".format(author_id, h)