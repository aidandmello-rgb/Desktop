import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().title("Polygon")
turtle.Screen().setup(300, 400)
num_lines = int(turtle.textinput("Polygon", "Enter the number of sides for the polygon: "))
side_length = int(turtle.textinput("Polygon", "Enter the length of each side: "))
angle = 360 / num_lines
for i in range(num_lines):
    turtle.forward(side_length)
    turtle.right(angle)
turtle.done()