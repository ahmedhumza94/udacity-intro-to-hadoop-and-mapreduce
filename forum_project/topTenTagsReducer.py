#!/usr/bin/python

#This script reduces input in form of tag\t1 to output
#a sorted list of the topTen tags in form of tag\tcount

#import library
import sys

#Set counter of tag freq to 0
count = 0
#set default key to None
oldKey = None
# top ten Dict
topTen = {}
#least count in topTen
lowestTagCount = 0
#Loop through input

for line in sys.stdin:
	#Split input
	data = line.strip().split('\t')
	#Check if input contains correct number of fields
	if len(data) !=2:
		continue
	thisKey, num_validator = data
	#Check if key has changed
	if oldKey and oldKey != thisKey:
	#Check if topTen dict is full
		if len(topTen) == 10:
		#if full check if latest key has a a topTen tag count
			topTenInverseTuple = [(value, key) for key, value in topTen.items()]
			lowestTagCount = min(topTenInverseTuple)
		#if latest count makes it to the top 10 delete the current last place tag
			if count > lowestTagCount[0]:
				del topTen[lowestTagCount[1]]
				topTen[oldKey] = count
			
		else:
		#If there is empty space in dict add the tag 
			topTen[oldKey] = count
		#Reset count
		count = 0
	#Set key and update count
	oldKey = thisKey
	count += 1 
#Check last tag count and update topTen dict if necessary
if oldKey == None:
	if len(topTen) == 10:
		topTenInverseTuple = [(value, key) for key, value in topTen.items()]
		lowestTagCount = min(topTenInverseTuple)
		if count > lowestTagCount[0]:
			del topTen[lowestTagCount[1]]
			topTen[oldKey] = count
		
	else:
		topTen[oldKey] = count
#Sort and print the topTen tags by value and then by key

for tagTuple in sorted(topTen.items(), key = lambda kv: (-kv[1], kv[0])):
	print"{0}\t{1}".format(tagTuple[0],tagTuple[1])
