# name=input("What's your name?")

# with open("name.txt", "a") as file:
#   file.write(f"{name}\n")

# file.close()

with open("name.txt","r") as file:
#   lines = file.readlines()

# for line in lines:
#   print("hello,",line.rstrip())

    for line in file:
        print("hello,",line.rstrip())
        