# Javion Connelly
# P1HW2
# 9/13/2026
# Creating a program that does basic math operations

print("Welcome to the vacation calculator!")

# Get users budget
budget = input("What is your budget?: ")

# Get users destination
Destination = input("What is your destination?: ")

# Get the users cost on gas
gas = input("What is the cost of gas?: ")

# Get the users cost on food
food = input("What is the cost of food?: ")

# Get the users accomadation cost
accommodation = input("What is the cost of accommodation?: ")

# Add expences the subtract
total = int(gas) + int(food) + int(accommodation)

# Subtract the total from the budget
amount_left = int(budget) - total

print()

# Display the users summary
print("Initial budget:", budget)
print("Gas expense:", gas)
print("Food expense:", food)
print("Cost on accommodations:", accommodation)
print("Your vacation spot!:", Destination)

print()
# Display Total budeget left
print("Remaining balance: ", amount_left)