# Javion Connelly
# 9/24/26
# Enhancing existing programs and aligning lists

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
total = float(gas) + float(food) + float(accommodation)

# Subtract the total from the budget
amount_left = float(budget) - total

print()

# Display the users summary
print("--------------------Travel Expenses-------------------------")
print(f"{'Location':<16}{Destination:<17}")
print(f"{'Initial Budget':<16}${budget:<17}")
print(f"{'Fuel':<16}${gas:<17}")
print(f"{'Food':<16}${food:<17}")
print(f"{'Accommodation':<16}${accommodation:<17}")
print("-" * 60)

print()
# Display Total budeget left
print("Remaining balance: ", amount_left)