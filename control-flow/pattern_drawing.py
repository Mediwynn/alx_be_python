userin = int(input("Enter the size of the pattern: "))
i = 0
j = 0
block = "*"

while i != userin:  
    if userin >= 0:
        for i in range(userin):

            for j in range(userin):
                print(block, end=' ')
                j = j + 1
            
            i = i + 1
            print()


    else:
        print("Please enter a valid non-negative integer for the size of the grid.")
