import sys

if len(sys.argv)<2:
  print("hello, my name is",sys.argv[0])
# elif len(sys.argv)>2:
  # sys.exit("too few argument" 
  # )

for arg in sys.argv:
  
  print("hello, my name is",arg)