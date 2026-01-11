# Ask the user for a temperature in Celsius (string input). Convert it to ,
# then calculate and print temperature in Fahrenheit.

# Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 32

celsius_input = input("Enter temperature in Celsius: ")
celsius_temp = float(celsius_input)
fahrenheit_temp = (celsius_temp * (9/5)) + 32
print("Temperature in Fahrenheit:", fahrenheit_temp)