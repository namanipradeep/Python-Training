# first questiom
'''
a=input("enter file name")

b=a.split(".")

print("filename:" ,b[0])
print("Extension:",b[1])

'''
# second question

'''
a=input("enter any delimited string")

b=a.split(",")

print("list of elements are:" ,b)

print(len(b))

'''

# third question

'''
atup=()
atup=tuple()
#print(atup)
alist=[]
alist=["unix"]
atup=tuple(alist)

alsit=list(atup)

alist.extend(['spark', 'scala','hadoop','sccm'])
atup=tuple(alist)
#print(atup)
alist.extend(['c','cpp','java','salesforce','sap','unix'])
atup=tuple(alist)
#print(atup)

alist.remove('java')
alist.remove('salesforce')
atup=tuple(alist)
#print(atup)

alist.insert(0,'oracle')
alist.insert(5,'mongodb')

atup=tuple(alist)
#print(atup)

alist.sort()
alist.reverse()
atup=tuple(alist)
#print(atup)
unixcount=alist.count("unix")
print("Unix count:",unixcount)
print("length of elements:", len(alist))

'''

# Fourth program
'''
numbers = (10,20,10,20,30,40,60,70)

aset=set(numbers)
print(aset)
'''

# fifth program

'''
first=input("enter first number")
second=input("enter second number")

sum=int(first)+int(second)
print("total:",sum)

'''

# sixth program
'''
name=input("enter Python program")

print(name.replace("python","scala"))

'''

# seventh program
'''
alist = [10,20,30,40,50,10]
blist = [40,50,60,70,80]

aset=set(alist)
bset=set(blist)
print(aset)
print(bset)

print("common values:",aset.intersection(bset))

'''

# eighth program
'''
lang = "perl,unix,hadoop,scala,spark,ruby,go"
val=lang.find('python')
if val>0:
    print('python is existing')
else:
    print('python is not existing')

'''

# ninth program
'''
name="this is program"

print(name.upper())
lts=list(name)
print(name.rjust(30))
print(name.lower())

'''

# tenth program
'''
name=input("enter file name")
if name.endswith(".py"):
    print("Its python file")
elif name.endswith(".pl"):
     print("Its perl  file")
elif name.endswith(".c"):
     print("Its C lang  file")
elif name.endswith(".json"):
     print("Its Json  file")
     
     '''
# eleven pgm
'''
import socket
addr=input("enter IP Adress")

try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")
'''

# 12th program
'''
name=input("enter the string")

if name.isupper():
    print(name.lower())
elif name.islower():
    print(name.upper())
'''

# 13 th program
'''
username=input("enter the username") 
password=input("enter the password")
if len(password)>5 and len(password)<12 and( any(x in password for x in ('@', '*', '$'))) and (!password.isupper()):
    print("success")
'''
# 14th program
'''
alist = ["unix","hadoop","oracle","scala"]
alist.append("spark")

atouple=tuple(alist)

print(atouple)
'''   

#15th Program
'''
for x in range(51):
    print(x)
'''

#16th program
'''
for x in range(20,10):
'''

# dictonary
'''
colors = [
{
"colors": "red",
"values": "#f00"
},
{
"colors": "green",
"values": "#0f0"
},
{
"colors": "blue",
"values": "#00f"
},
{
"colors": "cyan",
"values": "#0ff"
},
{
"colors": "magenta",
"values": "#f0f"
},
{
"colors": "yellow",
"values": "#ff0"
},
{
"colors": "black",
"values": "#000"
}
]

for dlr in colors:
    print(dlr["colors"]+"("+dlr["values"]+")")
'''

# 2nd
dictry={
"id": "0001",
"type": "donut",
"name": "Cake",
"image":
{
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail":
{
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}

'''
keys=dictry.keys()
values=dictry.values()
print(keys)
#print(keys[0].ljust(10)+":")
'''

#for p_id, p_info in dictry.items():
 #   print(p_id.ljust(10)+":"+p_info)
    
  #  for key in p_info:
   #     print(key.ljust(10) + ':', p_info[key])
   
for key in dictry:
    if isinstance(dictry[key],str):
        print(str(key).ljust(10)+":"+ str(dictry[key]))
    elif isinstance(dictry[key],list):
        
        