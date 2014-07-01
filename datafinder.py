import sys
import os
import csv
import time

root = os.sys.path[0] #sets root
rcheck = os.walk(root) #makes a list of files in root
flist = []

lastslash = root[::-1].find('/')
drive = root[::-1][:lastslash][::-1]

firstline = ['Project Number','Project Title','Total Project Size','"01_Recording" Size','"02_Edit" Size','"03_Live" Size','Drive']

for x in rcheck:
	for y in x[2]:
		if y == 'datasize.txt': #finds all datasize.txt 
			flist.append(str(x[0]) + '/' + str(y)) #adds file to list to get processed
if len(flist) == 0:
	print 'No "datasize.txt" files found'
else:
	dlout = open(root + '/' + drive + ' drivedata.csv', 'w') #creates .csv file for summary of all datasize.txt files
	typer = csv.writer(dlout)
	typer.writerow(firstline)
	for x in flist:
		f = open(x,'rU') #opens the datasize.txt file
		print '*' * len(x)
		print x
		print '*' * len(x)
		entry = ['-','-','-','-','-','-',drive]
		for z in f: #goes through each line of the file
			if 'Project Number' in z:
				entry[0] = f.next()[::-1][1:][::-1]
			elif 'Project Title' in z:
				entry[1] = f.next()[::-1][1:][::-1]
			elif 'Total Project Size' in z:
				entry[2] = f.next()[::-1][1:][::-1]
			elif '"01_Recording" Size' in z:
				entry[3] = f.next()[::-1][1:][::-1]
			elif '"02_Edit" Size' in z:
				entry[4] = f.next()[::-1][1:][::-1]
			elif '"03_Live" Size' in z:
				entry[5] = f.next()[::-1][1:][::-1]
		typer.writerow(entry)
		f.close()