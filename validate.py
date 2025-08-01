
import re
email=input("What's your email?").strip()

# username,domain=email.split("@")

# if username and "." in domain. endswith(".com"):
#   print("valid email")
# else:
#   print("invalid")
if re.search(r"^[^@].+@[^@]+\.edu$",email):
  print ("valid")
else:
  print("invalid")