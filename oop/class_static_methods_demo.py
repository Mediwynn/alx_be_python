class Calculator:
    calculation_type = "Arithmetic Operations"

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def add(a, b):
        addition = a + b
        return addition

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation Type: {cls.calculation_type}")
        cls.multiply = a * b
        return cls.multiply