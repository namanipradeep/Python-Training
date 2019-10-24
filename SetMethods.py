alist=[]
alsit=list()

atup=()
atup=tuple()

#/empty set
aset=set()
print(aset)


aset={10,20,13,25}
bset={20,25,30,45}

aset.add(40)
bset.add(60)
bset.add(10)

print(aset)
print(bset)
print(aset.union(bset))

print(aset.intersection(bset))

print(aset.issubset(bset))

print(aset.issuperset(bset))

cset={1,2,3}
dset={1,2,3,4,5}

print(cset.issubset(dset))

print(dset.issuperset(cset))