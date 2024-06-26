userin = int(input("Enter the size of the pattern: "))

block = "*"

while userin >= 0:  
    if userin >= 0:
        for i in range(userin):
            for j in range(userin):
                print(block, end=' ')
            print()
    else:
        print("Please enter a valid non-negative integer for the size of the grid.")
