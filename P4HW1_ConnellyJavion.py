# Javion Connelly
# 9/22/26
# P2HW2
# Display student grade averages with highest, lowest and sum of grades

# Get inputs from user
grade1 = float(input("Enter the first module grade: "))
grade2 = float(input("Enter the second module grade: "))
grade3 = float(input("Enter the third module grade: "))
grade4 = float(input("Enter the fourth module grade: "))
grade5 = float(input("Enter the fifth module grade: "))
grade6 = float(input("Enter the sixth module grade: "))

print()

for num in range(1,101):
    if grade1 <0 or grade1 >100:
        print("Error! Please enter a score between 0 and 100!")
        grade1 = float(input("Enter the first module grade: "))
    if grade2 <0 or grade2 >100:
        print("Error! Please enter a score between 0 and 100!")
        grade2 = float(input("Enter the second module grade: "))
    if grade3 <0 or grade3 >100:
        print("Error! Please enter a score between 0 and 100!")
        grade3 = float(input("Enter the third module grade: "))
    if grade4 <0 or grade4 >100:
        print("Error! Please enter a score between 0 and 100!")
        grade4 = float(input("Enter the fourth module grade: "))
    if grade5 <0 or grade5 >100:
        print("Error! Please enter a score between 0 and 100!")
        grade5 = float(input("Enter the fifth module grade: "))
    if grade6 <0 or grade6 >100:
        print("Error! Please enter a score between 0 and 100!")
        grade6 = float(input("Enter the sixth module grade: "))



# Create a list to hold grades
grade_list = [grade1, grade2, grade3, grade4, grade5, grade6]

print()
print("-------------------Results--------------------")

# Display Highest and lowest grade
print(f"Lowest grade: {min(grade_list)}")

print(f"Highest grade: {max(grade_list)}")

# Display The sum and average of grade
grade_total = sum(grade_list)
print(f"Sum of grades:{grade_total}")

average = sum(grade_list)/len(grade_list)
print(f"Average:{average:.2f}")