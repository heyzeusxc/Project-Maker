import datetime
import time
import csv
import os
import sys

print '*' * 10
print ''
print 'Starting timekeeper. . .'
print ''
print str(datetime.date.today())
print ''

log = [['Date','Project','Hours']]
date = str(datetime.date.today())
commands = ['NP - New Project','Save - Saves a .csv file of the current log']
date = str(datetime.date.today())
log_name = str(datetime.date.today()) + ' Hour Log.csv'

def new_project():
	project = raw_input('Enter Project: ' )
	print project
	print ''

	start = raw_input('Type "Start" to start counter: ')

	while True:

		time_read = time.strftime('%I:%M %p', time.localtime())

		if start.lower() == 'start':
			start_time = time.time()
			print time_read
			break
		else:
			start = raw_input('Type "Start" to start counter: ')
	print ''

	stop = raw_input('Type "Stop" to stop counter: ')

	while True:

		time_read = time.strftime('%I:%M %p', time.localtime())

		if stop.lower() == 'stop':
			end_time = time.time()
			length = (end_time - start_time)/60.0/60.0
			length = str(length)[:str(length).find('.') + 3] + ' hours'
			print time_read
			print length
			print ''
			entry = [date, project, length]
			return entry
		else:
			stop = raw_input('Type "Stop" to stop counter: ')

def save():
	if log_name in os.listdir(os.sys.path[0]):
		with open(os.sys.path[0] + '/' + log_name, 'a') as original:
			typer = csv.writer(original)
			for x in log[1:]:
				typer.writerow(x)
	else:
		with open(os.sys.path[0] + '/' + log_name, 'wb') as save_data:
			typer = csv.writer(save_data)
			for x in log:
				typer.writerow(x)

for x in commands:
	print x

print ''


while True:
	input = raw_input('Enter Command: ')
	if input.lower() == 'np':
		print 'New Project'
		print ''
		add_project = new_project()
		log.append(add_project)
	elif input.lower() == 'save':
		print 'Save'
		print ''
		for y in log:
			print y
		print ''
		save()
		break