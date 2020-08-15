import sys

prev_id = None
q_len = 0
ans_len = 0
n_ans = 0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    id, node_info = data_mapped
    body_len, node_type = node_info.split('_')
    body_len = int(body_len)
    
    if(prev_id is not None and prev_id!=id):
        if(n_ans > 0):
            print("{0}\t{1}\t{2}".format(prev_id, q_len, ans_len/n_ans))
        else:
            print("{0}\t{1}\t{2}".format(prev_id, q_len, 0))
        q_len = 0
        ans_len = 0
        n_ans = 0

    if(node_type == 'q'):
        q_len = body_len
    elif(node_type == 'a'):
        ans_len += body_len
        n_ans += 1
    else:
        continue
    prev_id = id

if(n_ans > 0):
    print("{0}\t{1}\t{2}".format(id, q_len, ans_len/n_ans))
else:
    print("{0}\t{1}\t{2}".format(id, q_len, 0))

    

    
