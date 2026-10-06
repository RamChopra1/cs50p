# students = ["hermione", "harry" , "roy"]
# houses =  ["gryffindor", "gryffindor", "griffindor", "slytherin"]
# # for student in students:
# #     print(student)

# for i in range(len(students)):
#     print(i +1  , students[i])


# dictionaries

# students = {
#     "hermione": {"house": "gryffindor", "patronus": "otter"},
#     "harry": {"house": "gryffindor", "patronus": "stag"},
#     "ron": {"house": "gryffindor", "patronus": "jack Russell terrier"},
#     "draco": {"house": "slytherin", "patronus": "water snake"}
# }

# # print(students["hermione"])

# for student in students:
#     print(student, students[student] , sep =",")


#dictionary under list 
students=  [
     {"name":"hermione","house":"gryfindor","patronus":"otter"},
     {"name":"harry", "house": "gryffindor", "patronus": "stag"},
     {"name":"ron", "house": "gryffindor", "patronus": "jack russell terrier"},
     {"name":"draco", "house": "slytherin", "patronus": None}
]


for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ") 