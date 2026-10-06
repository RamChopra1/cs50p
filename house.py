name =  input("whats your name?")

# if name == "Harry" or name== "Hermione" or name=="Ron":
#     print("gryffindor")
# elif name=="Draco": 
#     print("slytherin")
# else:
#     print("who?")
#match concept methord 1 
# match name:
#     case "harry":
#         print("gryffindor")
#     case "hermione":
#         print("gryffindor")
#     case "ron":
#         print("gryffindor")
#     case "draco":
#         print("slytherin")
#     case _:
#         print("who?")
#methord 2
match name:
    case "harry" | "hermione" | "ron":
        print("gryffindor")
    case "draco":
        print("slytherin")
    case _:
        print("who?")
   