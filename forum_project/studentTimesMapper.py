#!/usr/bin/python

#This script will output key,value pairs in form of
#author_id\tpost_hour

#import libraries
import sys
import csv

#create reader object and skip column header line
reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

#loop through input
for line in reader:
	# if line meets log format
	if len(line) == 19:
		#gather post data
		author_id = line[3]
		timestampRaw = line[8]
		#split up timestamp
		date, time = timestampRaw.strip().split(" ")
		hour, minute, second = time.split(":")
		#output author and hour of post
		print "{0}\t{1}".format(author_id, hour)



