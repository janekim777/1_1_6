#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]
direction =45
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color=turtle_colors.pop()
  t.pencolor(new_color)
  my_turtles.append(t)
  t.fillcolor(new_color)

# giving the x and y coordinates value of 0
t.penup()
startx = 0
starty = 0
t.pendown()
# makng the connectors to connect the shapes

for t in my_turtles:
  t.goto(startx, starty)
  t.right(45)
  t.forward(50) 
  #	moving 50 units between the shapes
  startx=t.xcor()
  starty=t.ycor()
  direction = t.heading ()
  t.right(direction)
  





wn = trtl.Screen()
wn.mainloop()