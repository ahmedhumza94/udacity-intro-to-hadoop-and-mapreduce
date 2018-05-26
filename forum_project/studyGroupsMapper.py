#!/usr/bin/python

#This script will take the forum data tsv file and output key, value pairs
#of node_id\tauthor_id

#import libraries
import sys
import csv

#create reader object
reader = csv.reader(sys.stdin,delimiter='\t')
#Skip column header line
reader.next()
#Loop through input
for line in reader:
	#Check if number of fields is correct 
	if len(line) == 19:
		#Gather forum post information
		author_id = line[3]
		abs_parent_id = line[7]
		node_type = line[5]
		node_id = line[0]
		#Check if node is a question. If so it doesn't have a parent id so we will output its id
		if node_type == 'question':
			print"{0} \t{1}".format(node_id,author_id)
		else:
		#For other posts use parent id to link it to a particular question thread
			print"{0} \t{1}".format(abs_parent_id,author_id)
