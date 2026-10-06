# print("meow")
# print("meow") 
# print("meow")
# i = 3 
# while i!=0:
#     print("meow")
#     i = i - 1

# methord 2
# i = 0 
# while i < 3:
#     print("meow")
#     # i = i +1
#     i +=1 


#methord 3 
# for _ in range(3):
#     print("meow")

#methord 4
# print("meow\n"*3, end ="")
#methord 5 
# while True:
#     n = int(input("whats n?"))
#     if n<0:
#         continue
#     else:
#         break
# while True:
#     n = int(input("whats n?"))
#     if n>0:
#         break
# for _ in range(n):
#     print("meow")


#methord 6 
def main():
    number =  get_number()
    meow(number)

def get_number():
    while True:
        n =int(input("what's n?"))
        if n >0:
            return n 

def meow(n):
    for _ in range(n):
        print("meow")

main()