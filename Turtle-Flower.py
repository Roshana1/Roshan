import turtle
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(False)

# defins how to draw a petal 
def petal(r,steps):
    turtle.circle(r,80,steps)
    turtle.left(90)
    turtle.circle(r,80,steps)
turtle.color("red", "yellow")
# get the radius and steps and draw
r = input("Enter the petal radius")
steps = input("Enter the petal steps")
num = 20
turtle.setx(0)
turtle.sety(0)
for i in xrange (num):
    turtle.setheading(0)
    turtle.left(360*i/num)
    petal(r,steps)
    turtle.setx(0)
    turtle.sety(0)
    turtle.pendown

turtle.tracer(True)
turtle.done()

