# Javion Connelly
# 9/10/26
# Inputs, Outputs, Mathematical calculations

print("-------Calculating Exponents--------")
print()
print()

# Get the base value from user and convert to an int
base_value = int(input("Enter a base value: "))

# Get the exponent from user and convert to an int
exponent = int(input("Enter an exponent: "))

# Calculate
Answer = base_value ** exponent 

# Display Answer

print(base_value, "raised to the power of", exponent, "is", Answer)
print()
print()

print("-------Addition and Subtraction--------")
print()
print()

# Get three integers from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter number to add: "))
num3 = int(input("Enter number to subtract: "))

print()


# Display answer
print(num1, "+", num2, "-", num3, "=", num1 + num2 - num3)
