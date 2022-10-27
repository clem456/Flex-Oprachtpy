import turtle

times = 1

while times <= 3:
    for i in range(4):
        turtle.right(90)
        turtle.forward(150/times)

    times += 1

turtle.clear()

turtle.circle(50)

turtle.clear()

for i in range(3):
    turtle.left(120)
    turtle.forward(150)

turtle.clear()

for i in range(10):
    turtle.right(360/10)
    turtle.forward(60)

turtle.clear()

for i in range(5):
    turtle.left(360/5)
    turtle.forward(120)

turtle.clear()

for i in range(6):
    turtle.left(360/6)
    turtle.forward(120)

turtle.clear()

for i in range(5):
    turtle.right(144)
    turtle.forward(120)