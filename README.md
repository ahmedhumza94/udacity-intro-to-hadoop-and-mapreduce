# udacity-intro-to-hadoop-and-mapreduce
This repository contains python code for MapReduce jobs to answer questions about Udacity forum data.

This project is compatible with the Cloudera VM distribution described in this setup document:
https://d20vrrgs8k4bvw.cloudfront.net/documents/en-IN/BigDataVM.pdf

The code found in the forum_project folder was used to accomplish the following tasks related to
the forum dataset freely available as part of the Intro to Hadoop and MapReduce course by
Udacity:

## Project Tasks

(Task descriptions are copied from the project description)

Solutions are made to match the general output formats described here:
https://www.udacity.com/wiki/ud617/local-testing-instructions

### Task 1
In this exercise your task is to find for each student what is the hour during which the student
has posted the most posts. Output from reducers should be:
```
author_id    hour
```
For example:
```
13431511\t13
54525254141\t21
```
If there is a tie: there are multiple hours during which a student has posted a maximum number of 
posts, please print the student-hour pairs on separate lines. The order in which these lines 
appear in your output does not matter.

You can ignore the time-zone offset for all times - for example in the following line: 
"2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.

In order to find the hour posted, please use the date_added field and NOT the last_activity_at field.

#### Solution Code

Solution code for this task can be found in the studentTimesMapper.py and studentTimesReducer.py files.

### Task 2

Write a mapreduce program that would process the forum_node data and output the length of the post 
and the average answer (just answer, not comment) length for each post. You will have to decide 
how to write both the mapper and the reducer to get the required result.

#### Solution Code

Solution code for this taskcan be found in the studentPostAnsMapper.py	and studentPostAnsReducer.py 
files.

### Task 3

Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.

#### Solution Code

Solution code for this task can be found in the topTenTagsMapper.py	and topTenTagsReducer.py files.

### Task 4

As the first step for this analysis we have been tasked with writing a mapreduce program that for each 
forum thread (that is a question node with all it's answers and comments) would give us a list of 
students that have posted there - either asked the question, answered a question or added a comment. 
If a student posted to that thread several times, they should be added to that list several times as 
well, to indicate intensity of communication.

#### Solution Code

Solution code for this task can be found in the studyGroupsMapper.py	and studyGroupsReducer.py	files.

