try:
    with open("languages.txt","r") as fobj:
        for line in fobj:
            line=line.strip()  #remove one \n (line)
            print(line)
        
except TypeError as error:
    print("Invalid operation")
    print("System Error:",error)
except ValueError as error:
    print("Invalid input")
    print("System Error:",error)
except FileNotFoundError as error:
    print("FileNotFound")
    print("System Error:",error)
except Exception as error:
    print("unknown error")
    print("System Error:",error)
    
    
# By using CSV
import csv

fobj=open("Sacramentorealestatetransactions.csv","r")
reader=csv.reader(fobj)

for line in reader:
    print(line)
    
############file in the list format
fobj=open("Sacramentorealestatetransactions.csv","r")
print(fobj.readlines())  # whole file in the list
fobj.close()
    