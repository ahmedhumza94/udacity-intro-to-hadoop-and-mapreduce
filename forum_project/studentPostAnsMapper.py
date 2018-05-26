#!/usr/bin/python

#This script will take the forum data tsv and output post lengths (keys) and answer lengths (values) 
#seperated by tabs with a question or answer identifiter: Ex: node_id\tq\tbody_len

#Import libraries
import sys
import csv

#Create reader object
reader = csv.reader(sys.stdin, delimiter='\t')
#Skip header line
reader.next()
#For each line in reader 
for line in reader:
#Check if number of fields is correct 
   if len(line) == 19:
	#Get node type 
	node_type = line[5]
	#Body Length
	bodylen = len(line[4])
	#Node ID
	node_id = line[0]
	#parent id to connect answers to questions
	parent_id = line[6]
	#Print output of question or answer respectively
	if node_type == 'question':
		print "{0}\tq\t{1}".format(node_id,bodylen)
        if node_type == 'answer':
		print "{0}\ta\t{1}".format(parent_id,bodylen)

