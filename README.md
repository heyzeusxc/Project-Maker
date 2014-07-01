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

'datafinder.py' should be put in the drive of wherever multiple
projects are placed.  This searches each project folder for the
"datasize.txt", and creates and entry for each one in a .csv file named
after the drive.
