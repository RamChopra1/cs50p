import sys 
# try:
#  print("hello, my name is", sys.argv[1])
# except IndexError:
#  print("Too few arguments")

#check for errors
if len(sys.argv)<2:
    sys.exit("too few arguments")
# elif len(sys.argv)>2:
#     sys.exit("too many arguments")
for arg in sys.argv[1:]:
    print("Hello, my name is" , arg)