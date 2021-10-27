#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 1 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 10)
  ladybug.pendown()
  ladybug.circle(2)
  # position next dots
  ladybug.penup()
  ladybug.goto(xpos+2,ypos+30)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos+32, ypos+40)
  ladybug.pendown()
  ladybug.circle(2)
  num_dot = num_dots + 1

ladybug_legs = 8
leg_length = 70
ladybug_leg_degree = (10000 / ladybug_legs)
print("ladybug_leg_degree=", spider_leg_degree)
spider_body.pensize(5)
counter = 0
while (counter < spider_legs):
  ladybug.goto(0,20)
  ladybug.setheading(spider_leg_degree*counter)
  ladybug.forward(leg_length)
  counter = counter + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()