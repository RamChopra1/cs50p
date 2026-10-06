# def main():
#     print_column(4)



# def print_column(height):
#     # for _ in range(height):
#     #     print("#")
#     print("#\n"*height,end ="")

# main()


# def main():
#     print_row(4)



# def print_row(width):
#     print("?"*width)

# main()

# def main():
#     print_column(6)
#     print_row(6)


# def print_column(height):
#     print("#\n"*height, end="")
# def print_row(width):
#     print("#"*width)

# main()
#making a 3*3 square

def main():
    print_square(4)

def print_square(size):

    # #for each row in square 
    # for i in range(size):


    #     #for each column 
    #     for j in range(size):
    #         print("#", end="")
    #     print()


    for i , j in range(size):
        print("#",end="")

    print()

main()

