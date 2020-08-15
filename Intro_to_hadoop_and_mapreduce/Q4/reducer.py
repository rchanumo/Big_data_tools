import sys

student_ids = []
prev_q_id = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue  
    q_id, student_id = data_mapped

    if(prev_q_id is not None and prev_q_id!=q_id):
        print("{0}\t{1}".format(prev_q_id, student_ids))
        student_ids = []

    student_ids.append(student_id) 
    prev_q_id = q_id

print("{0}\t{1}".format(prev_q_id, student_ids))
