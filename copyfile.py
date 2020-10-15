import shutil

#creates a copy in the scripts folder
#shutil.copy("<filepath>", "<targetlocation>")
shutil.copy('fractal_turtle.py', 'scripts')

#copies a folder and creates a new one
shutil.copytree('scripts', 'scriptsbackup')

"""BOTH OF THESE FUNCTIONS RETURN PATH TO NEW FILE/FOLDER"""

#shutil.move(src, dest)
#now this removes from old directory)
#can also rename
