question = input ("Would you like to convert Pounds or Fahrenheit: ")
if question.lower() == ("pounds"):
    Pounds = float(input("Enter weight in Pounds: "))
    Kilograms = (Pounds * 0.453592)
    print(f"{Pounds}lbs is equal to {Kilograms:.2f}kgs")
elif question.lower() == ("fahrenheit"):
    Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    Celcius = (Fahrenheit - 32) * 5/9
    print(f"{Fahrenheit}°F is equal to {Celcius:.2f}°C")