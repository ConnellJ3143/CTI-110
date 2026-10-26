# Javion Connelly
# 10/25/26
# Create a loop to view add a new emoployee


print("💰Paycheck Calculator💰")

total_employees = 0
total_grosspay = 0
total_hours = 0
total_OT_hours = 0

repeat = ""

while repeat.lower() != "done":

    # Get name
    name = input("Enter employee name: ")

    # Get hours worked for the week
    hours = float(input("Enter hours worked for the week: "))

    # Get base pay rate
    base_payrate = float(input("Enter base pay rate: $"))


    # If statement is true whent they work more than 40 hrs
    if hours > 40:
        OT_hours = hours - 40
        OT_pay = OT_hours * (base_payrate*1.5)
        reg_pay = base_payrate * 40
        grosspay = OT_pay + reg_pay
        
    if hours <= 40:
        OT_hours = 0
        OT_pay = 0
        reg_pay = base_payrate * hours
        grosspay = OT_pay + reg_pay

     # Display results
    print(f"Employee name: {name}")
    print(f"Hours Worked: {hours}")
    print(f"Pay Rate: ${base_payrate:.2f}")
    print(f"Overtime: {OT_hours}")
    print(f"Overtime Pay: ${OT_pay:.2f}")
    print(f"RegHour Pay: ${reg_pay:.2f}")
    print(f"Gross Pay: ${grosspay:.2f}")

    print()

    total_employees = total_employees + 1
    total_hours = total_hours + hours
    total_grosspay = total_grosspay + grosspay
    total_OT_hours = total_OT_hours + OT_hours

    repeat = input("Add another employee or type 'Done' to finish: ")

print(f"Number of employees entered: {total_employees}")
print(f"Total Hours Worked: {total_hours}")
print(f"Total amount paid in gross: ${total_grosspay:.2f}")
print(f"Total Overtime Hours: {total_OT_hours}")
