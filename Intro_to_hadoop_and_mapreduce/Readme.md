#Intro to Hadoop and Mapreduce

## Project:

These scripts process data about users of and posts on Udacity's forums: 'forum_node.tsv'. To run on local env: 'student_test_posts.tsv'.

** Q1) This mapreduce code finds for each student what is the hour during which the student has posted the most posts.

** Q2) This mapreduce code outputs the length of the post and the average answer (just answer, not comment) length for each post.

** Q3) This mapreduce code finds the top 10 tags, ordered by the number of questions they appear in.

** Q4) This mapreduce code, for each forum thread (that is a question node with all it's answers and comments) give a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they are added to that list several times as well, to indicate intensity of communication.