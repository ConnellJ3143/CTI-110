# 10/1/2026
# Javion Connelly
# Using loops to draw shapes

import turtle

# Set the window and drawing object (turtle)
window = turtle.Screen()
darwin = turtle.Turtle()

darwin.pensize(2)
darwin.pencolor("orange")


# For loop to draw a square
for pointer in range(4):
    darwin.forward(200)
    darwin.right(90)

# For loop to draw a triangle
num = 1
while num <= 3:
    # Draw a side
    darwin.forward(200)
    darwin.left(120)
    
    # Increment num
    num = num + 1


# Keep the window open
window.mainloop()