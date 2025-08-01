#from random import choice
import random
coin= random.choice(["head","tail"])

number=random.randint(1,10)

cards=["jack","queen","king"]
random.shuffle(cards)
for c in cards:
  print(c)

  
print()
print(number)
print (coin)