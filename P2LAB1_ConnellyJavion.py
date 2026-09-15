# Javion Connelly
# 9/15/26
# Calculate components of a circle using pi from the math library

import math


# Get radius from user
radius = float(input("Enter the radius: " ))

print()

diameter = 2 * radius

# Display diameter using an f-string
print(f"The diameter of the circle is {diameter:.1f}")

# Calculate circumference
circumference = 2 * math.pi * radius

# Display the circumference using the f-string
print(f"The circumference of the circle is {circumference:.2f}")

# Calculate the area
area = math.pi * pow(radius, 2)

# Display the area using the f-string
print(f"The area of the circle is {area:.3f}")