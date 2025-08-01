name=input("What's your name?")

# if name=="Harry" or name=="tony":
#   print("Gryffindor")
# elif name=="critian":
#   print("bale")
# else:
#   print ("who?")

match name:
  case "Harry" | "hermoine" | "ROn":
    print("griffonder")
  case "jonny":
    print("depp")
  case _:
    print("Who?")