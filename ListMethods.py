alist=[10,20,30,48,75]

alist.append(40) # for single value
print("after appending:",alist)

alist.extend([1,25,9001,584,10]) # for assigning multiple valus

print("after extendiding:",alist)

getcount=alist.count(10)

print(getcount)

alist.insert(0,5) #index and value

print("after Insertinging:",alist)

alist.insert(4,45)

print("after Insertinging:",alist)

alist.pop()

print("after pop:",alist)

alist.pop(0) #index

print("after pop:",alist)

alist.remove(48) #remove value

print("after pop:",alist)

alist.sort()

print("after sorting:",alist)

alist.reverse()

print("after reversing:",alist)