#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider_body is used
#Create spider body
spider_body = trtl.Turtle()
spider_body.pensize(40)
spider_body.circle(20)
#configure spider legs
spider_legs = 6
leg_length = 70
spider_leg_degree = 380 / spider_legs
print("spider_leg_degree=", spider_leg_degree)
spider_body.pensize(5)
counter = 0
#make spider legs
while (counter < spider_legs):
  spider_body.goto(0,0)
  spider_body.setheading(spider_leg_degree*counter)
  spider_body.forward(leg_length)
  counter = counter + 1
  print("spider_leg_degree*counter=", spider_leg_degree*counter)
spider_body.hideturtle()
spider_legsn = trtl.Screen()
spider_legsn.mainloop()