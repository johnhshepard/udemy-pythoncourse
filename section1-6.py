# Exercise 1-6: KM to Miles Converter
# Create a program that asks the user for a number in kilometers and converts it to miles.
print("Welcome to the Kilometers to Miles Converter.")
# Ask the user for a number in kilometers.
kilometers = float(input("How many kilomerters would you like to convert to miles? "))
# Convert the input to miles using: 1 mile = 1.606344 Km
miles = kilometers / 1.606344
# Print the result.
print(str(kilometers) + " kilometers converts to " + str(miles) + " miles.")
