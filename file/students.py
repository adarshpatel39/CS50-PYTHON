

students=[]

with open("students.csv") as file:
  for line in file:
    name,house=line.rstrip().split(",")

    student={"name":name,"house":house}

    # student["name"]=name
    # student["house"]=house
    students.append(student)

# def get_name(student):
#   return student["name"]

for student in sorted(students,key=lambda student:student["name"] , reverse=False):
  print(f"{student['name']} is in {student['house']}")