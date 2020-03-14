# Exercise 1-6: KM to Miles Converter
# Create a program that asks the user for a number in kilometers and converts it to miles.
print("Welcome to the Miles to Kilometers Converter.")
# Ask the user for a number in kilometers.
miles = float(input("How many miles would you like to convert to kilometers? "))
# Convert the input to miles using: 1 mile = 1.606344 Km
kilometers = miles * 1.606344
# Print the result.
print(str(miles) + " miles converts to " + str(kilometers) + " kilometers.")
