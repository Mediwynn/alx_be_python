num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        result = num1 + num2
        print("the result is ", result)

    case '-':
        result = num1 - num2
        print("the result is ", result)

    case '*':
        result = num1 * num2
        print("the result is ", result)

    case '/':
        if num2 != 0:
            result = num1 / num2
            print("the result is ", result)
        
        else:
            print("ERROR cannot divide by 0")

    case _:
        print("INVALID INPUT")
        