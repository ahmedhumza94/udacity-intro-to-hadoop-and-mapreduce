#!/usr/bin/python

#This Script will reduce forum input in form of node_id\tnode_type\tbody_length to
#output node_type\tquestion_length\taverage_ans_length

#import sys library
import sys
#list of answerLengths per key
answerLengths = []
#default question len to 0
qLen = 0
#Set default key to none which will be question id during loop
oldKey = None

for line in sys.stdin:
	data = line.strip().split('\t')
	#Check if input contains correct number of fields
	if len(data) !=3:
		continue
	#multiple assignment
	thisKey, node_type, body_len = data
	#See if key switched
	if oldKey and oldKey != thisKey:
		# If no answers print 0 as avg answer length
		if len(answerLengths) == 0:
			print"{0}\t{1}\t0".format(oldKey,qLen)
		else:
		#Otherwise calculate avg
			avgAnsLen = float(sum(answerLengths))/len(answerLengths)
			print"{0}\t{1}\t{2}".format(oldKey,qLen,avgAnsLen)
		qLen = 0
		answerLengths = []
	#Set oldKey
	oldKey = thisKey
	#Check node_type
	if node_type =='q':
		qLen = body_len
	if node_type == 'a':
		answerLengths.append(int(body_len))
#Output results of final key
if oldKey != None:
	# If no answers print 0 as avg answer length
	if len(answerLengths) == 0:
		print"{0}\t{1}\t0".format(oldKey,qLen)
	else:
	#Otherwise calculate avg
		avgAnsLen = float(sum(answerLengths))/len(answerLengths)
		print"{0}\t{1}\t{2}".format(oldKey,qLen,avgAnsLen)
