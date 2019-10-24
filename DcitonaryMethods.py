adict={"chap1":10,"chap2":20,"chap3":30}

print(adict)

print(adict["chap1"])

#add values
adict["chap4"]=40
adict["chap5"]=50
print(adict)

print(adict.keys()) # display ala keys

print(adict.values()) # display all values

print(adict.items()) # display all items

#print(adict["chap6"])

print(adict.get("chap6"))

print(adict.get("chap6",60)) # just display the value

bdict={"chap7":70,"chap8":80,"chap9":90}

adict.update(bdict) # combine 2 dictionaries

print(adict)

adict.pop("chap1")
print("After removing chap1",adict)

adict.popitem() #will remove random values
print("After pop item",adict)

adict.setdefault("chap10",100)
print("after updating",adict)


