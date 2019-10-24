import os
import shutil

def deletefile(filename):
    os.remove(filename)
    print(filename +"is removed")
    
def listfiles(path):
    for x in os.listdir(path):
        print("list of files in given directory"+ str(x))
        
def copyfile(source,destination):
    shutil.copy(source,destination)
    print("copy success")
    
