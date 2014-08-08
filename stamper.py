"""
Import os, sys, datetime, and shutil.
"""
import sys
import os
import datetime
import shutil

"""
Set variables and checks if the 'datestamper' folder is found.
"""

dlist = os.walk(sys.path[0]).next()[1]
today = datetime.date.today()

if str(today) in dlist:
	pass
else:
	os.mkdir(sys.path[0] + '/' + str(today))

target = os.listdir(os.sys.path[0]).index(str(today))
send = os.sys.path[0] + '/' + os.listdir(os.sys.path[0])[target]
stampinhere = sys.path[0] + '/' + 'datestamper'

"""
Looks in 'datestamper' folder, scans files if found, renames and moves if appropriate.
"""

if 'datestamper' in dlist:
	print '*' * 10
	print 'Datestamper folder found!'
	print ''

	stamplist = os.listdir(stampinhere)

	for m in stamplist:
		if m[0] == '.':
			pass
		elif str(today) in m:
			if m in os.listdir(send):
				pass
			else:
				print 'Moving ' + str(today) + ' ' + m + ' to ' + send
				shutil.move(stampinhere + '/' + m,send)
		else:
			if str(today) in m:
				pass
			else:
				print 'Changing ' + m + ' to ' + str(today) + ' ' +  m
				print ''
				os.rename(str(stampinhere) + '/' + m, str(stampinhere) + '/' + str(today) + ' ' +  m)
				if str(today) + ' ' + m in os.listdir(send):
					pass
				else:
					shutil.move(stampinhere + '/' + str(today) + ' ' + m,send)
					print 'Moving ' + str(today) + ' ' + m + ' to ' + send

	print '*' * 10

else:
	print '*' * 10
	print "datestamper folder not found! Creating a new one, please place files you wish to stamp with today's date in there and rerun the application."
	print '*' * 10
	os.mkdir(sys.path[0] + '/' + 'datestamper')

