#fixed args
def display(first,second):
    print(first,second)

display(10,20)


#deafult args (optional)
def display(first=0,second=0,third=0):
    print(first,second,third)

display()
display(10)
display(10,20)
display(10,20,30)

#Keyword args
def display(first,second):
    print(first,second)
    
display(second=20,first=10)

#variable length args

def display(*info):   # * means its a tuple
    for val in info:
        print(val)

display(10,30,20,'unix')

#dictonary example
def displayvalues(**values): # ** means its a dictonary
   print(values)

displayvalues(chap1=10,chap2=20)