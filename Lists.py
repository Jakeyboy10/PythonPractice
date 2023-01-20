names = ["Jake", "Kye", "Kara"]
print (names)

print (names[1])
print (names[0].title())
print (names[1].title())
print (names[2].title())
print (names[-1].title())

message = (f"{names[-1].title()} is my girlfriend")
print (message)
message = (f"{names[1].title()} has the smelliest arsehole ever")
print (message)
message = (f"{names[0].title()} is the best at python")
print (message)

names[0] = "RJ"
print (names)

names.append("Jake")
print(names)
names.insert(0,"Bert")
print(names) 
del names[0]
print (names)

names.remove("RJ")
print (names)
names[0] = "RJ"
too_smelly = "RJ"
names.remove(too_smelly)
print (names)
print (f"\n{too_smelly.title()} is so gross")