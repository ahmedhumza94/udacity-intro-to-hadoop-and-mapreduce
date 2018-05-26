#!/usr/bin/python

#This script finds hour in which a user posted the most on the udacity forum. The mapper should 
# output should be in format author_id\thour

#Import sys library
import sys

#Create list that will keep track of the number of posts in each hour. 
hourCountList = 24*[0]
#Default key is None. This will be author_id during iterations
oldKey = None

#loop through each stdin line split by tabs
for line in sys.stdin:
	data = line.strip().split('\t')
	#Check if line contains right amount of tab separated fields
	if len(data) != 2:
		continue
	#Multiple assignment of input
	thisKey, postHour = data
	#Check if key has changed
	if oldKey and oldKey != thisKey:
		maxCount = max(hourCountList)
		clockHour = 0
		#If key has changed print hour(s) during the day with the most number of user posts 
		for hourCount in hourCountList:
			if hourCount == maxCount:
				print"{0}\t{1}".format(oldKey,clockHour)
			clockHour += 1
		hourCountList = 24*[0]
	#Set Key and iterate counter
	oldKey = thisKey
	hourCountList[int(postHour)] +=1

#Output results of final key
if oldKey != None:
	maxCount = max(hourCountList)
	clockHour = 0
	for hourCount in hourCountList:
		if hourCount == maxCount:
			print"{0}\t{1}".format(oldKey,clockHour)
		clockHour += 1

			
