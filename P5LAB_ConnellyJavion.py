# Javion Connelly
# 11/10/26
# Use of loops, functions and module import to complete assignments
# Self-checkout program

import random


def disperse_change(change):
    
    if change == 0:
        print("No change due")
        
    # Calculate the amount of each coin needed
    num_dollars = change // 100
    change = change - (num_dollars * 100)
    
    num_quarters = change // 25
    change = change - (num_quarters * 25)
    
    num_dimes = change // 10
    change = change - (num_dimes * 10)
    
    num_nickels = change // 5
    change = change - (num_nickels * 5)
    
    num_pennies = change // 1
    change = change - (num_pennies * 1)
    
    # Display change owed
    if num_dollars > 0:
        print(num_dollars, end='')
        if num_dollars == 1:
            print(" Dollar")
        else:
            print(" Dollars")
    
    if num_quarters > 0:
        print(num_quarters, end='')
        if num_quarters == 1:
            print(" quarter")
        else:
            print(" quarters")
    
    if num_dimes > 0:
        print(num_dimes, end='')
        if num_dimes == 1:
            print(" Dime")
        else:
            print(" Dimes")
    
    if num_nickels > 0:
        print(num_nickels, end='')
        if num_nickels == 1:
            print(" Nickel")
        else:
            print(" Nickels")
    
    if num_pennies > 0:
        print(num_pennies, end='')
        if num_pennies == 1:
            print(" Penny")
        else:
            print(" Pennies")

def main():
    
    # Generate a random float with 2 decimal places as the amount that the customer owes
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    
    # Display the amount owed
    print(f"You owe ${amount_owed:.2f}")
    
    # Prompt the user to enter a float as the cash they will put into the checkout machine
    amount = float(input("Insert amount owed: "))
    
    # Calculate change owed
    change = amount - amount_owed
    
    # Display change owed
    print(f"Change is ${change:.2f}")
    
    # Convert change owed to an integer
    change = round(change * 100)
    
    # Call the function and pass change as the parameter
    disperse_change(change)
    
# Call main
main()