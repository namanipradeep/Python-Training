name= "python programing"

print(name)

print(name.capitalize())

print(name.upper())

# name[0]='z' #  it will give error because it Immutable(Unchange)

# print("after replacing:",name)

print(name.center(40))

print(name.center(40,"*"))

print(name.count("p"))

print(name.endswith("z"))

print(name.isalnum())

aname="I am working in {} and {}"

print(aname.format("python","dot net"))

print(aname.format("python",3))

output=name.split(" ")

print(output)


name="        python program   "

print(name.strip())
print(name.lstrip())
print(name.rstrip())

name="python"
print(name.rjust(20))

print(name.encode())

print(len(aname))

print(aname.format("python","dot net").rjust(20))


name="python program"
print(name.replace("python","dotnet"))

