"""
Q. In this exercise your task is to find for each student what is the hour during which the student has posted the most posts. 
Output from reducers should be:
**
13431511\t13
54525254141\t21
**
If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, 
please print the student-hour pairs on separate lines. The order in which these lines appear in your output does not matter.

You can ignore the time-zone offset for all times - for example in the following line: "2012-02-25 08:11:01.623548+00" - 
you can ignore the +00 offset.

In order to find the hour posted, please use the date_added field and NOT the last_activity_at field.
"""

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next() #skip first line

for data in reader:
    if len(data) == 19:
        author_id, date_time = data[3], data[8]
        time = date_time.split(' ')[1]
        hour = time.split(':')[0]
        print "{0}\t{1}".format(author_id, hour)