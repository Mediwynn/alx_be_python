class Calculator:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def add(num1, num2):
        addition = num1 + num2
        return addition

    @classmethod
    def multiply(cls, num1, num2):
        cls.multiply = num1 * num2
        return cls.multiply