import os
import shutil
sourcepath=r'C:\Users\*****\Downloads'  #specify your own source
sourcefiles = os.listdir(sourcepath)    
destinationpath = r'C:\Users\****\Downloads\PDF_FILES'    #specify your own destination
for file in sourcefiles:
    if file.endswith('.pdf'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
