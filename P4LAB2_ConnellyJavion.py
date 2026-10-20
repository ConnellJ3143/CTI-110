# Javion Connelly
# 10/20/26
# Nested Loops

# Create the variable that controls the while loop
# This value is temporary
run_again = "yes"

while run_again == "yes":
    # Get an integer from the user
    integer = int(input("Enter an integer: "))
    
    # Check if integer is positive
    if integer >= 0:
        # Display multiplication
        for table in range(1,13):
            print(f"{integer} * {table} = {integer * table}")
    # If the number is negative
    else:
        print("Enter a positive whole number!")
    
    # Allow the user to give a new value to run again
    run_again = input("Run the program again? ").lower()
    
# Loop Breaks here
print("Program has ended")