def perform_operation(num1, num2, operation):
    result = None
    op = ["add", "subtract", "multiply","divide"]

    if operation == op[0]:
        result = num1 + num2
        return result
    
    elif operation == op[1]:
        result = num1 - num2
        return result
    
    elif operation == op[2]:
        result = num1 * num2
        return result
    
    elif operation == op[3]:
        
        if num2 == 0:
            msg = print("INVALID SECOND NUMBER")
            return msg
        
        else:
            result = num1 / num2
            return result
        
    else:
        msg = print("INVALID OPERATION INPUT")
        return msg