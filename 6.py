#--------------------GENERAL TURTLE EXPLANATION--------------------
import turtle as t

t.tracer(0)
t.screensize(2000,2000)
step = 20

for x in range(2):
    t.forward(21 * step)
    t.right(90)
    t.forward(27 * step)
    t.right(90)
t.up()
t.forward(9*step)
t.right(90)
t.forward(10 * step)
t.left(90)
t.down()
for x in range(2):
    t.forward(86 * step)
    t.right(90)
    t.forward(47 * step)
    t.right(90)

t.up()
for x in range(-40,40):
    for y in range(-40,40):
        t.goto(x*step,y*step)
        t.dot(4,"Red")

t.exitonclick()

#------------------------------------------------------------------