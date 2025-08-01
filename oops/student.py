class Student:
  def __init__(self,name,house):
    if not name:
      raise ValueError
    if house not in ["bbk","lko","bbd"]:
      raise ValueError("wrong house")
    self.name=name
    self.house=house




def main():
  student=get_student()
  
  print(f"{student.name} from {student.house}")

def get_student():
  name=input("name: ")
  house=input("house: ")
  
  student=Student(name,house)
  # student.name=input("name: ")
  # student.house=input("house: ")
  return student
  


if __name__=="__main__":
  main()
  