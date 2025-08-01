# class two_D_vector():
#   def __init__(self,i,j):
#     self.i=i
#     self.j=j
#   def show(self):
#     print(f"{self.i}i+{self.j}j ")

# class three_D_Vector(two_D_vector):
#   def __init__(self,i,j,k):
#     super().__init__(i,j)
#     self.k=k
#   def show(self):
#     print(f"{self.i}i+{self.j}j+{self.k}k ")

# a=two_D_vector(2,5)
# b=three_D_Vector(4,10,3)
# a.show()
# b.show()

    
# class animal():
#   pass
# class pet(animal):
#   pass
  
# class dog(pet):
#   @staticmethod
#   def bark():
#     print("bow bow!")
# c=dog()
# c.bark()


# class employee():
#   salary=300
#   increment=50
#   @property
#   def afterIncrement(self):
#     return (self.salary+(self.salary*self.increment)/100)
#   @increment.setter
#   def increment(self,value):
#     return 


# a=employee()
# print(a.afterIncrement)


class complex():
  def __init__(self,real,imaginary):
    self.real=real
    self.imaginary=imaginary
  def show(self):
    print(f"{self.real}+i*{self.imaginary}")
  
a=complex(2,5)
a.show()

    