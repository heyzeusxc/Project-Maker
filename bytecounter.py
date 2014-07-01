import os
import sys
import time

root = os.sys.path[0] #sets root folder
check = os.walk(root)	#creates list of all files and folders in root
subcheck = os.listdir(root) #checks for subfolder structure made by projectmaker

print ''
print '-----------------------------------------------------------------------------------------------'
print ''

#time.sleep(1)

print ''
print 'Computing size of: ' + root
print ''

#time.sleep(2)

bytes = 0
subbytes1 = 0
subbytes2 = 0
subbytes3 = 0

subcheck = os.listdir(root)

for x in check:
	if len(x[2]) > 0: #checks if folders are found
		for y in x[2]: #every file in a folder
			print x[0] + '/' + y + ', ' + str(os.path.getsize(x[0] + '/' + y)) + ' bytes'
			bytes += os.path.getsize(x[0] + '/' + y) #adds byte size
#			time.sleep(0.25)

for x in subcheck: #checks subfolders for folders made by projectmaker
	if x == '01_Recording':
		check = os.walk(root + '/' + x)
		for x in check:
			if len(x[2]) > 0: #checks if folders are found
				for y in x[2]: #every file in a folder
#					print x[0] + '/' + y + ', ' + str(os.path.getsize(x[0] + '/' + y)) + ' bytes'
					subbytes1 += os.path.getsize(x[0] + '/' + y) #adds byte size
	if x == '02_Edit':
		check = os.walk(root + '/' + x)
		for x in check:
			if len(x[2]) > 0: #checks if folders are found
				for y in x[2]: #every file in a folder
#					print x[0] + '/' + y + ', ' + str(os.path.getsize(x[0] + '/' + y)) + ' bytes'
					subbytes2 += os.path.getsize(x[0] + '/' + y) #adds byte size

	if x == '03_Live':
		check = os.walk(root + '/' + x)
		for x in check:
			if len(x[2]) > 0: #checks if folders are found
				for y in x[2]: #every file in a folder
#					print x[0] + '/' + y + ', ' + str(os.path.getsize(x[0] + '/' + y)) + ' bytes'
					subbytes3 += os.path.getsize(x[0] + '/' + y) #adds byte size

print ''

dout = open(root + '/' + 'datasize.txt','w') #creates .txt summarizing project and subfolder size

lastslash = root [::-1].find('/')
project = root[::-1][:lastslash][::-1]

if 'C' in project:
	firstc = project.find('C')
	if project[firstc + 1:firstc + 2].isdigit():
		tsep = project.find('-')
		if tsep == -1:
			tsep = project.find(' ')
		elif tsep >= 5:
			tsep = project.find(' ')
		ptitle = project[tsep + 3:]
		pnumb = project[:tsep]
		print 'Project Number'
		print pnumb
		dout.write('Project Number')
		dout.write('\r')
		dout.write(pnumb)
		dout.write('\r')
		dout.write('\r')
		
		print ''

		print 'Project Title'
		print ptitle
		dout.write('Project Title')
		dout.write('\r')
		dout.write(ptitle)
		dout.write('\r')

		print ''

#time.sleep(1)

bytecount = 0
bytecount1 = 0
bytecount2 = 0
bytecount3 = 0

bytecounter = '{:,}'.format(bytes)
bytecounter1 = '{:,}'.format(subbytes1)
bytecounter2 = '{:,}'.format(subbytes2)
bytecounter3 = '{:,}'.format(subbytes3)

for x in bytecounter:
	if x == ',':
		bytecount += 1

for x in bytecounter1:
	if x == ',':
		bytecount1 += 1

for x in bytecounter2:
	if x == ',':
		bytecount2 += 1

for x in bytecounter3:
	if x == ',':
		bytecount3 += 1

if bytes != 0:
	dout.write('\r')
	print 'Total Project Size'
	dout.write('Total Project Size')
	dout.write('\r')
	if bytecount == 0:
		print str(bytes) + ' bytes'
		dout.write(str(bytes) + ' bytes')
		dout.write('\r')
	elif bytecount == 1:
		print str(bytes)[:bytecounter.find(',')] + '.' + str(bytes)[bytecounter.find(','):bytecounter.find(',') + 2] + ' kB'
		dout.write(str(bytes)[:bytecounter.find(',')] + '.' + str(bytes)[bytecounter.find(','):bytecounter.find(',') + 2] + ' kB')
		dout.write('\r')
	elif bytecount == 2:
		print str(bytes)[:bytecounter.find(',')] + '.' + str(bytes)[bytecounter.find(','):bytecounter.find(',') + 2] + ' MB'
		dout.write(str(bytes)[:bytecounter.find(',')] + '.' + str(bytes)[bytecounter.find(','):bytecounter.find(',') + 2] + ' MB')
		dout.write('\r')
	elif bytecount == 3:
		print str(bytes)[:bytecounter.find(',')] + '.' + str(bytes)[bytecounter.find(','):bytecounter.find(',') + 2] + ' GB'
		dout.write(str(bytes)[:bytecounter.find(',')] + '.' + str(bytes)[bytecounter.find(','):bytecounter.find(',') + 2] + ' GB')
		dout.write('\r')

#time.sleep(0.5)

if subbytes1 != 0:
	dout.write('\r')
	print ''
	print '"01_Recording" Size'
	dout.write('"01_Recording" Size')
	dout.write('\r')
	if bytecount1 == 0:
		print str(subbytes1) + ' bytes'
		dout.write(str(subbytes1) + ' bytes')
		dout.write('\r')
	elif bytecount1 == 1:
		print str(subbytes1)[:bytecounter1.find(',')] + '.' + str(subbytes1)[bytecounter1.find(','):bytecounter1.find(',') + 2] + ' kB'
		dout.write(str(subbytes1)[:bytecounter1.find(',')] + '.' + str(subbytes1)[bytecounter1.find(','):bytecounter1.find(',') + 2] + ' kB')
		dout.write('\r')
	elif bytecount1 == 2:
		print str(subbytes1)[:bytecounter1.find(',')] + '.' + str(subbytes1)[bytecounter1.find(','):bytecounter1.find(',') + 2] + ' MB'
		dout.write(str(subbytes1)[:bytecounter1.find(',')] + '.' + str(subbytes1)[bytecounter1.find(','):bytecounter1.find(',') + 2] + ' MB')
		dout.write('\r')
	elif bytecount1 == 3:
		print str(subbytes1)[:bytecounter1.find(',')] + '.' + str(subbytes1)[bytecounter1.find(','):bytecounter1.find(',') + 2] + ' GB'
		dout.write(str(subbytes1)[:bytecounter1.find(',')] + '.' + str(subbytes1)[bytecounter1.find(','):bytecounter1.find(',') + 2] + ' GB')
		dout.write('\r')

#time.sleep(0.5)

if subbytes2 != 0:
	dout.write('\r')
	print ''
	print '"02_Edit" Size'
	dout.write('"02_Edit" Size')
	dout.write('\r')
	if bytecount2 == 0:
		print str(subbytes2) + ' bytes'
		dout.write(str(subbytes2) + ' bytes')
		dout.write('\r')
	elif bytecount2 == 1:
		print str(subbytes2)[:bytecounter2.find(',')] + '.' + str(subbytes2)[bytecounter2.find(','):bytecounter2.find(',') + 2] + ' kB'
		dout.write(str(subbytes2)[:bytecounter2.find(',')] + '.' + str(subbytes2)[bytecounter2.find(','):bytecounter2.find(',') + 2] + ' kB')
		dout.write('\r')
	elif bytecount2 == 2:
		print str(subbytes2)[:bytecounter2.find(',')] + '.' + str(subbytes2)[bytecounter2.find(','):bytecounter2.find(',') + 2] + ' MB'
		dout.write(str(subbytes2)[:bytecounter2.find(',')] + '.' + str(subbytes2)[bytecounter2.find(','):bytecounter2.find(',') + 2] + ' MB')
		dout.write('\r')
	elif bytecount2 == 3:
		print str(subbytes2)[:bytecounter2.find(',')] + '.' + str(subbytes2)[bytecounter2.find(','):bytecounter2.find(',') + 2] + ' GB'
		dout.write(str(subbytes2)[:bytecounter2.find(',')] + '.' + str(subbytes2)[bytecounter2.find(','):bytecounter2.find(',') + 2] + ' GB')
		dout.write('\r')

#time.sleep(0.5)

if subbytes3 != 0:
	dout.write('\r')
	print ''
	print '"03_Live" Size'
	dout.write('"03_Live" Size')
	dout.write('\r')
	if bytecount3 == 0:
		print str(subbytes3) + ' bytes'
		dout.write(str(subbytes3) + ' bytes')
		dout.write('\r')
	elif bytecount3 == 1:
		print str(subbytes3)[:bytecounter3.find(',')] + '.' + str(subbytes3)[bytecounter3.find(','):bytecounter3.find(',') + 2] + ' kb'
		dout.write(str(subbytes3)[:bytecounter3.find(',')] + '.' + str(subbytes3)[bytecounter3.find(','):bytecounter3.find(',') + 2] + ' kb')
		dout.write('\r')
	elif bytecount3 == 2:
		print str(subbytes3)[:bytecounter3.find(',')] + '.' + str(subbytes3)[bytecounter3.find(','):bytecounter3.find(',') + 2] + ' MB'
		dout.write(str(subbytes3)[:bytecounter3.find(',')] + '.' + str(subbytes3)[bytecounter3.find(','):bytecounter3.find(',') + 2] + ' MB')
		dout.write('\r')
	elif bytecount3 == 3:
		print str(subbytes3)[:bytecounter3.find(',')] + '.' + str(subbytes3)[bytecounter3.find(','):bytecounter3.find(',') + 2] + ' GB'
		dout.write(str(subbytes3)[:bytecounter3.find(',')] + '.' + str(subbytes3)[bytecounter3.find(','):bytecounter3.find(',') + 2] + ' GB')
		dout.write('\r')

#time.sleep(0.5)

print''
print 'Creating ' + root + '/' + 'datasize.txt'

#time.sleep(1.5)

dout.close()

print ''
print '-----------------------------------------------------------------------------------------------'
print ''

#time.sleep(1)