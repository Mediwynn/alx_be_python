def perform_operation(num1, num2, operation):
    result = None
    op = ['add', 'substract', 'multiply','divide']

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
        
        if num2 != 0:
            result = num1 * num2
            return result
        else:
            msg = print("INVALID SECOND NUMBER")
            return msg
        
    else:
        msg = print("INVALID OPERATION INPUT")
        return msg