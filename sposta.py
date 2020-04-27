import os
import shutil
sourcepath=r'C:\Users\*****\Downloads'
sourcefiles = os.listdir(sourcepath)
destinationpath = r'C:\Users\****\Downloads\PDF_FILES'
for file in sourcefiles:
    if file.endswith('.pdf'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
