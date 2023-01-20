f_people = ["Gerrard", "Will Smith", "Torres", "Patrick Bateman"]
message = (f"Hey, {f_people[0].title()} would you like to come to my dinner service")
print(message)
message = (f"\nHey, {f_people[1].title()} would you like to come to my dinner service")
print(message)
message = (f"\nHey, {f_people[2].title()} would you like to come to my dinner service")
print(message)
message = (f"\nHey, {f_people[3].title()} would you like to come to my dinner service")
print(message)

print(f"\nSorry to hear you couldn't make it {f_people[1].title()} hopefully you can next time")
del f_people[1]
f_people.insert(1, "Jamal")
message = (f"\nHey, {f_people[1].title()} would you like to come to my dinner service as Will couldnt make it")
print(message)