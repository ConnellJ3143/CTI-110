# Javion Connelly
# 9/17/26
# P2LAB2
# Use the dictionary to determine the amount of fuel needed from user input

# Create a dictionary - cars are keys and mpgs are the values
car_mpg = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Select only the keys
keys = car_mpg.keys()

# Display the keys
print()
print(keys)

# Get a car choice from the user
car_choice = input("Enter a car to see its mpg: ")

# using car_choice, pull the associated mpg from the dictionary
mpg = car_mpg[car_choice]

# Display car choice and mpg back to user
print(f"The {car_choice} gets {mpg} mpg.")

# Get miles to drive from user as a float
miles = float(input(f"How many miles will you drive the {car_choice}?: "))

# Calculate gallons of gas needed

gallons = miles/mpg

# Display
print(f"{gallons:.2f} gallons of gas are needed to drive the {car_choice} {miles} miles.")