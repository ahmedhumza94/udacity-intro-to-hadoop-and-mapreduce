#!/usr/bin/python

#This script will reducer key, value pairs of node_id and author id into a 
#key, list pair of node_id and list of authors for that node separated by a tab.

#import library
import sys

#Set default key and empty author list
oldKey = None
authorList = []

#Loop through input
for line in sys.stdin:
	#Split data into key and author
	data = line.strip().split('\t')
	#Check if input contains correct number of fields
	if len(data) !=2:
		continue
	thisKey, author_id = data
	#Check if key has changed and print out all authors for that node
	if oldKey and oldKey != thisKey:
		print"{0}\t{1}".format(oldKey,authorList)
	#Reset author list
		authorList =[]
	#Set key and update author
	oldKey = thisKey
	authorList.append(author_id)

#Output results for final key
if oldKey != None:
	print"{0}\t{1}".format(oldKey,authorList)
