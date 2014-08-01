"""
Import os, sys, and csv
"""
import os
import sys
import csv

"""
Set standard variables
"""

columns = ['Project Number','Project Title','Total Size','"01_Recording" Size','"02_Edit" Size','"03_Live" Size','Folder Name','Drive']

print '*' * 10
print '*' * 10
print '*' * 10

print os.sys.path[0]

"""
Creates a master .csv file to list all other .csv files in the folder
"""

with open(os.sys.path[0] + '/' + 'Archived Data.csv', 'wb') as master:
	typer = csv.writer(master)
	typer.writerow(columns)

	for x in os.listdir(os.sys.path[0]):
		if x[0] == '.':
			pass
		elif '.py' in x:
			pass
		elif '.csv' in x:
			print x[:x.find(' drivedata.csv')]
			print '*' * 10

			with open(os.sys.path[0] + '/' + x, 'r') as file:
				reader = csv.reader(file)
				typer.writerow('*' * 8)
				for y in reader:
					if 'Project Number' in y:
						pass
					else:
						if 'Loose Files' in y:
							print '*' * 10
						print y
						typer.writerow(y)
				file.close()
			print '*' * 10
	master.close()