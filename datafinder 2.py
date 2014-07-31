"""
Import modules
"""
import sys
import os
import csv


"""
Set variables
"""
root = os.sys.path[0]
rootsplit = root.split('/')[1:]
lastslash = root[::-1].find('/')
drive = root[::-1][:lastslash][::-1]
Found_Text_Files = []
Folders = []
FBin = []
Files = []
FolderBytes = 0
FileBytes = 0
i = 0
c = 0
line = '*' * 20
firstline = ['Project Number','Project Title','Total Size','"01_Recording" Size','"02_Edit" Size','"03_Live" Size','Folder Name','Drive']

"""
Define Functions
"""
def byteconvert(n): #makes byte size more easily readable
	ci = 0
	c_form = '{:,}'.format(n)
	for comma in c_form:
		if comma == ',':
			ci += 1
	if ci == 0:
		return str(n) + ' bytes'
	if ci == 1:
		return str(n)[:c_form.find(',')] + '.' + str(n)[c_form.find(','):c_form.find(',') + 2] + ' KB'
	if ci == 2:
		return str(n)[:c_form.find(',')] + '.' + str(n)[c_form.find(','):c_form.find(',') + 2] + ' MB'
	if ci == 3:
		return str(n)[:c_form.find(',')] + '.' + str(n)[c_form.find(','):c_form.find(',') + 2] + ' GB'
	if ci == 4:
		return str(n)[:c_form.find(',')] + '.' + str(n)[c_form.find(','):c_form.find(',') + 2] + ' TB'

print line
print line
print line

"""
Scan for files
"""

print 'Scanning - ', root

print line

for x in os.walk(root):
	subs = x[0].split('/')
	subname = str(subs[len(rootsplit) + 1:len(rootsplit) + 2])[2:-2]
	subfolder = root + '/' + subname
	if 'datasize.txt' in os.listdir(subfolder):
		found = subfolder + '/datasize.txt'
		Found_Text_Files.append(found)
	else:
		for y in x[2]:
			if subname != '':
				if subname[0] != '.':
					ff = x[0] + '/' + y
					Folders.append([subname,ff])
			elif y[0] != '.':
				rf = x[0] + '/' + y
				Files.append(rf)

for a in set(Found_Text_Files):
	print 'Summary Found -', a

print line

for b in Folders:
	print 'File in Folder Found - ',b[0],b[1], byteconvert(os.path.getsize(b[1]))

print line

for z in Files:
	print 'Loose File in Root -', z, byteconvert(os.path.getsize(z))
	FileBytes += os.path.getsize(z)

print line

while i < len(Folders):
	FolderBytes += os.path.getsize(Folders[i][1])
	fcheck = Folders[i][0]
	i += 1
	if i == len(Folders):
		FBin.append([Folders[i - 1][0], byteconvert(FolderBytes)])
		print Folders[i - 1][0], byteconvert(FolderBytes)
		break
	elif Folders[i][0] != fcheck:
		FBin.append([Folders[i - 1][0], byteconvert(FolderBytes)])
		print Folders[i - 1][0], byteconvert(FolderBytes)
		FolderBytes = 0

print line

print 'Loose Files -', byteconvert(FileBytes)

print line

print 'Free Space: ' + byteconvert(os.statvfs(root).f_bavail * os.statvfs(root).f_frsize)

"""
Write data
"""
if True:
	dlout = open(root + '/' + drive + ' drivedata.csv', 'w')
	typer = csv.writer(dlout)
	typer.writerow(firstline)

	if len(set(Found_Text_Files)) != 0:
		for x in set(Found_Text_Files):
			folder = str(x.split('/')[len(x.split('/')) - 2:len(x.split('/')) -1])[2:-2]
			f = open(x,'rU')
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

	if len(FBin) != 0:
		for f in FBin:
			folder_entry = [f[0],'-',f[1],'-','-','-','-',drive]
			typer.writerow(folder_entry)

	if len(Files) != 0:
		looseentry = ['Loose Files','-',byteconvert(FileBytes),'-','-','-','-',drive]
		typer.writerow(looseentry)

	typer.writerow(['Free Space:','-',byteconvert(os.statvfs(root).f_bavail * os.statvfs(root).f_frsize),'-','-','-','-',drive])
		
print line
print line
print line