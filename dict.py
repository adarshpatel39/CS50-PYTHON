# students=["Hermione", "Harry", "Ron","Draco"]
# house=["Gyyfindor","Gyyfindor","Gyyfindor","Slytherin"]

# students={                   "Hermoine":"gryffindor",
#   "harry":"Gryffindor",
#   "Ron":"Slytherin"
#   }
# #print(students["Hermoine"])

# for st in students:
#   print(f"{st},{students[st]}",sep=", ")


students=[
    {"name":"Hermoine","house":"Gryffindor","patronus":"Otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronus":None}

]

for st in students:
  print(st["name"],st["house"],st["patronus"], sep=", ")