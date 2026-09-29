# Javion Connelly
# 9/29/26
# P3HW1
# Display student grade 

# Get inputs from user
grade1 = float(input("Enter the first module grade: "))
grade2 = float(input("Enter the second module grade: "))
grade3 = float(input("Enter the third module grade: "))
grade4 = float(input("Enter the fourth module grade: "))
grade5 = float(input("Enter the fifth module grade: "))
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

avg = sum(grade_list)/len(grade_list)
print(f"Average:{avg:.2f}")

print("----------------------------------------------")

# Round average to the nearest integer
avg = round(avg)

# Braching to determine letter grade based on average
if avg >= 90:
    grade_report = "A"
elif avg >= 80:
    grade_report = "B"
elif avg >= 70:
    grade_report = "C"
elif avg >= 60:
    grade_report = "D"
else:
    grade_report = "F"

print(f"Your Letter grade is: {grade_report} Your average is: {avg}")
