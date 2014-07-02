import sys
import os
import csv
import time

root = os.sys.path[0] #sets root
flist = []
loose = []
lastslash = root[::-1].find('/')
drive = root[::-1][:lastslash][::-1] #sets drive name
firstline = ['Project Number','Project Title','Total Size','"01_Recording" Size','"02_Edit" Size','"03_Live" Size','Folder Name','Drive']
loosebytes = 0

for x in os.walk(os.sys.path[0]): #looks for .txt files to add
	for y in x[2]:
		if y == 'datasize.txt': #finds all datasize.txt 
			flist.append(str(x[0]) + '/' + str(y))

for a in os.listdir(root): #adds loose files in the root
	loose.append(a)

for b in loose:
	if len(b[2]) > 0: #checks if files are found
		if b[0] != '.':
			loosebytes += os.path.getsize(root + '/' + b)

if loosebytes/1024 == 0:
	LBtext = str(loosebytes) + ' B'
elif loosebytes/1024/1024 == 0:
	LBtext = str(loosebytes/1024) + ' KB'
elif loosebytes/1024/1024/1024 == 0:
	LBtext = str(loosebytes/1024/1024) + ' MB'
elif loosebytes/1024/1024/1024/1024 == 0:
	LBtext = str(loosebytes/1024/1024/1024) + ' GB'
elif loosebytes/1024/1024/1024/1024/1024 == 0:
	LBtext = str(loosebytes/1024/1024/1024/1024) + ' TB'

if len(flist) == 0:
	print 'No "datasize.txt" files found'
else:
	dlout = open(root + '/' + drive + ' drivedata.csv', 'w') #creates .csv file for summary of all datasize.txt files
	typer = csv.writer(dlout)
	typer.writerow(firstline)
	for x in flist:
		foldslash = x.find('/',lastslash) + 1
		folder = x[foldslash:x.find('/',foldslash)]
		f = open(x,'rU') #opens the datasize.txt file
		print '*' * len(x)
		print x
		print '*' * len(x)
		entry = ['-','-','-','-','-','-',folder,drive]
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
	looseentry = ['Loose Files','-',LBtext,'-','-','-','-',drive]
	typer.writerow(looseentry)