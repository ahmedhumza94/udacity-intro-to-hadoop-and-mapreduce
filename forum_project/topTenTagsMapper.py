#!/usr/bin/python

#THis script outputs key value pairs of tag\t1 where 1 represents a single 
#occurrence of a tag in a question node

#import libraries
import sys
import csv

#create reader object of input tsv file
reader = csv.reader(sys.stdin,delimiter='\t')
#skip first line of headers
reader.next()
for line in reader:
	#Check if number of fields is correct 
	if len(line) == 19:
		#Gather tag and node info
		tagsRaw = line[2]
		node_type = line[5]
		#Check if node is question
		if node_type == 'question':
		#Print out all tags
			for tag in tagsRaw.split():
				print "{0}\t1".format(tag)
