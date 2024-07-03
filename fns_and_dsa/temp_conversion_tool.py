FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):  #conversion from fahrenheit to celsius
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius): #conversion from celsius to fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperature = input("Enter the temperature to convert: ").strip() #get init temp

conversion_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper() #determine what init temp is

conversion_options = ["F", "C"]

if temperature.isdigit():
    temp = int(temperature)
    if conversion_type in conversion_options:
        if conversion_type == "F":
            C = convert_to_celsius(temp)
            print(f"{temp}\u00b0F is {C}\u00b0C")
        else:
            F = convert_to_fahrenheit(temp)
            print(f"{temp}\u00b0C is {F}\u00b0F")
    else:
        print("Incorrect conversion option")
else:
    print("INVALID TEMPERATURE INPUT")

