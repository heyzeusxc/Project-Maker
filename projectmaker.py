import sys
import os
import time


print ''
print '-----------------------------------------------------------------------------------------------'
print ''

#time.sleep(1)

print 'Folders will be made in "' + str(os.sys.path[0]) + u'\033[1m%s\033[0m' %  '/***PROJECT NUMBER - TITLE***' + '"'

print ''

#time.sleep(1)

pnumber = raw_input('Enter project number: ') #sets project folder name

pnumber = pnumber.upper()

pdesc = raw_input('Enter a project title: ') #sets project folder description

#time.sleep(1)

print ''
print 'Creating "' + str(os.sys.path[0]) + '/' + pnumber + ' - ' +  pdesc + '"'
print ''

pdirect = os.sys.path[0] + '/' + pnumber  + ' - ' + pdesc #sets folder to be made

i = 0
s = 0
editroot = pdirect + '/02_Edit'
editsub = ['/Graphics','/Audio','/Exports','/Notes','/Exports/datestamper']
lfolder = '/03_Live'
uinp = ['y','ye','yes','n','no']

os.mkdir(pdirect) #creates folder

#time.sleep(1)

cams = raw_input('How many cameras/inputs were used for this project or shoot? (Limit of eight (8)): ') #sets number of camera folders to be made if needed

while cams.isdigit() != True:
	print 'Invalid input'
	print ''
#	time.sleep(1)
	cams = raw_input('How many cameras/inputs were used for this project or shoot? (Limit of eight (8)): ')

else:
	cams = int(cams)
#	time.sleep(1)
	print str(cams) + ' cameras/inputs used'

print ''
#time.sleep(1)

streamcheck = raw_input('Will there be a live stream for this project? (y/n): ') #sets if '03_Live' folder will be made, won't if input is 0

while streamcheck.isalpha() != True:
	print 'Invalid input'
	print ''
	streamcheck = raw_input('Will there be a live stream for this project? (y/n): ')

else:
	while streamcheck.lower() not in uinp:
		print 'Invalid input'
		print ''
		streamcheck = raw_input('Will there be a live stream for this project? (y/n): ')

	else:
		if streamcheck.lower() in uinp[:3]:
			print 'Livestream: Yes'
			os.mkdir(pdirect + lfolder) #creates '03_Live'

		elif streamcheck.lower() in uinp[3:]:
			print 'Livestream: No'

		else:
			print 'WTF MATE'

print ''
#time.sleep(1)

if cams != 0:	
	scount = raw_input('How long was the shoot in terms of days? (Limit of seven (7)): ') #creates day subfolders in '/01_Recording', doesn't if == 1
	
	while scount.isdigit() != True:
		print 'Invalid input'
		print ''
		time.sleep(1)
		scount = raw_input('How long was the shoot in terms of days? (Limit of seven (7)): ')
	
	else:
		scount = int(scount)

		os.mkdir(pdirect + '/01_Recording/')

		if scount == 1:
			print 'Length: 1 day'
			rsubfolder = pdirect + '/01_Recording'

			while i != cams:
				i += 1
				os.mkdir(rsubfolder + '/Cam - ' + str(i))
				#print rsubfolder + '/Cam - ' + str(i)

				if i == cams:
					os.mkdir(rsubfolder + '/Audio')
					os.mkdir(rsubfolder + '/Notes')
					#print rsubfolder + '/Audio'
					i = 0
					break

			#print pdirect + '/01_Recording/' + 'Camera'
			#print pdirect + '/01_Recording/' + 'Audio'
		
		else:
			print 'Length: ' + str(scount) + ' days'

			while s != scount:
				s += 1
				os.mkdir(pdirect + '/01_Recording/' + 'Day - ' + str(s))
				rsubfolder = pdirect + '/01_Recording/' + 'Day - ' + str(s)
				#print pdirect + '/01_Recording/' + 'Day - ' + str(s)
				
				while i != cams:
					i += 1
					os.mkdir(rsubfolder + '/Cam - ' + str(i))
					#print rsubfolder + '/Cam - ' + str(i)

					if i == cams:
						os.mkdir(rsubfolder + '/Audio')
						os.mkdir(rsubfolder + '/Notes')
						#print rsubfolder + '/Audio'
						i = 0
						break
					
					if i == 8:
						i = 0
						break

				if s == 7:
					break


#print editroot

os.mkdir(editroot) #creates '/02_Edit' folder

for x in editsub:
	os.mkdir(editroot + x) #creates editing subfolders (graphics, audio, exports, etc.)
	#print editroot + x

#time.sleep(1)

print ''
print 'Project folders have been created.'
print ''

#time.sleep(0.5)

print 'Making "' + str(os.sys.path[0]) + u'\033[1m%s\033[0m' %  '/bytecounter.py' + '"'

bytewriter = open(os.sys.path[0] + '/' + 'bytecounter.py','r')
newbyte = open(pdirect + '/' + 'bytecounter.py','w')

for x in bytewriter:
	newbyte.write(x)

print 'Making "' + str(os.sys.path[0]) + u'\033[1m%s\033[0m' %  '/02_Edit/Exports/stamper.py' + '"'

stamper = open(os.sys.path[0] + '/' + 'stamper.py','r')
newstamp = open(pdirect + '/02_Edit/Exports/stamper.py','w')

for x in stamper:
	newstamp.write(x)

print ''
print '-----------------------------------------------------------------------------------------------'
print ''