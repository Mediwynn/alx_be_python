result = None
num1 = None
num2 = None

def safe_divide(numerator, denominator):
    def isnum(numerator, denominator):
        try:
            num1 = float(numerator)
            num2 = float(denominator)
        except ValueError:
            print("Invalid input")
        else:
            return True

    if isnum(numerator, denominator) == True:
        try:
            result = numerator / denominator
    
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        else:
            return result