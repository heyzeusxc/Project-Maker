Project-Maker
=============

Sets up folders for my projects at work

'projectmaker.py' creates a project folder based off user input.  Setup
for how my place of work categorizes projects.

'stamper.py' will put the current date on any files in the
"datestamper" folder as well as create a new blank folder for the day's
date in the "02_Edit/Exports" folder.

'bytecounter.py' calculates creates a .txt file of number of bytes the
project folder and the first level of subfolders use.

'datafinder 2.py' should be put in the drive of wherever multiple
projects are placed.  This searches each project folder for the
"datasize.txt", and creates and entry for each one along with any folders and loose files in a .csv file named after the drive.

'datacompiler.py' scans all the .csv files made by 'datafinder 2.py' and creates and master list of all .csv files and data.