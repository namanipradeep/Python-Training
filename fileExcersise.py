#write a program to display all the lines from the file
'''
try:
    with open("Sacramentorealestatetransactions.csv","r") as fobj:
        for line in fobj:
            line=line.strip()
            print(line)
            
except Exception as error:
    print("System error",error)
'''

#write a program to display STREET and CITY from the file
'''
try:
    with open("Sacramentorealestatetransactions.csv","r") as fobj:
        for line in fobj:
            line=line.strip()
            alist=line.split(",")
            print("Street:  "+alist[0]+"City:  "+alist[1])
            
except Exception as error:
    print("System error:",error)
 
'''

#write a program to display all the  UNIQUE cities from the file
'''
aset=set()
try:
    with open("Sacramentorealestatetransactions.csv","r") as fobj:
        for line in fobj:
            line=line.strip()
            line=line.split(",")
            aset.add(line[1])
        print(aset)
except Exception as error:
    print("System error:",error)
'''

# write  a program to display each city and the no. of times it has been repeated
'''
try:
    with open("Sacramentorealestatetransactions.csv","r") as fobj:
        for line in fobj:
            line=line.split(",")
            alist=line
        print(alist)
'''

# Display all files in current directory line by line
'''
import os
#print(os.listdir())
for x in os.listdir():
    print(x)
'''
# Display all files from C drive
'''
import os
for x in os.listdir("C:\\"):
    print(x)
'''

#display all files and its size
'''
import os
for x in os.listdir():
   # print("file name:"+x + " File size is:"+os.path.getsize(x))
   print("file name:"+ str(x) + " File size is: "+ str(os.path.getsize(x)))
'''

# write a pragram to display files and directory
''' not at completed
import os
file=[]
dire=[]
for x in os.listdir("C:\\"):
    if os.path.isfile(x):
        file.append(x)
    elif os.path.isdir(x):
        dire.append(x)
    for line in file:
        print(line)    
    for line1 in dire:
        print(dire)
'''

# 
import getpass
import os
from datetime import datetime
import calendar
import platform
import sys
import socket
print("Current user name:"+ getpass.getuser())
print("Current working directory:"+ os.getcwd())
print(datetime.now())
print(" Below is this month calendar")
yy = 2019
mm = 10
print(calendar.month(yy, mm))
print("Current process id:" + str(os.getpid()))
print(len(os.listdir(os.getcwd())))
print("Current operating system:"+platform.system())
print("Current python version:"+ sys.version)
print("Socket name is"+socket.gethostname())