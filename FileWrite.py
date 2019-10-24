fobj=open("client.txt","w")

fobj.write("Python programing learning\n")
fobj.write("Scala programing")
fobj.close()




## using context manager

with open("demo.txt","w") as fobj:
    fobj.write("unix shell\n")
    fobj.write("unix shell2\n")
    fobj.write("unix shell3\n")
    
## if you wnat to specify the your own path
''''
open("C:\\Users\\Admin\\Desktop\\client.txt") --- double slash

or

open("C:/Users/Admin/Desktop/client.txt") -- forward slash
'''