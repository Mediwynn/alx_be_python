result = None
num1 = None
num2 = None

def safe_divide(numerator, denominator):
    def isnum(up, down):
        try:
            num1 = float(up)
            num2 = float(down)
        except ValueError:
            print("Invalid input")
        else:
            return True

    if isnum(numerator, denominator) == True:
        try:
            result = numerator / denominator
    
        except ZeroDivisionError:
            print("Cannot divide by ZERO")
        else:
            return result