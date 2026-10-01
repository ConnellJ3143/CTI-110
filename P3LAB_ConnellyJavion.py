# 10/1/2026
# Javion Connelly
# Using Branching and functions to display coin combinations

# Get value from user
money = float(input("Enter money amount: $"))
if money == 0.00:
    print("No change")

#print(f"Dollars submitted: ${money}")

#Converting the value to an integer
money_int = int(money * 100)

#print(f"Converted as an integer: {money_int}")

#print()

################### Dollars #########################
# Determine how many dollars are needed
dollars = money_int // 100
# Remove the dollars from money_int
money_int = money_int % 100

#print(f"Dollars: {dollars}")
#print(f"Leftover: {money_int}")


################### Quarters #########################
# Determine how many quarters are needed
quarters = money_int // 25
# Remove the dollars from money_int
money_int = money_int % 25

#print(f"Quarters: {quarters}")
#print(f"Leftover: {money_int}")


################### Dimes #########################
# Determine how many Dimes are needed
dimes = money_int // 10
# Remove the dollars from money_int
money_int = money_int % 10

#print(f"Dimes: {dimes}")
#print(f"Leftover: {money_int}")


################### Nickels #########################
# Determine how many Nickels are needed
nickels = money_int // 5
# Remove the dollars from money_int
money_int = money_int % 5

#print(f"Nickels: {nickels}")
#print(f"Leftover: {money_int}")


################### Pennies #########################
# Determine how many Pennies are needed
pennies = money_int // 1
# Remove the dollars from money_int
money_int = money_int % 1

#print(f"Pennies: {pennies}")
#print(f"Leftover: {money_int}")

print()

# Define a function to show the coins only if needed
def show_coins(coin, coin_name):
    if coin > 0:
        if coin == 1:
            print(f" 1 {coin_name}")
        if coin > 1:
            if coin_name == "Penny":
                print(f"{coin} pennies")
            else:
                print(f"{coin} {coin_name}s")

# Call the function for each of the coins
show_coins(dollars, "Dollar")
show_coins(quarters, "Quarter")
show_coins(dimes, "Dime")
show_coins(nickels, "Nickel")
show_coins(pennies, "Penny")