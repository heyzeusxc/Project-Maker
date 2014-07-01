import sys
import os
import datetime

dlist = os.walk(sys.path[0]).next()[1]


if 'datestamper' in dlist: #checks if the date stamper folder is in root
	print ''
	print 'Folder found!'
	print ''
	stampinhere = sys.path[0] + '/' + 'datestamper'
	stamplist = os.listdir(stampinhere)
	for m in stamplist:
		print 'Changing ' + m + ' to ' + str(datetime.date.today()) + ' ' +  m
		os.rename(str(stampinhere) + '/' + m, str(stampinhere) + '/' + str(datetime.date.today()) + ' ' +  m)
	os.mkdir(sys.path[0] + '/' + str(datetime.date.today()))
	print ''

else: #makes a datestamper folder if not found
	print ''
	print "datestamper folder not found! Creating a new one, please place files you wish to stamp with today's date in there and rerun the application."
	print ''
	os.mkdir(sys.path[0] + '/' + 'datestamper')